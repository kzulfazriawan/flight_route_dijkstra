import sys
from src.utilities import load_json_file
from src.services import DijkstraAlgorithm

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python main.py <flights json file>')
        sys.exit(1)

    json_file = sys.argv[1]

    try:
        n, flights, src, dst, k = load_json_file(json_file)
        dijkstra = DijkstraAlgorithm(n, flights,)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    else:
        print(f'Cheapest Price: {dijkstra.priority_queue(src, dst, k)}')
