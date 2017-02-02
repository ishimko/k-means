import matplotlib.pyplot as plt
import numpy as np


def display_source(data):
    xs = list(map(lambda x: x[0], data))
    ys = list(map(lambda x: x[1], data))
    plt.scatter(xs, ys)
    plt.show()


def display_result(vectors, clusters):
    colors = [np.random.rand(3, 1) for i in range(len(clusters))]
    for cluster_index, (centroid, cluster) in enumerate(clusters.items()):
        plt.scatter(vectors[centroid][0], vectors[centroid][1], c=colors[cluster_index], marker='x')
        for vector_index in cluster:
            if vector_index != centroid:
                plt.scatter(vectors[vector_index][0], vectors[vector_index][1], c=colors[cluster_index])
    plt.show()
