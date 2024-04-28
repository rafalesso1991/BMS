from fastapi import HTTPException

# HTTP EXCEPTION "TITLE NOT FOUND"
def title_not_found():
    raise HTTPException(status_code=404, detail="Title not found")
