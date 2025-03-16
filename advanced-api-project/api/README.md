# 📖 Advanced Django API Project

## 🔍 Filtering, Searching, and Ordering

### 1️⃣ **Filtering**
| Query Parameter | Description | Example |
|----------------|-------------|----------|
| `?publication_year=YYYY` | Filter books by publication year | `/api/books/?publication_year=2023` |
| `?author__name=AUTHOR_NAME` | Filter books by author name | `/api/books/?author__name=J.K. Rowling` |

### 2️⃣ **Searching**
| Query Parameter | Description | Example |
|----------------|-------------|----------|
| `?search=keyword` | Search books by title or author name | `/api/books/?search=Harry` |

### 3️⃣ **Ordering**
| Query Parameter | Description | Example |
|----------------|-------------|----------|
| `?ordering=title` | Order books by title (ascending) | `/api/books/?ordering=title` |
| `?ordering=-publication_year` | Order books by publication year (descending) | `/api/books/?ordering=-publication_year` |

---

# ✅ Unit Testing Django REST Framework APIs

## 📌 Running the Tests
To run all tests:
```bash
python manage.py test api
