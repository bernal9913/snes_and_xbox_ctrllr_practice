import random, readchar, os, pygame
POS_X = 0
POS_Y = 1

MAP_WIDTH = 10
MAP_HEIGHT = 10

NUM_OF_MAP_OBJECTS = 11
map_objects = []
my_position = [3,1]
tail_length = 0
tail = []
died = False
repeat = True
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())



while repeat == True:
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0,MAP_WIDTH), random.randint(0,MAP_HEIGHT)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append([random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)])

    #os.system('clear')
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    for coor_y in range(MAP_HEIGHT):
        
        print("|", end="")
        for coor_x in range(MAP_WIDTH):
            
            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None
            
            for map_object in map_objects:
                if map_object[POS_X] == coor_x and  map_object[POS_Y] == coor_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_place in tail:
                if tail_place[POS_X] == coor_x and tail_place[POS_Y] == coor_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_place

            if my_position[POS_X] == coor_x and  my_position[POS_Y] == coor_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                    #tail.append(object_in_cell)
                
                if tail_in_cell:
                    #print("Te haz muerto pa")
                    #repeat = False
                    died = True

            print(" {} ".format(char_to_draw), end="")
        print("|")
    
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

#end the loop
    if died == True:
        break


#ask user pa donde moverse

#direction = input("A donde nos moveremos padrino? [WASD]: " )
    direction = readchar.readchar()
#print(direction)
    if direction == "w" or pygame.JOYBUTTONDOWN == 11:
        tail.insert(0,my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0,my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        tail.insert(0,my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0,my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    else:
        repeat = False
    os.system('clear')