from fastapi import APIRouter


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
async def register_view():
    pass


@router.post("/login")
async def login_view():
    pass
