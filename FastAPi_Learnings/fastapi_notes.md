# FastAPI Notes

## What is FastAPI?
- A modern Python web framework for building APIs.
- Acts as the **application server layer** for handling HTTP requests and responses.
- Built on top of **Starlette** (for web handling and async support).
- Starlette is built on top of **ASGI (Asynchronous Server Gateway Interface)**.
- Since FastAPI uses ASGI, it is commonly run with the **Uvicorn** server.

## Why is development fast in FastAPI?
- Uses **Pydantic** for automatic data validation.
- Automatic request and response **serialization**.
- Generates interactive **OpenAPI documentation** automatically.
  - Swagger UI: `/docs`
  - ReDoc: `/redoc`
- Simple and clean Python syntax.
- Strong type-hint support improves editor autocomplete and error checking.

## Benefits of FastAPI
- Automatic API documentation.
- Built-in data validation.
- High performance with asynchronous support.
- Easy and rapid development.
- Easy dependency injection system.
- Strong community and ecosystem support.

## FastAPI vs Django vs Flask

### Django
- Built on **WSGI (Web Server Gateway Interface)**.
- Full-featured framework (ORM, admin panel, authentication, etc.).
- Best for large web applications.

### Flask
- Also built on **WSGI**.
- Lightweight and minimal framework.
- More manual setup compared to Django and FastAPI.

### FastAPI
- Built on **ASGI**.
- Native support for **async/await**.
- Better suited for high-performance APIs and microservices.
- Automatic validation and documentation out of the box.

## WSGI vs ASGI

### WSGI
- Handles **synchronous** requests.
- One request is processed at a time per worker.
- Suitable for traditional web applications.

### ASGI
- Handles **asynchronous** requests.
- Can manage many concurrent connections efficiently.
- Suitable for APIs, WebSockets, and real-time applications.

## Quick Comparison

| Feature | FastAPI | Flask | Django |
|---|---|---|---|
| Interface | ASGI | WSGI | WSGI |
| Async support | Native | Limited | Partial |
| Auto validation | Yes | No | No |
| Auto API docs | Yes | No | No |
| Performance | High | Medium | Medium |
| Best use case | APIs & microservices | Small apps | Full-stack web apps |

## Common FastAPI Commands

Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

Run the development server:

```bash
uvicorn main:app --reload
```

- `main` → Python file name (`main.py`)
- `app` → FastAPI instance (`app = FastAPI()`)
- `--reload` → automatically reloads on code changes

---


# REST API Notes

## What is a REST API?
- **REST (Representational State Transfer)** is an architectural style for communication between a **client** and a **server** over HTTP.
- A REST API exposes **resources** through URLs and allows clients to perform operations using HTTP methods.

---

## Fundamental Building Blocks

### Resources / Endpoints / URLs
- A **resource** is any data or object managed by the API.
- An **endpoint** is the URL used to access a resource.

Examples:
- `/users`
- `/users/1`
- `/products/10`

---

## Request

### HTTP Methods

| Method | Purpose | SQL Analogy |
|---|---|---|
| **GET** | Retrieve data | SELECT |
| **POST** | Create new data | INSERT |
| **PUT** | Update existing data | UPDATE |
| **DELETE** | Remove data | DELETE |

### Examples
- `GET /users` → fetch all users
- `POST /users` → create a user
- `PUT /users/1` → update user with ID 1
- `DELETE /users/1` → delete user with ID 1

---

## Headers
- Sent as **key-value pairs**.
- Used for:
  - Authentication (`Authorization: Bearer <token>`)
  - Content type (`Content-Type: application/json`)
  - Accept type (`Accept: application/json`)

Example:
```http
Authorization: Bearer abc123
Content-Type: application/json
```

---

## Request Body
- Contains the data sent to the server.
- Commonly used with **POST** and **PUT** requests.
- Usually sent in **JSON** format.

Example:
```json
{
  "name": "Rahul",
  "age": 25
}
```

---

## Request Parameters

### Path Parameters
- Part of the URL path.
- Used to identify a specific resource.

Example:
```http
GET /users/10
```

Here, `10` is the **path parameter**.

### Query Parameters
- Added after `?` in the URL.
- Used for filtering, searching, sorting, and pagination.

Example:
```http
GET /users?city=Mumbai&page=1
```

- `city=Mumbai`
- `page=1`

---

# Response

## HTTP Status Codes

### 2xx — Success
- `200 OK` → request successful
- `201 Created` → resource created
- `204 No Content` → success with no response body

### 4xx — Client Errors
- `400 Bad Request` → invalid request
- `401 Unauthorized` → authentication required
- `403 Forbidden` → access denied
- `404 Not Found` → resource not found

### 5xx — Server Errors
- `500 Internal Server Error`
- `502 Bad Gateway`
- `503 Service Unavailable`

---

## Response Body
- Contains the data returned by the server.
- Can be in:
  - **JSON** (most common)
  - **Text**
  - **Binary** (images, files, PDFs, etc.)

Example JSON response:
```json
{
  "id": 1,
  "name": "Rahul",
  "city": "Mumbai"
}
```

---

## Complete Example

### Request
```http
POST /users
Content-Type: application/json
```

Request body:
```json
{
  "name": "Amit",
  "age": 30
}
```

### Response
```http
201 Created
Content-Type: application/json
```

Response body:
```json
{
  "id": 101,
  "name": "Amit",
  "age": 30
}
```

---

## Quick Flow

- **Client** sends an HTTP request.
- **Server** processes the request.
- **Server** returns an HTTP response with a status code and an optional response body.
- **Client** reads the response and updates the UI or performs further actions.