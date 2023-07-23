# Endpoints

[Back to main readme](../README.md)

Below is a list of the available endpoints:

- [Client](#client)
- [Address](#address)

---------

# Client

[top](#endpoints) ⬆️

## Create Client

- Method: POST

```
{{url}}/api/v1/management/client/
```

- Example Request:

```json
{
  "email": "maguilera0810@gmail.com",
  "first_name": "Mauricio",
  "last_name": "Aguilera",
  "identification_type": "DNI",
  "identification": "0123456789",
  "cellphone": "0999999999",
  "main_address": {
    "province": "Guayas",
    "city": "Guayaquil",
    "address": "Calle 1 y Calle 2"
  }
}
```

- Example Response:

```json
{
  "id": 5,
  "email": "maguilera0810@gmail.com",
  "first_name": "Mauricio",
  "last_name": "Aguilera",
  "identification_type": "DNI",
  "identification": "0123456789",
  "cellphone": "0999999999",
  "main_address": {
    "id": 3,
    "province": "Guayas",
    "city": "Guayaquil",
    "address": "Calle 1 y Calle 2",
    "is_matriz": true,
    "client": 5
  }
}
```

## Get Client

- Method: GET

```
{{url}}/api/v1/management/client/{{client_id}}
```

- Example Response:

```json
{
  "id": 5,
  "email": "maguilera0810@gmail.com",
  "first_name": "Mauricio",
  "last_name": "Aguilera",
  "identification_type": "DNI",
  "identification": "0123456789",
  "cellphone": "0999999999",
  "main_address": {
    "id": 3,
    "province": "Guayas",
    "city": "Guayaquil",
    "address": "Calle 1 y Calle 2",
    "is_matriz": true,
    "client": 5
  }
}
```

## List Client

- Method: GET
- QueryParams: You can filter the data with the following filters by passing as queryparams
  - **email (optional)**
  - **first_name (optional)**
  - **last_name (optional)**
  - **identification_type (optional)**
  - **identification (optional)**
  - **cellphone (optional)**

```
{{url}}/api/v1/management/client/
```

- Example Response:

```json
[ 
  {
    "id": 5,
    "email": "maguilera0810@gmail.com",
    "first_name": "Mauricio",
    "last_name": "Aguilera",
    "identification_type": "DNI",
    "identification": "0123456789",
    "cellphone": "0999999999",
    "main_address": {
      "id": 3,
      "province": "Guayas",
      "city": "Guayaquil",
      "address": "Calle 1 y Calle 2",
      "is_matriz": true,
      "client": 5
    }
  }
]
```

## Update Client

- Method: PUT

```
{{url}}/api/v1/management/client/{{client_id}}
```

- Example Request:

```json
{
  "email": "maguilera0810@gmail.com",
  "first_name": "Mauricio",
  "last_name": "Aguilera",
  "identification_type": "DNI",
  "identification": "0123456789",
  "cellphone": "0999999999",
}
```

- Example Response:

```json
{
  "id": 5,
  "email": "maguilera0810@gmail.com",
  "first_name": "Mauricio",
  "last_name": "Aguilera",
  "identification_type": "DNI",
  "identification": "0123456789",
  "cellphone": "0999999999",
  "main_address": {
    "id": 3,
    "province": "Guayas",
    "city": "Guayaquil",
    "address": "Calle 1 y Calle 2",
    "is_matriz": true,
    "client": 5
  }
}
```

## Delete Client

- Method: DELETE

```
{{url}}/api/v1/management/client/{{client_id}}
```

- Example Response:

```json
{}
```

---

# Address

[top](#endpoints) ⬆️

## Create Address

- Method: POST

```
{{url}}/api/v1/management/address/
```

- Example Request:

```json
{
  "province": "Peru",
  "city": "Lima",
  "address": "Calle 1 y Calle 2 ",
  "is_matriz": false,
  "client": 4
}
```

- Example Response:

```json
{
  "id": 7,
  "province": "Peru",
  "city": "Lima",
  "address": "Calle 1 y Calle 2 ",
  "is_matriz": false,
  "client": 4
}
```

## Get Address

- Method: GET

```
{{url}}/api/v1/management/address/{{address_id}}
```

- Example Response:

```json
{
  "id": 7,
  "province": "Peru",
  "city": "Lima",
  "address": "Calle 1 y Calle 2 ",
  "is_matriz": false,
  "client": 4
}
```

## List Addresses

- Method: GET
- QueryParams: You can filter the data with the following filters by passing as queryparams
  - **province (optional)**
  - **city (optional)**
  - **address (optional)**
  - **is_matriz (optional)**
  - **client (optional)**

```
{{url}}/api/v1/management/address/
```

- Example Response:

```json
[ 
  {
    "id": 7,
    "province": "Peru",
    "city": "Lima",
    "address": "Calle 1 y Calle 2 ",
    "is_matriz": false,
    "client": 4
  }
]
```

## Update Address

- Method: PUT

```
{{url}}/api/v1/management/address/{{client_id}}
```

- Example Request:

```json
{
  "province": "Peru",
  "city": "Lima",
  "address": "Calle 1 y Calle 2 ",
  "is_matriz": false,
  "client": 4
}
```

- Example Response:

```json
{
    "id": 7,
    "province": "Peru",
    "city": "Lima",
    "address": "Calle 1 y Calle 2 ",
    "is_matriz": false,
    "client": 4
  }
```

## Delete Address

- Method: DELETE

```
{{url}}/api/v1/management/address/{{address_id}}
```

- Example Response:

```json
{}
```

---
