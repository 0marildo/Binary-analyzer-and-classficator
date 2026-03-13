import numpy as np
from .features import entropy_block, byte_zero_ratio, unique_byte_ratio, variance
from .clustering import cluster_blocks
from .plot import cluster_plot

def analyze_binary(data: bytes, block_size=32):
    arr = np.frombuffer(data, dtype=np.uint8)

    blocks = [
        arr[i:i+block_size]
        for i in range(0, len(arr), block_size)
        if len(arr[i:i+block_size]) == block_size
    ]

    features = np.array([
        [entropy_block(b), byte_zero_ratio(b), unique_byte_ratio(b), variance(b)]
        for b in blocks
    ])

    clusters, scores = cluster_blocks(features)
    plot = cluster_plot(features, clusters)
    


    return {
        "num_blocks": len(blocks),
        "clusters": clusters.tolist(),
        "silhouette_score": scores,
        "features": features.tolist(),
        "plot": plot,
        
    }