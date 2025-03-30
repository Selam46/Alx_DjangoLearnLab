# Social Media API - Posts & Comments

## Endpoints

### Posts
- `GET /api/posts/` - List all posts
- `POST /api/posts/` - Create a post (requires authentication)
- `GET /api/posts/{id}/` - Retrieve a post
- `PUT /api/posts/{id}/` - Update a post (requires authentication)
- `DELETE /api/posts/{id}/` - Delete a post (requires authentication)

### Comments
- `GET /api/comments/` - List all comments
- `POST /api/comments/` - Create a comment (requires authentication)
- `GET /api/comments/{id}/` - Retrieve a comment
- `PUT /api/comments/{id}/` - Update a comment (requires authentication)
- `DELETE /api/comments/{id}/` - Delete a comment (requires authentication)

## Authentication
All protected endpoints require authentication via Token.
