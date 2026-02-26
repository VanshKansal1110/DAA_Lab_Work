def orientation(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def distance_from_line(a, b, p):
    return abs(orientation(a, b, p))

def find_hull(points, a, b, hull):
    if not points:
        return

    farthest = max(points, key=lambda p: distance_from_line(a, b, p))
    hull.add(farthest)

    left_of_af = [p for p in points if orientation(a, farthest, p) > 0]
    left_of_fb = [p for p in points if orientation(farthest, b, p) > 0]

    # Recurse
    find_hull(left_of_af, a, farthest, hull)
    find_hull(left_of_fb, farthest, b, hull)

def convex_hull(points):
    if len(points) <= 2:
        return points

    min_x = min(points, key=lambda p: p[0])
    max_x = max(points, key=lambda p: p[0])

    hull = set()
    hull.add(min_x)
    hull.add(max_x)

    left_set = [p for p in points if orientation(min_x, max_x, p) > 0]
    right_set = [p for p in points if orientation(min_x, max_x, p) < 0]

    find_hull(left_set, min_x, max_x, hull)
    find_hull(right_set, max_x, min_x, hull)

    return list(hull)

points = [(0, 0), (4, 0), (4, 4), (0, 4), (0, 0), (4, 4)]
hull = convex_hull(points)
print(hull)