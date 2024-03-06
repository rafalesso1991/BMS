Requirements
1. PostgreSQL DDBB
• Create tables: "Users" one-to-many "Books" relationship
• "users" table: "id", "name", "email" and "password" (hashed)
• "books" table: "id", "name, "desc" and "owner"
2. FastAPI Models
• Reflects DDBB table's structure
• Includes 'Pydantic' validations "email" in "users" "owner" in "books" with "name" in "users"
3. CRUD Operations
• Both Tables: "CREATE", "READ" ("GET"), "UPDATE" and "DELETE"
4. Login functionality
• Allow user authentication • Verify hash password stored in DDBB
5. Filter "Books" by Logged-In "User"
• API returns filtered books associated with Logged-In User