import json
import numpy as np


def get_points_on_vector(initial_pt, terminal_pt, resolution):
    dist = np.linalg.norm(np.array(initial_pt, dtype=float) - np.array(terminal_pt, dtype=float)) / resolution
    res = []
    for i in range(resolution):
        res = res + [get_point_on_vector(initial_pt, terminal_pt, dist * i)]
    assert (len(res) == resolution)
    return res


def get_point_on_vector(initial_pt, terminal_pt, distance):
    v = np.array(initial_pt, dtype=float)
    u = np.array(terminal_pt, dtype=float)
    n = v - u
    n /= np.linalg.norm(n, 2)
    point = v - distance * n
    return point.tolist()


with open("examples/mission-123.json", "r+") as f:
    samples = 10
    mission = json.load(f)
    f.seek(0)
    actualLocation = mission["actualLocation"]["coordinates"]
    res = []
    prev = actualLocation[0]
    for l in actualLocation[1:]:
        if prev != l:
            res += get_points_on_vector(prev, l, samples)
        prev = l
    assert (len(res) <= samples * len(actualLocation))
    mission["actualLocation"]["coordinates"] = res
    json.dump(mission, f, indent=4)