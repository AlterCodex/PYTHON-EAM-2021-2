import sys

if __name__ == '__main__':

    variable = 'algo'
    print(f'int {sys.getsizeof(4)} Bytes')

    print(f'string {sys.getsizeof("4")} Bytes')

    print(f'float {sys.getsizeof(5.5)} Bytes')

    print(f'list {sys.getsizeof([])} Bytes')

    print(f'algo {sys.getsizeof(variable)} bytes ')



