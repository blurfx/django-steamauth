# django-steamauth
make steam openid authorization easily

## Dependency
- requests
- Django >= 1.7

## Install
### Python >= 3
```bash
pip install django-steamauth
```


### Python 2.x
```bash
pip install django-steamauth==1.1.1
```

## Usage
You should set `ABSOLUTE_URL` in `settings.py` for redirection after login. default is `localhost`

```python
# settings.py

ABSOLUTE_URL='127.0.0.1:8000'
# or
ABSOLUTE_URL='yourowndomain.com'
```

You can retrive user id with `get_uid` method when a login is successful.

```python
# views.py
from django.shortcuts import redirect
from steamauth import auth, get_uid

# GET /login
def login(request):
    # if your service does not support ssl, set use_ssl parameters value to False
    # return auth('/callback', use_ssl=False)
    return auth('/callback')

# GET /process
def login_callback(request):
    steam_uid = get_uid(request.GET)
    if steam_uid is None:
        # login failed
        return redirect('/login_failed')
    else:
        # login success
        # do something with variable `steam_uid`
        return redirect('/')
```

## Changelog

### 1.1.2

- Dropping Python 2 Support
- Remove deprecated interfaces: `RedirectToSteamSignIn`, `GetSteamID64`
- Change the default value of `ABSOLUTE_URL` from `localhost` to `localhost:8000`
- Fix an issue `use_ssl` parameter of `auth` didn't work ([#6](https://github.com/blurfx/django-steamauth/issues/6))
- Set default value of `use_ssl` to `True` 
