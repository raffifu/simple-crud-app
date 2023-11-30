from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def generate():
    return {"message": "Hello World!"}
