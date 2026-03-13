from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np

def cluster_blocks(features):
    scaler = StandardScaler()
    model = DBSCAN(eps=0.2, min_samples=3)
    X_scaled = scaler.fit_transform(features)
    clusters = model.fit_predict(X_scaled)
    


    return clusters


