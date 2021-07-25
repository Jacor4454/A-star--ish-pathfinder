import pygame, random

grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

for i in range (round(0.75*10*10)):
    john = random.randint(0,19)
    karen = random.randint(0,19)
    if john == 19 and karen == 19:
        pass
    elif john == 0 and karen == 0:
        pass
    else:
        grid[john][karen] = 1

pygame.init()
win = pygame.display.set_mode((400,400))
pygame.display.set_caption("Pathfinder")
    

def pathfinder(start, end, r) :
    surround = [[0,1],[1,0],[0,-1],[-1,0]]
    current = [0,0]
    global deadlist
    current[0] = start[0]
    current[1] = start[1]
    step = 0
    test = [0,0]
    hypo = 0
    save = []
    distance = [0 for i in range (10)]
    minimum = 999
    to_print = ""
    save.append(start)
    path = 0
    fail = 0
    remember = 0
    broken = 0
    while path == 0:
        step += 1
        distance = [0,0,0,0]
        for i in range (0,4):
            test[0] = current[0] + surround[i][0]
            test[1] = current[1] + surround[i][1]
            for j in range (0,len(save)):
                if test == save[j]:
                    fail = 1
            for k in range (0,len(deadlist)):
                if test == deadlist[k]:
                    fail = 1
            try:
                if grid[test[1]][test[0]] == 1:
                    fail = 1
            except:
                pass
            if test[0]<0 or test[0]>19 or test[1]<0 or test[1]>19:
                pass
            elif fail == 1:
                pass
            else:
                distance[i] = step
                hypo = ((test[0]-end[0])**2)+((test[1]-end[1])**2)
                distance[i] += hypo
            fail = 0
        minimum = 99999
        remember = 0
        movement = 5
        for i in range (0,4):
            if distance[i] == 0:
                remember += 1
            elif distance[i] < minimum:
                minimum = distance[i]
                movement = i
        if remember == 4 and current == start:
            return save[step-1], -1
        elif remember == 4:
            return save[step-1], 0
        else:
            current[0] = current[0] + surround[movement][0]
            current[1] = current[1] + surround[movement][1]
            pygame.draw.rect(win, (r,r,r), (current[0]*20+1, current[1]*20+1, 19, 19))
            pygame.display.update()
            pygame.time.wait(50)
            save.append([0,0])
            save[step][0] = current[0]
            save[step][1] = current[1]
    
        if current == end:
            path = 1
        
    returned_path = []
    returned_path = [[0 for j in range (0)] for i in range (step+1)]
    for i in range (0, step+1):
        to_print += str(save[i]) + " "
        returned_path[i] = save[i]
    return returned_path, step


def wholefinder(start, end) :
    temp_path = []
    original_path = 0
    global deadlist
    deadlist = []
    incompleteable = 0
    r = 200
    while original_path == 0 and incompleteable == 0:
        path, step = pathfinder(start, end, r)
        r -= 40
        if r < 0:
            r = 200
        if step == 0:
            deadlist.append(path)
        elif step == -1:
            incompleteable = 1
        else:
            original_path = 1
    
    complete = 1
    while complete == 1 and incompleteable == 0:
        complete = 0
        for i in range (step-1, 0, -1):
            if complete == 0:
                new_save = []
                temp_path, temp_step = pathfinder(start, path[i-1], r)
                r -= 40
                if r < 0:
                    r = 200
                if temp_step == 0 or temp_step == -1:
                    pass
                else:
                    x = len(path)-len(temp_path)
                    if len(temp_path) < i :
                        new_save += temp_path
                        for j in range (i, step+1):
                            new_save.append(path[j])
                        path = new_save
                        step = i-x
                        complete = 1
                    else:
                        pass
            else:
                pass
    print(path)
    if path == 0:
        pass
    else:
        for i in range (len(path)):
            pygame.draw.rect(win, (111,185,143), (path[i][0]*20+1, path[i][1]*20+1, 19, 19))
            pygame.display.update()





start = [0,0]
end = [19,19]
win.fill((255,255,255))
for i in range (0, 20):
    for j in range (0,20):
        if grid[j][i] == 1:
            pygame.draw.rect(win, (255,216,0), (i*20, j*20, 20, 20))
        else:
            pygame.draw.rect(win, (44,120,115), (i*20, j*20, 20, 20))
for i in range (0,20):
    pygame.draw.line(win, (0,0,0), (i*20, 0), (i*20, 400))
    pygame.draw.line(win, (0,0,0), (0, i*20), (400, i*20))
pygame.draw.rect(win, (0,0,255), (start[0]*20+1, start[1]*20+1, 19, 19))
pygame.draw.rect(win, (0,0,255), (end[0]*20+1, end[1]*20+1, 19, 19))
pygame.display.update()

wholefinder(start, end)
