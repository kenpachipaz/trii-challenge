from fastapi import APIRouter
from zipfile import ZIP_DEFLATED, ZipFile
from fastapi.responses import FileResponse
import requests

# api-endpoint
URL = "https://rickandmortyapi.com/api"
router = APIRouter(prefix="/api/v1")

#TODO: Delete file after response
@router.get("/download-zip/{document_name}", response_class=FileResponse)
def download_zip(document_name:str):
    zipName = document_name + ".zip"
    json = requests.get(URL + "/character/1").text
    with ZipFile(zipName, mode="w", compression=ZIP_DEFLATED) as zip: 
        zip.writestr(document_name + ".json", json)
        zip.close()
    attachment = "attachment;filename=" + zipName
    return FileResponse(zipName, media_type="application/zip", headers = {"Content-Disposition": attachment })