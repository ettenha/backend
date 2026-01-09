from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uuid, shutil
import uvicorn
from ocr import extract_stats

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract")
async def extract(file: UploadFile = File(...)):
    path = f"/tmp/{uuid.uuid4()}.png"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return extract_stats(path)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
