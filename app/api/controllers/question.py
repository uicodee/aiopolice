from fastapi import APIRouter


router = APIRouter(prefix="/question")


@router.get(
    path="/all",
    description="Get all questions"
)
async def questions():
    ...
