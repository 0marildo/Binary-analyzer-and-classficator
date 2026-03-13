from fastapi import APIRouter, UploadFile, File, HTTPException
from services.binary_analyzer import process_binary_file
from schemas.analyze import AnalyseResponse
import tracemalloc
router = APIRouter(prefix="/api/v1", tags=["analyze"])

@router.post("/analyze", response_model=AnalyseResponse)
async def analyze(file: UploadFile = File(...)):
    tracemalloc.start()
    
    
    if not file.filename.endswith(".bin"):
        raise HTTPException(status_code=400, detail="O arquivo deve ser um .bin")
    
    try:
        data = await file.read()
        result = process_binary_file(data)
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 10**6:.2f} MB; Peak: {peak / 10**6:.2f} MB")
        tracemalloc.stop()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
