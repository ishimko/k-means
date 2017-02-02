from random import randint
from sys import argv


if __name__ == '__main__':
    components_count = int(argv[1])
    max_vectors_count = int(argv[2])
    file_name = argv[3]
    result = set()
    for i in range(max_vectors_count):
        result.add((randint(0, 100) for i in range(components_count)))
    with open(file_name, 'w') as out:
        out.write('{}\n'.format(components_count))
        for item in result:
            out.write('\t'.join((str(x) for x in item)) + '\n')
