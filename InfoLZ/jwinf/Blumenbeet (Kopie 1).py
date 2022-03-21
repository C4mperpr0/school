from random import randrange as rr

def new_flowerobject(): return {
                                 "1-3":"schwarz",
                          "2-2":"schwarz", "2-4":"schwarz",
                "3-1":"schwarz", "3-3":"schwarz", "3-5":"schwarz",
                          "4-2":"schwarz", "4-4":"schwarz",
                                 "5-3":"schwarz"}.copy()

def flower_exists(flowername):
    if flowername in flowerobject:
        return True
    return False

def get_neighbors(flowername):
    neighbors = []
    flower_indexes = flowername.split("-")
    for x in range(3):
        y = int(flower_indexes[0]) + x - 1
        for i in range(3):
            if y == int(flower_indexes[0]):
                j = int(flower_indexes[1]) + ((i - 1)*2)
            else:
                j = int(flower_indexes[1]) + i - 1
            neighborname = "{}-{}".format(y, j)
            if not flower_exists(neighborname):
                continue
            elif neighborname == flowername:
                continue
            neighbors.append(neighborname)
    return neighbors

def rate_image(flowerobject):
    pass

