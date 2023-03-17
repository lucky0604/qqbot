from fastapi import APIRouter, Response

home_router = APIRouter()


@home_router.get("/test")
async def home():
    return Response(status_code=200, content={"hello": "world"})