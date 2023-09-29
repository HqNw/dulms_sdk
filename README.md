# DULMS SDK

this package is a simple non official SDK for [DULMS](https://dulms.deltauniv.edu.eg/login.aspx)

```note
this package is still in development and the responses are pure from the server without any sanitization

```



# usage
## login
```python
from delta_sdk import delta_auth

auth = delta_auth.login("https://dulms.deltauniv.edu.eg")
auth.auth("USERNAME", "PASSWORD")
```

## get user data
```python
from delta_sdk import delta_auth

auth = delta_auth.login("https://dulms.deltauniv.edu.eg")
auth.auth("USERNAME", "PASSWORD")

data = auth.get_user_data()
print(data)
```



