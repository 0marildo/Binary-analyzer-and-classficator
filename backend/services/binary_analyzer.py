import numpy as np
from ml.analyzer import analyze_binary

def process_binary_file(data: bytes) -> dict:
    result = analyze_binary(data)

    clusters_list = result["clusters"]
    features = result["features"]

    # Agrupa features por cluster
    cluster_features_map = {}
    for i, cluster_id in enumerate(clusters_list):
        if cluster_id not in cluster_features_map:
            cluster_features_map[cluster_id] = []
        cluster_features_map[cluster_id].append(features[i])

    # Calcula stats médias de cada cluster
    cluster_stats = {}
    for cid, feats in cluster_features_map.items():
        cluster_stats[cid] = {
            "entropy": np.mean([f[0] for f in feats]),
            "zero_ratio": np.mean([f[1] for f in feats]),
            "variance": np.mean([f[3] for f in feats]),
            "count": len(feats)
        }

    # Zeros puros e outliers sempre são offset
    label_map = {}
    for cid, stats in cluster_stats.items():
        if stats["zero_ratio"] > 0.95:
            label_map[cid] = "offset"
    label_map[-1] = "offset"

    # Dos restantes, classifica relativamente
    remaining = {
        cid: s for cid, s in cluster_stats.items()
        if cid not in label_map
    }

    if remaining:
        min_e = min(s["entropy"] for s in remaining.values())
        max_e = max(s["entropy"] for s in remaining.values())
        threshold = min_e + (max_e - min_e) * 0.3

        for cid, stats in remaining.items():
            if stats["entropy"] <= threshold:
                label_map[cid] = "header"
            else:
                label_map[cid] = "raw_data"

    # Monta summary
    summary = {"header": 0, "raw_data": 0, "offset": 0}
    for cluster_id in clusters_list:
        label = label_map.get(cluster_id, "raw_data")
        summary[label] += 1

    print("Cluster → Label map:", label_map)
    print("Summary:", summary)

    return {**result, "summary": summary}