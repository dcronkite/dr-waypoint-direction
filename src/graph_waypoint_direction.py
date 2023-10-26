from pathlib import Path

import matplotlib.pyplot as plt


def plot_waypoints_cli(waypoints):
    wp1000 = [(x * 1000, y * 1000) for x, y in waypoints]
    colors = ['red', 'green', 'blue']
    while True:
        index0 = input('Start index > ')
        try:
            index0 = int(index0)
        except Exception as e:
            print(e)
            if index0.strip().lower().startswith('q'):
                break
            continue
        if index0 + 3 >= len(waypoints):
            print(f'Array not big enough, max start index: {len(waypoints) - 4}.')
            continue
        for (x, y), c in zip(wp1000[index0: index0+3], colors):
            plt.scatter(x, y, c=c)
        plt.plot((wp1000[index0][0], wp1000[index0 + 2][0]), (wp1000[index0][1], wp1000[index0 + 2][1]), 'k-')
        plt.title('Red-to-Blue>> 0: Red, 1: Green, 2: Blue')
        plt.show()


def get_waypoints_from_file():
    waypoints = []
    with open(Path(__file__).parent.parent / 'test' / 'waypoints.csv') as fh:
        for i, line in enumerate(fh):
            if i == 0:
                continue
            x, y = line.strip().split(',')
            waypoints.append((float(x), float(y)))
    return waypoints


if __name__ == '__main__':
    plot_waypoints_cli(get_waypoints_from_file())
