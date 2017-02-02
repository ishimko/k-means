import matplotlib.pyplot as plt
import numpy as np


def display_result(vectors, clusters):
    colors = [np.random.rand(3, 1) for i in range(len(clusters))]
    for cluster_index, (centroid, cluster) in enumerate(clusters.items()):
        current_cluster = [vectors[i] for i in cluster]
        xs = list(map(lambda x: x[0], current_cluster))
        ys = list(map(lambda x: x[1], current_cluster))
        plt.scatter(xs, ys, c=colors[cluster_index])
        plt.scatter(centroid[0], centroid[1], c=colors[cluster_index], marker='x')
    plt.show()
