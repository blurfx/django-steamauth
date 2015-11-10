# django-steamauth
make steam openid authorization easily

## Install
```
pip install django-steamauth
```


## Usage
You should set ABSOLUTE_URL at settings.py for redirection after login. default is 'localhost'
```python
# settings.py

ABSOLUTE_URL = '127.0.0.1:8000'
# or
ABSOLUTE_URL = 'yourowndomain.com'
```

You can retrive SteamID64 when a login is successful
```python
#views.py

from steamauth import *

# /login
def Login(request):
  return RedirectToSteamSignIn('/process')

# /process
def LoginProcess(request):
    steamid = GetSteamID64(request.GET)
    if steamid == False:
        # login failed
        return redirect('/login_failed')
    else:
        # login success
        return redirect('/')
    

```
