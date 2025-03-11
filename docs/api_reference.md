# API Reference Documentation

## Overview

This document provides a detailed reference for the API endpoints available in the FastAPI application. Each endpoint is described with its method, path, request parameters, and response structure.

## Base URL

The base URL for the API is:

```
http://localhost:8000/api
```

## Endpoints

### 1. Example Endpoint

- **Method:** `GET`
- **Path:** `/example`
- **Description:** Retrieves an example resource.

#### Request Parameters

| Parameter | Type   | Required | Description                |
|-----------|--------|----------|----------------------------|
| id        | int    | Yes      | The ID of the resource.    |

#### Response

- **Status Code:** `200 OK`
- **Content:**

```json
{
  "id": 1,
  "name": "Example Resource",
  "description": "This is an example resource."
}
```

### 2. Create Example Endpoint

- **Method:** `POST`
- **Path:** `/example`
- **Description:** Creates a new example resource.

#### Request Body

- **Content-Type:** `application/json`
- **Body:**

```json
{
  "name": "New Resource",
  "description": "Description of the new resource."
}
```

#### Response

- **Status Code:** `201 Created`
- **Content:**

```json
{
  "id": 2,
  "name": "New Resource",
  "description": "Description of the new resource."
}
```

### 3. Update Example Endpoint

- **Method:** `PUT`
- **Path:** `/example/{id}`
- **Description:** Updates an existing example resource.

#### Request Parameters

| Parameter | Type   | Required | Description                |
|-----------|--------|----------|----------------------------|
| id        | int    | Yes      | The ID of the resource.    |

#### Request Body

- **Content-Type:** `application/json`
- **Body:**

```json
{
  "name": "Updated Resource",
  "description": "Updated description."
}
```

#### Response

- **Status Code:** `200 OK`
- **Content:**

```json
{
  "id": 1,
  "name": "Updated Resource",
  "description": "Updated description."
}
```

### 4. Delete Example Endpoint

- **Method:** `DELETE`
- **Path:** `/example/{id}`
- **Description:** Deletes an example resource.

#### Request Parameters

| Parameter | Type   | Required | Description                |
|-----------|--------|----------|----------------------------|
| id        | int    | Yes      | The ID of the resource.    |

#### Response

- **Status Code:** `204 No Content`

## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of requests. Common error responses include:

- **400 Bad Request:** The request was invalid.
- **404 Not Found:** The requested resource was not found.
- **500 Internal Server Error:** An unexpected error occurred on the server.

## Conclusion

This API reference provides a comprehensive overview of the available endpoints and their usage. For further details, please refer to the source code or other documentation files in the project.