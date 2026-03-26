import pygame
import boundary

def create_map(boundary_list, MAP, block_types, arena):
    match MAP:
        case 'map1':
            image = block_types[0]
            for i in range(16):
                b = boundary.Boundary(50 + 25 * i, 450, image)
                boundary_list.append(b)
            
            for i in range (3):
                b = boundary.Boundary(100 + 25 * i, 375, image)
                boundary_list.append(b)

            for i in range (6):
                b = boundary.Boundary(225 + 25 * i, 375, image)
                boundary_list.append(b)
            
            for i in range (2):
                b = boundary.Boundary(375 + 25 * i, 300, image)
                boundary_list.append(b)

            for i in range (4):
                b = boundary.Boundary(150 + 25 * i, 225, image)
                boundary_list.append(b)
            
            for i in range (2):
                b = boundary.Boundary(275 + 125 * i, 150, image)
                boundary_list.append(b)
            
            if arena == True:
                makeArena(boundary_list, MAP, image)
    
        case 'map2':
            image = block_types[0]
            makeArena(boundary_list, MAP, image)

        case 'map3':
            image = block_types[1]
            for i in range(10):
                b = boundary.Boundary(125 + 25 * i, 450, image)
                boundary_list.append(b)
            for i in range(2):
                b = boundary.Boundary(100, 425 - 25 * i, image)
                boundary_list.append(b)
            for i in range(2):
                b = boundary.Boundary(375, 425 - 25 * i, image)
                boundary_list.append(b)
        

def makeArena(boundary_list, MAP, block_image):
    # ground
    for i in range (20):
        b = boundary.Boundary(25 * i, 475, block_image)
        boundary_list.append(b)    

    # left wall
    for i in range (19):
        b = boundary.Boundary(0, 25 * i, block_image)
        boundary_list.append(b)
    
    # right wall
    for i in range (19):
        b = boundary.Boundary(475, 25 * i, block_image)
        boundary_list.append(b)
    
    # top
    for i in range (18):
        b = boundary.Boundary(25 + 25 * i, 0, block_image)
        boundary_list.append(b)
    return