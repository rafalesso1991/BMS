from fastapi import HTTPException, status

# 401 UN-AUTORIZED
credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = {"WWW-Authenticate": "Bearer"},
    )

inactive_user_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Inactive user",
    )

# 404 NOT FOUND
book_not_found_exception = HTTPException(
    status_code = status.HTTP_404_NOT_FOUND,
    detail = "Book not found"
)

user_not_found_exception = HTTPException(
    status_code = status.HTTP_404_NOT_FOUND,
    detail = "User not found"
)

# 409 DATABASE CONFLICT
duplicated_username_exception = HTTPException(
    status_code = status.HTTP_409_CONFLICT,
    detail = "User with that Name already registered"
)

duplicated_email_exception = HTTPException(
    status_code = status.HTTP_409_CONFLICT,
    detail = "User with that Email already registered"
)
