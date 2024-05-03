from fastapi import HTTPException, status

book_not_found = HTTPException(
    status_code = status.HTTP_404_NOT_FOUND,
    detail = "Book not found"
)
duplicated_title = HTTPException(
    status_code = status.HTTP_409_CONFLICT,
    detail = "Book with that title already exists in database"
)