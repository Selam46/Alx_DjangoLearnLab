# Django REST API for Books

## Endpoints
- `GET /api/books/` → List all books (Public)
- `GET /api/books/<id>/` → Retrieve a book (Public)
- `POST /api/books/create/` → Create a new book (Authenticated)
- `PUT /api/books/<id>/update/` → Update a book (Authenticated)
- `DELETE /api/books/<id>/delete/` → Delete a book (Authenticated)

## Permissions
- Authenticated users can create, update, and delete books.
- Unauthenticated users can only view books.

## How to Test
- Use **Postman**, **cURL**, or **Django Admin**.
