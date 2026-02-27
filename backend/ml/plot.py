import matplotlib.pyplot as plt
import io
import base64
import numpy as np

def cluster_plot(features, cluster):
    features = np.array(features)
    x = features[:, 0]
    y = features[:, 2]
    plt.figure()
    plt.scatter(x,y,c=cluster)
    plt.xlabel("Entropy")
    plt.ylabel("Variance")
    plt.title("Clusterization of binary Blocks")

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()

    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    return f"data:image/png;base64, {img_base64}"

