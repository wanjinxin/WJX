import math

# 地球半径，单位千米
EARTH_R = 6371


def convert_degrees_to_radians(degrees):
    return degrees * math.pi / 180


def convert_radians_to_degrees(radians):
    return radians * 180 / math.pi


def haver_sin(theta):
    v = math.sin(theta / 2)
    return v * v


"""
用haversine公式计算球面两点间的距离
"""


def calc_distance(lng1, lat1, lng2, lat2):
    lat1 = convert_degrees_to_radians(lat1)
    lng1 = convert_degrees_to_radians(lng1)
    lat2 = convert_degrees_to_radians(lat2)
    lng2 = convert_degrees_to_radians(lng2)

    vlng = math.fabs(lng1 - lng2)
    vlat = math.fabs(lat1 - lat2)

    h = haver_sin(vlat) + math.cos(lat1) * math.cos(lat2) * haver_sin(vlng)
    distance = 2 * EARTH_R * math.asin(math.sqrt(h))
    return distance
