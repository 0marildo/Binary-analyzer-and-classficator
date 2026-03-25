from fastapi import APIRouter, UploadFile, File, HTTPException
from services.binary_analyzer import process_binary_file
from schemas.analyze import AnalyseResponse
import tracemalloc

router = APIRouter(prefix="/api/v1", tags=["analyze"])

MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB

@router.post("/analyze", response_model=AnalyseResponse)
async def analyze(file: UploadFile = File(...)):
    tracemalloc.start()

    if not file.filename.endswith(".bin"):
        raise HTTPException(status_code=400, detail="Only .bin files are allowed")

    try:
        data = await file.read()

        if len(data) > MAX_FILE_SIZE:
            raise HTTPException(status_code=413, detail="File too large. Maximum size is 50MB")
        if len(data) == 0:
            raise HTTPException(status_code=400, detail="File is empty")

        result = process_binary_file(data)
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 10**6:.2f} MB; Peak: {peak / 10**6:.2f} MB")
        tracemalloc.stop()
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
