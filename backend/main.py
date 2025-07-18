from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import easyocr
import pandas as pd
import shutil
import os

app = FastAPI()

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
RESULTS_XLSX = "output.xlsx"
os.makedirs(UPLOAD_DIR, exist_ok=True)
reader = easyocr.Reader(['en'])

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    # OCR
    result = reader.readtext(file_location, detail=0)
    # Save to Excel
    df = pd.DataFrame({"Trailer ID": result})
    df.to_excel(RESULTS_XLSX, index=False)
    return {"ids": result}

@app.get("/download/")
def download_excel():
    if os.path.exists(RESULTS_XLSX):
        return FileResponse(RESULTS_XLSX, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=RESULTS_XLSX)
    return JSONResponse(status_code=404, content={"error": "No results found."}) 