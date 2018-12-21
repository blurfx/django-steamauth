# django-steamauth
make steam openid authorization easily

## Dependency
- requests
- Django >= 1.7

## Install
```
pip install django-steamauth
```


## Usage
You should set ABSOLUTE_URL at settings.py for redirection after login. default is 'localhost'
```python
# settings.py

ABSOLUTE_URL='127.0.0.1:8000'
# or
ABSOLUTE_URL='yourowndomain.com'
```

You can retrive user id with `get_uid` method when a login is successful
```python
#views.py

from steamauth import auth, get_uid

# /login
def login(request):
    # if your service supports ssl, set use_ssl parameters value to True
    # if use_ssl options are turned on, auth returns https url. if not it returns http url.
    return auth('/process', use_ssl=True)

# /process
def login_process(request):
    steam_uid = get_uid(request.GET)
    if steamid == False:
        # login failed
        return redirect('/login_failed')
    else:
        # login success
        # do something with variable `steamid`
        return redirect('/')
    

```
