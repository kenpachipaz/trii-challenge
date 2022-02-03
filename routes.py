from fastapi import APIRouter
from models import Status
import requests

# api-endpoint
URL = "https://rickandmortyapi.com/api"
router = APIRouter(prefix="/api/v1")

@router.get("/character")
async def root(page:int, name:str, status: Status):
    return requests.get(URL + "/character", params={"page": page, "name": name, "status": status}).json()