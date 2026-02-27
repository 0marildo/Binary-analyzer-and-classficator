from pydantic import BaseModel
from typing import List

class AnalyseResponse(BaseModel):
    num_blocks: int
    clusters: List[int]
    features: List[List[float]]
    plot: str #string em base64
    summary: dict #quantos blocos são headers, raw data, offset 
    
