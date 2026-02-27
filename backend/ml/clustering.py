from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np

def cluster_blocks(features):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)

    model = DBSCAN(eps=0.3, min_samples=3)
    clusters = model.fit_predict(X_scaled)

    return clusters