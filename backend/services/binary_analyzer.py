import numpy as np
from ml.analyzer import analyze_binary
from collections import Counter

def process_binary_file(data: bytes) -> dict:
    result = analyze_binary(data)

    clusters_list = result["clusters"]
    cluster_counts = Counter(clusters_list)
    
    summary = {"header": 0, "raw_data": 0, "offset": 0}
    for cluster_id, count in cluster_counts.items():
        if cluster_id == -1:
            summary["offset"] += count
        else:
            summary["raw_data"] += count

    print("Cluster counts:", dict(cluster_counts))
    print("Summary:", summary)

    # Remove features do result antes de retornar
    result.pop("features", None)

    return {**result, "summary": summary}