from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import numpy as np

def cluster_blocks(features):
    scaler = StandardScaler()
    model = DBSCAN(eps=0.05, min_samples=3)
    X_scaled = scaler.fit_transform(features)
    clusters = model.fit_predict(X_scaled)
    
    # Calculate silhouette score only if there are at least 2 clusters and not all points are noise
    unique_clusters = set(clusters)
    if len(unique_clusters) > 1 and -1 not in unique_clusters or len(unique_clusters) > 2:
        # Remove noise points for silhouette calculation
        mask = clusters != -1
        if np.sum(mask) >= 2:  # Need at least 2 points
            score = silhouette_score(X_scaled[mask], clusters[mask])
        else:
            score = None
    else:
        score = None

    return clusters, score


