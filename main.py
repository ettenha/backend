from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import uuid
import uvicorn
from ocr import extract_stats

app = FastAPI()

# CORS OBLIGATOIRE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract")
async def extract(file: UploadFile = File(...)):
    filename = f"/tmp/{uuid.uuid4()}.png"

    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = extract_stats(filename)
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
