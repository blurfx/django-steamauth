from django.http import HttpResponse
from urllib.parse import urlencode
from django.conf import settings
import re, requests

ABSOLUTE_URL = getattr(settings, 'ABSOLUTE_URL', 'localhost')

STEAM_LOGIN_URL = 'http://steamcommunity.com/openid/login'

def RedirectToSteamSignIn(responseURL):
    refinedScripts = re.search('(?:http)', responseURL)
    if refinedScripts == None or refinedScripts.group(0) == None:
        responseURL = "http://{0}{1}".format(ABSOLUTE_URL,responseURL)

    authParameters = {
        "openid.ns": "http://specs.openid.net/auth/2.0",
        "openid.mode": "checkid_setup",
        "openid.return_to": responseURL,
        "openid.realm": responseURL,
        "openid.identity": "http://specs.openid.net/auth/2.0/identifier_select",
        "openid.claimed_id": "http://specs.openid.net/auth/2.0/identifier_select"
    }

    response = HttpResponse()
    response['Location'] = "{0}?{1}".format(STEAM_LOGIN_URL, urlencode(authParameters))
    response['Content-Type'] = 'application/x-www-form-urlencoded'
    response.status_code = 302
    return response

def GetSteamID64(results):
    results = dict(results)

    validationArgs = {
        'openid.assoc_handle': results['openid.assoc_handle'][0],
        'openid.signed': results['openid.signed'][0],
        'openid.sig': results['openid.sig'][0],
        'openid.ns': results['openid.ns'][0]
    }

    # Basically, we split apart one of the args steam sends back only to send it back to them to validate!
    # We also append check_authentication which tells OpenID 2 to actually yknow, validate what we send.
    signedArgs = results['openid.signed'][0].split(',')

    for item in signedArgs:
        itemArg = 'openid.{0}'.format(item)
        if results[itemArg][0] not in validationArgs:
            validationArgs[itemArg] = results[itemArg][0]

    validationArgs['openid.mode'] = 'check_authentication'

    # Just use requests to quickly fire the data off.
    reqData = requests.post(STEAM_LOGIN_URL, validationArgs)
    reqData.connection.close()

    # is_valid:true is what Steam returns if something is valid. The alternative is is_valid:false which obviously, is false.
    if re.search('is_valid:true', reqData.text):
        matched64ID = re.search('http://steamcommunity.com/openid/id/(\d+)', results['openid.claimed_id'][0])
        if matched64ID != None or matched64ID.group(1) != None:
            return matched64ID.group(1)
        else:
            # If we somehow fail to get a valid steam64ID, just return false
            return False
    else:
        # Same again here
        return False