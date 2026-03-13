from pydantic import BaseModel
from typing import List, Optional

class AnalyseResponse(BaseModel):
    num_blocks: int
    clusters: List[int]
    features: List[List[float]]
    plot: str #string em base64
    summary: dict #quantos blocos são headers, raw data, offset
    silhouette_score: Optional[float] 
    
