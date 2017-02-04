import matplotlib.pyplot as plt


def display_result(vectors, clusters):
    for cluster_index, (centroid, cluster) in enumerate(clusters.items()):
        current_cluster = [vectors[i] for i in cluster]
        xs = list(map(lambda x: x[0], current_cluster))
        ys = list(map(lambda x: x[1], current_cluster))
        plt.plot(xs, ys, '.')
        plt.plot(centroid[0], centroid[1], marker='x')
    plt.show()
