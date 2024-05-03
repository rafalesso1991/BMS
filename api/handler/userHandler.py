from fastapi import HTTPException, status

user_not_found = HTTPException(
    status_code = status.HTTP_404_NOT_FOUND,
    detail = "User not found"
)

duplicated_username = HTTPException(
    status_code = status.HTTP_409_CONFLICT,
    detail = "User with that name already registered"
)

duplicated_email = HTTPException(
    status_code = status.HTTP_409_CONFLICT,
    detail = "User with that email already registered"
)
