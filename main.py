input_map_list = input("Please enter feeding map as a list:")
temp_map_list = []
map_list = []
input_movement_list = input("Please enter direction of movements as a list:")
movement_list = []
movement = 0
item = ""
points = 0
rabbitx = 0
rabbity = 0

input_map_list = input_map_list.replace("'", "").replace("[", "").replace(",", "").replace(" ", "")
for i in input_map_list:
    if i != "]":
        temp_map_list.append(i)
    else:
        map_list.append(temp_map_list)
        temp_map_list = []
map_list.pop()

input_movement_list = input_movement_list.replace("'", "")
input_movement_list = input_movement_list.replace("[", "")
input_movement_list = input_movement_list.replace("]", "")
input_movement_list = input_movement_list.replace(" ", "")
movement_list = input_movement_list.split(",")

print("Your board is:")
for i in range(len(map_list)):
    print("")
    for j in range(len(map_list[i])):
        print(map_list[i][j], end=" ")
        if map_list[i][j] == '*':
            rabbitx = j
            rabbity = i
print(" ")
for i in range(len(movement_list)):
    movement = movement_list[i]
    if movement == 'U':
        if rabbity > 0:
            rabbity = rabbity-1
            item = map_list[rabbity][rabbitx]
            if item == "C":
                points = points+10
                map_list[(rabbity+1)][rabbitx] = "X"
            elif item == "A":
                points = points+5
                map_list[(rabbity+1)][rabbitx] = "X"
            elif item == "M":
                points = points-5
                map_list[(rabbity+1)][rabbitx] = "X"
            elif item == "W":
                rabbity = rabbity+1
            elif item == "X":
                map_list[(rabbity+1)][rabbitx] = "X"
            elif item == "P":
                break
    if movement == 'D':
        if rabbity < (len(map_list)-1):
            rabbity = rabbity+1
            item = map_list[rabbity][rabbitx]
            if item == "C":
                points = points+10
                map_list[(rabbity-1)][rabbitx] = "X"
            elif item == "A":
                points = points+5
                map_list[(rabbity-1)][rabbitx] = "X"
            elif item == "M":
                points = points-5
                map_list[(rabbity-1)][rabbitx] = "X"
            elif item == "W":
                rabbity = rabbity-1
            elif item == "X":
                map_list[(rabbity-1)][rabbitx] = "X"
            elif item == "P":
                break
    if movement == 'L':
        if rabbitx > 0:
            rabbitx = rabbitx-1
            item = map_list[rabbity][rabbitx]
            if item == "C":
                points = points+10
                map_list[rabbity][(rabbitx+1)] = "X"
            elif item == "A":
                points = points+5
                map_list[rabbity][(rabbitx+1)] = "X"
            elif item == "M":
                points = points-5
                map_list[rabbity][(rabbitx+1)] = "X"
            elif item == "W":
                rabbitx = rabbitx+1
            elif item == "X":
                map_list[rabbity][(rabbitx+1)] = "X"
            elif item == "P":
                break
    if movement == 'R':
        if rabbitx < (len((map_list[0]))-1):
            rabbitx = rabbitx+1
            item = map_list[rabbity][rabbitx]
            if item == "C":
                points = points+10
                map_list[rabbity][(rabbitx-1)] = "X"
            elif item == "A":
                points = points+5
                map_list[rabbity][(rabbitx-1)] = "X"
            elif item == "M":
                points = points-5
                map_list[rabbity][(rabbitx-1)] = "X"
            elif item == "W":
                rabbitx = rabbitx-1
            elif item == "X":
                map_list[rabbity][rabbitx-1] = "X"
            elif item == "P":
                break
print("Your output should be like this:")
map_list[rabbity][rabbitx] = '*'
for i in range(len(map_list)):
    print("")
    for j in range(len(map_list[i])):
        print(map_list[i][j], end=" ")
print("")
print("Your score is:", points)
