from math import sqrt
from random import sample
from collections import defaultdict


def sqr(a):
    return a*a


def distance(a, b):
    if len(a) != len(b):
        raise ValueError('Vectors have different dimensions')
    return sqrt(sum(map(sqr, (x-y for x, y in zip(a, b)))))


def allocate_clusters(vectors, centroids_indexes):
    clusters = defaultdict(list)
    for vector_index, vector in enumerate(vectors):
        centroid_index = min(centroids_indexes, key=lambda i: distance(vector, vectors[i]))
        clusters[centroid_index].append(vector_index)
    return clusters


def get_centroid_index(vectors, members_indexes):
    current_cluster = (vectors[i] for i in members_indexes)
    return min(members_indexes, key=lambda i: sum(map(sqr, (distance(vectors[i], x) for x in current_cluster))))


def kmeans(vectors, clusters_count, centroids_indexes=None, max_iterations=100):
    clusters = None
    if centroids_indexes is None:
        centroids_indexes = sample(range(len(vectors)), clusters_count)
    for i in range(max_iterations):
        clusters = allocate_clusters(vectors, centroids_indexes)
        new_centroids = set(map(lambda x: get_centroid_index(vectors, x), clusters.values()))
        old_centroids = set(clusters.keys())
        if old_centroids == new_centroids:
            break
    return clusters
