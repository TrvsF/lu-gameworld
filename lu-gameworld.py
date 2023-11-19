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
Columns = len(GameWorld[0]) # assumes gameworld is a quad

def print_grid():
    for row in GameWorld:
        for columnrow in row:
            print(f"{columnrow}", end=" ")
        print("")

def is_within_distance(seek_object_type : str, i: int, j: int, distance: int) -> bool:
    min_i = max(0,          i - distance)
    max_i = min(Rows,       i + distance + 1)
    min_j = max(0,          j - distance)
    max_j = min(Columns,    j + distance + 1)

    for i in range(min_i, max_i):
        for j in range(min_j, max_j):
            if GameWorld[i][j] == seek_object_type:
                return True
    
    return False

def is_within_eyesight(seek_object_type : str, i: int, j: int):
    top, bottom, left, right = i, i, j, j
    
    # top
    while top > 0:
        top -= 1
        if GameWorld[top][j] == seek_object_type:
            return True
        
        if GameWorld[top][j] != "x" and GameWorld[top][j] != seek_object_type:
            break
    # bottom
    while bottom < Rows - 1:
        bottom += 1
        if GameWorld[bottom][j] == seek_object_type:
            return True
        
        if GameWorld[bottom][j] != "x" and GameWorld[bottom][j] != seek_object_type:
            break
    # left
    while left > 0:
        left -= 1
        if GameWorld[i][left] == seek_object_type:
            return True
        
        if GameWorld[i][left] != "x" and GameWorld[i][left] != seek_object_type:
            break
    # right
    while right < Columns - 1:
        right += 1
        if GameWorld[i][right] == seek_object_type:
            return True
        
        if GameWorld[i][right] != "x" and GameWorld[i][right] != seek_object_type:
            break

    return False

def is_object_valid(object_type: str, i: int, j: int) -> bool:
    if object_type == "p" or object_type == "x" or object_type == "a" or object_type == "o" or object_type == "n":
        return True
    
    if object_type == "e":
        if is_within_distance("a", i, j, 1) and not is_within_distance("o", i, j, 2):
            return True
        
    if object_type == "w":
        if not is_within_distance("o", i, j, 2) and not is_within_eyesight("e", i, j):
            return True
        
    if object_type == "f":
        if not is_within_distance("o", i, j, 2) and not is_within_eyesight("e", i, j):
            return True 

    return False

def populate_static_objects():
    # [p]layer
    GameWorld[0][1] = "p"
    
    # [o]planet
    GameWorld[2][3] = "o"
    GameWorld[4][13] = "o"

    # [n]ebula
    GameWorld[9][9] = "n"

    # [a]steroid
    GameWorld[4][4] = "a"
    GameWorld[4][5] = "a"
    GameWorld[5][6] = "a"

def populate_dynamic_objects():
    # [e]nemy
    GameWorld[5][5] = "e"
    # [w]eapons cache
    GameWorld[9][6] = "w"
    # [f]uel cache 
    GameWorld[1][14] = "f"

if (__name__ == "__main__"):
    populate_static_objects()    

    # TODO : populate dynamic objects base on rules
    # TODO : look into procedural generation ?
    populate_dynamic_objects()

    # check if grid is valid
    for i, object_row in enumerate(GameWorld):
        for j, object_type in enumerate(object_row):
            if not is_object_valid(object_type, i, j):
                print(f"invalid object '{object_type}' with index '{i}:{j}'")

    # output gameworld
    print_grid()