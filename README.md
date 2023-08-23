# Zoozle
Apis

## create APi

```
http://127.0.0.1:8003/account/accountapi/
parameters:-- post
{
    "password": "1234",
    "email": "utkash.rastogi@cvia.comlp",
    "first_name": "utkarsh",
    "phone_number": 8279911219
}

```

## list api

```
http://127.0.0.1:8003/account/accountapi/
get
```
## delete
```
http://127.0.0.1:8003/account/accountapi/1/
```
## detail

```
http://127.0.0.1:8003/account/accountapi/detail/
get
```

## login
```
http://127.0.0.1:8003/account/accountapi/login/
parameter
{
    "email": "utkash.rastogi@clovia.colmlp",
    "password": "1234"
}
post
```