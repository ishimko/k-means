from math import sqrt
from random import sample
from collections import defaultdict


def sqr(a):
    return a*a


def distance(a, b):
    if len(a) != len(b):
        raise ValueError('Vectors have different dimensions')
    return sqrt(sum(map(sqr, (x-y for x, y in zip(a, b)))))


def allocate_clusters(vectors, centroids):
    clusters = defaultdict(list)
    for vector_index, vector in enumerate(vectors):
        centroid = min(centroids, key=lambda x: distance(vector, x))
        clusters[centroid].append(vector_index)
    return clusters


def get_centroid(vectors, members_indexes):
    component_count = len(vectors[0])
    result = [None]*component_count
    for component in range(component_count):
        result[component] = sum((vectors[i][component] for i in members_indexes)) / len(members_indexes)
    return tuple(result)


def kmeans(vectors, clusters_count, max_iterations=30):
    clusters = None
    centroids = [vectors[i] for i in sample(range(len(vectors)), clusters_count)]
    for i in range(max_iterations):
        clusters = allocate_clusters(vectors, centroids)
        centroids = set(map(lambda x: get_centroid(vectors, x), clusters.values()))
        old_centroids = set(clusters.keys())
        if old_centroids == centroids:
            break
    return clusters
