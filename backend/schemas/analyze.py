from pydantic import BaseModel
from typing import List

class AnalyseResponse(BaseModel):
    num_blocks: int
    clusters: List[int]
    plot: str #string em base64
    summary: dict #quantos blocos são headers, raw data, offset
