from django.http import HttpResponse
from django.conf import settings
from urllib.parse import urlencode
import re
import requests

ABSOLUTE_URL = getattr(settings, 'ABSOLUTE_URL', 'localhost:8000')
STEAM_LOGIN_URL = 'https://steamcommunity.com/openid/login'


def auth(response_url, use_ssl=True):
    protocol_re = re.search(r'(?:http)', response_url)
    if protocol_re is None or protocol_re.group(0) is None:
        protocol = 'https' if use_ssl else 'http'
        response_url = '{0}://{1}{2}'.format(protocol, ABSOLUTE_URL, response_url)

    params = {
        'openid.ns': 'http://specs.openid.net/auth/2.0',
        'openid.mode': 'checkid_setup',
        'openid.return_to': response_url,
        'openid.realm': response_url,
        'openid.identity': 'http://specs.openid.net/auth/2.0/identifier_select',
        'openid.claimed_id': 'http://specs.openid.net/auth/2.0/identifier_select',
    }

    response = HttpResponse()
    response['Location'] = f'{STEAM_LOGIN_URL}?{urlencode(params)}'
    response['Content-Type'] = 'application/x-www-form-urlencoded'
    response.status_code = 302
    return response


def get_uid(results):
    results = dict(results)

    args = {
        'openid.assoc_handle': results['openid.assoc_handle'][0],
        'openid.signed': results['openid.signed'][0],
        'openid.sig': results['openid.sig'][0],
        'openid.ns': results['openid.ns'][0]
    }

    signed_args = results['openid.signed'][0].split(',')

    for arg in signed_args:
        arg = 'openid.{0}'.format(arg)
        if results[arg][0] not in args:
            args[arg] = results[arg][0]

    args['openid.mode'] = 'check_authentication'

    response = requests.post(STEAM_LOGIN_URL, args)

    if re.search(r'is_valid:true', response.text):
        matches = re.search(r'https://steamcommunity.com/openid/id/(\d+)', results['openid.claimed_id'][0])
        if matches is not None and matches.group(1) is not None:
            return matches.group(1)
        else:
            return None
    else:
        return None
