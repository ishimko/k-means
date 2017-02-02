from sys import argv, stderr
from drawer import *
from kmeans import kmeans


def read_vectors(file_name):
    result = None
    with open(file_name, 'r') as f:
        vector_length = int(f.readline())
        vectors = list(map(lambda line: tuple(map(int, line.split())), f.readlines()))
        if all((len(x) == vector_length for x in vectors)):
            result = vectors
    return result


def main():
    vectors = read_vectors(argv[1])
    clusters_count = int(argv[2])
    if vectors:
        clusters = kmeans(vectors, clusters_count=clusters_count)
        if len(vectors[0]) == 2:
            display_source(vectors)
            display_result(vectors, clusters)
    else:
        print('Invalid input', file=stderr)


if __name__ == '__main__':
    main()


