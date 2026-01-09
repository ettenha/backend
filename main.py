from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import uuid
from ocr import extract_stats

app = FastAPI()

# 🔥 CORS DOIT ÊTRE ICI, AVANT LES ROUTES
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract")
async def extract(file: UploadFile = File(...)):
    filename = f"/tmp/{uuid.uuid4()}.png"

    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return extract_stats(filename)
