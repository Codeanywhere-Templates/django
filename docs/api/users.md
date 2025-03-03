# Users

Supports registering, viewing, and updating user accounts.

## Register a new user account

**Request**:

`POST` `/users/`

Parameters:

| Name       | Type   | Required | Description                            |
| ---------- | ------ | -------- | -------------------------------------- |
| username   | string | Yes      | The username for the new user.         |
| password   | string | Yes      | The password for the new user account. |
| first_name | string | No       | The user's given name.                 |
| last_name  | string | No       | The user's family name.                |
| email      | string | No       | The user's email address.              |

_Note:_

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "username": "john",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@doe.com",
  "auth_token": "132cf952e0165a274bf99e115ab483671b3d9ff6"
}
```

The `auth_token` returned with this response should be stored by the client for
authenticating future requests to the API. See [Authentication](authentication.md).

## Get a user's profile information

**Request**:

`GET` `/users/:id`

Parameters:

_Note:_

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "username": "john",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@doe.com",
}
```

## Update your profile information

**Request**:

`PUT/PATCH` `/users/:id`

Parameters:

| Name       | Type   | Description                        |
| ---------- | ------ | ---------------------------------- |
| first_name | string | The first_name of the user object. |
| last_name  | string | The last_name of the user object.  |
| email      | string | The user's email address.          |

_Note:_

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "12314-124-325-12fae-23",
  "username": "john",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@doe.com",
}
```
