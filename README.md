# Book Management System

## Description


## How to use
 
We first need to run the backend.

for this we use docker-compose and poetry.

```bash
docker-compose up -d
poetry run python3 src/main.py
```

### Testing
For testing its best to first destroy 
```bash
docker-compose down --volumes
docker-compose up
poetry run python -m pytest tests/
```

Now

# Project Requirements
1. PostgreSQL DDBB
• Create tables: "Users" one-to-many "Books" relationship
• "users" table: "id", "username", "email" and "password" (hashed)
• "books" table: "id", "title", "description" and "owner_id"
2. FastAPI Models
• Reflects DDBB table's structure
• Includes 'Pydantic' validations "email" in "users" "owner" in "books" with "name" in "users"
3. CRUD Operations
• Both Tables: "CREATE", "READ" ("GET"), "UPDATE" and "DELETE"
4. Login functionality
• Allow user authentication
• Verify hash password stored in DDBB
5. Filter "Books" by Logged-In "User"
• API returns filtered books associated with Logged-In User