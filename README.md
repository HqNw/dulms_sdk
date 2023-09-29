# DULMS SDK

this package is a simple non official SDK for [DULMS](https://dulms.deltauniv.edu.eg/login.aspx)

```note
this package is still in development and the responses are pure from the server without any sanitization

```

# installation
```bash
pip install delta-sdk
```

# usage
## importing
```python
from delta_sdk import delta_auth
```

## login
```python
auth = delta_auth.Auth("https://dulms.deltauniv.edu.eg")
auth.login("USERNAME", "PASSWORD")
```

## get user data
```python
auth = delta_auth.Auth("https://dulms.deltauniv.edu.eg")
auth.login("USERNAME", "PASSWORD")

data = auth.get_user_data()
print(data)
```

## get assginments
```python
auth = delta_auth.Auth('https://dulms.deltauniv.edu.eg')
auth.login("USERNAME", "PASSWORD")

data = auth.get_assignments()
print(data)
```

## get quizzes
```python
auth = Auth('https://dulms.deltauniv.edu.eg')
auth.login("USERNAME", "PASSWORD")

data = auth.get_quizzes()
print(data)
```

## using the coockies for other uses

```python
auth = Auth('https://dulms.deltauniv.edu.eg')
auth.login("USERNAME", "PASSWORD")

cookies = auth.get_cookies()
print(coockies['Id'])
```
____
```note
the coockies are stored in a dict with the following keys
 - Id
 - ASP.NET_SessionId
```




