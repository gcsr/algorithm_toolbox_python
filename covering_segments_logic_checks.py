from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def get_covered_items_by_point(current_point, start_index, sorted_segments):
    max_covered_segments = 0
    # print(current_point, start_index, sorted_segments[start_index])
    for i in range(start_index, len(sorted_segments)):
        if current_point < sorted_segments[i][0] or current_point > sorted_segments[i][1]:
            break
        max_covered_segments += 1
    # print(max_covered_segments)
    return max_covered_segments

def process_points(start_index, sorted_segments):
    max_covered_segments = 0
    max_covered_point = 0
    for i in range(sorted_segments[start_index][0], sorted_segments[start_index][1] + 1):
        current_covered_items = get_covered_items_by_point(i, start_index, sorted_segments)
        if max_covered_segments < current_covered_items:
            max_covered_segments = current_covered_items
            max_covered_point = i
            print(max_covered_point, max_covered_segments)
    return max_covered_segments, max_covered_point

def optimal_points(segments):
    sorted_segments = sorted(segments)
    print(sorted_segments)
    total_points = []
    looper = 0
    while looper< len(segments):
        max_covered_segments, max_covered_point = process_points(looper, sorted_segments)
        print(max_covered_segments, max_covered_point)
        looper += max_covered_segments
        total_points.append(max_covered_point)
    return total_points


if __name__ == '__main__':
    '''input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))'''
    points = optimal_points([[10,14], [6,9], [6,8], [1,3], [2,5], [2, 6], [4,5]])
    print(len(points))
    print(*points)