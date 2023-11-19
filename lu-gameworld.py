'''
    NOTE :
    the grid is using row > column indexing, which is counterintuitive
    this is on purpose, sometimes you have to use systems that you did 
    not write - stick to the coding standard too.

    TODO : what improvements would you make if designers were meant to
    use this?
'''

# globals
GameWorld = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]
Rows = len(GameWorld)
Columns = len(GameWorld[0]) # assumes gameworld a quad

def print_grid():
    for row in GameWorld:
        for columnrow in row:
            print(f"{columnrow}", end=" ")
        print("")

def is_within_distance(seek_object_type : str, i: int, j: int, distance: int) -> bool:
    min_i = max(0,          i - distance)
    max_i = min(Rows,       i + distance)
    min_j = max(0,          j - distance)
    max_j = min(Columns,    j + distance)

    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if GameWorld[i][j] == seek_object_type:
                return True
    
    return False

# TODO : FIX!!
def is_within_eyesight(seek_object_type : str, i: int, j: int):
    t, b = i, i
    while t > 0 and b < Rows:
        t -= 1
        b += 1
        if GameWorld[t][j] != "x" and GameWorld[t][j] != seek_object_type:
            return False

    l, r = j, j
    while t > 0 and b < Rows:
        l -= 1
        r += 1
        if GameWorld[i][l] != "x" and GameWorld[i][r] != seek_object_type:
            return False

    return True

def is_object_valid(object_type: str, i: int, j: int) -> bool:
    if object_type == "p" or object_type == "x" or object_type == "a" or object_type == "o" or object_type == "n":
        return True
    
    if object_type == "e":
        if is_within_distance("a", i, j, 1) and not is_within_distance("o", i, j, 2):
            return True
        
    if object_type == "w":
        if not is_within_distance("o", i, j, 2) and not is_within_eyesight("e", i, j):
            return True

    return False

if (__name__ == "__main__"):
    # [p]layer
    GameWorld[1][1] = "p"
    
    # [o]planet
    GameWorld[2][3] = "o"

    # [a]steroid
    GameWorld[4][4] = "a"
    GameWorld[4][5] = "a"
    GameWorld[5][6] = "a"

    # TODO : populate dynamic objects
    # TODO : look into procedural generation
    GameWorld[5][5] = "e"

    GameWorld[7][5] = "w"

    # check if grid is valid
    for i, object_row in enumerate(GameWorld):
        for j, object_type in enumerate(object_row):
            if not is_object_valid(object_type, i, j):
                print(f"invalid object '{object_type}' with index '{i}:{j}'")

    # output gameworld
    print_grid()