import matplotlib.pyplot as plt
import numpy as np


def display_result(vectors, clusters):
    colors = [np.random.rand(3, 1) for i in range(len(clusters))]
    for cluster_index, (centroid, cluster) in enumerate(clusters.items()):
        plt.scatter(centroid[0], centroid[1], c=colors[cluster_index], marker='x')
        for vector_index in cluster:
            plt.scatter(vectors[vector_index][0], vectors[vector_index][1], c=colors[cluster_index])
    plt.show()
