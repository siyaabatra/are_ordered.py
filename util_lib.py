# TODO Your solution(s)
def are_ordered(x, y, z):
    return all(x <= y <= z or x >= y >= z for x, y, z in [(x, y, z), (z, y, x)])