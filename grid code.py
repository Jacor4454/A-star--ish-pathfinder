import random, time

#define arrays

grid = [[" " for x in range (16)] for y in range (16)]
hiddenX = [0 for x in range (15)]
hiddenY = [0 for Y in range (15)]
wallX = [0 for x in range (6)]
wallY = [0 for y in range (6)]
ewallX = [0 for x in range (6)]
ewallY = [0 for y in range (6)]
mwallX = [0 for x in range (26)]
mwallY = [0 for y in range (26)]
switchX = [0 for x in range (3)]
switchY = [0 for y in range (3)]
minigrid = [[" " for x in range (3)] for y in range (3)]

#assign all values

level = 1           #set levels here
refresh = "| "
top = ""
death = 0
yn = ""
global toset
toset = 1
gold = 0

#define classes

class move():
    name = ""
    power = 50
    physical = 1
    effector = [0]
    ident = 0

    def raiser(self):
        for i in range (0,len(self.effector)):
            if self.effector[i] == 0:
                pass
            elif self.effector[i] == 1:
                if char.attack_raiser < 5:
                    char.temp_attack -= 5
                    print("your attack decreased")
            elif self.effector[i] == 2:
                if char.defence_raiser < 5:
                    char.temp_defence -= 5
                    print("your defence decreased")
            elif self.effector[i] == 3:
                if char.speed_raiser < 5:
                    char.temp_speed -= 5
                    print("your speed decreased")
            elif self.effector[i] == 4:
                if char.sp_attack_raiser < 5:
                    char.temp_sp_attack -= 5
                    print("your sp_attack decreased")
            elif self.effector[i] == 5:
                if char.sp_defence_raiser < 5:
                    char.temp_sp_defence -= 5
                    print("your sp_defence decreased")
            elif self.effector[i] == 6:
                 if char.attack_raiser > -5:
                    char.temp_attack += 5
                    print("your attack increased")
            elif self.effector[i] == 7:
                if char.defence_raiser > -5:
                    char.temp_defence += 5
                    print("your defence increased")
            elif self.effector[i] == 8:
                if char.speed_raiser > -5:
                    char.temp_speed += 5
                    print("your speed increased")
            elif self.effector[i] == 9:
                if char.sp_attack_raiser > -5:
                    char.temp_sp_attack += 5
                    print("your sp_attack increased")
            elif self.effector[i] == 10:
                if char.sp_defence_raiser > -5:
                    char.temp_sp_defence += 5
                    print("your sp_defence increased")

    def oppraiser(self, level):
        for i in range (0,len(self.effector)):
            if self.effector[i] == 0:
                pass
            elif self.effector[i] == 1:
                if enemy.attack_raiser < 5:
                    enemy.out_attack -= (round((5/10)*level))
                    print("opponents attack decreased")
            elif self.effector[i] == 2:
                if enemy.defence_raiser < 5:
                    enemy.out_defence -= (round((5/10)*level))
                    print("opponents defence decreased")
            elif self.effector[i] == 3:
                if enemy.speed_raiser < 5:
                    enemy.out_speed -= (round((5/10)*level))
                    print("opponents speed decreased")
            elif self.effector[i] == 4:
                if enemy.sp_attack_raiser < 5:
                    enemy.out_sp_attack -= (round((5/10)*level))
                    print("opponents sp_attack decreased")
            elif self.effector[i] == 5:
                if enemy.sp_defence_raiser < 5:
                    enemy.out_sp_defence -= (round((5/10)*level))
                    print("opponents sp_defence decreased")
            elif self.effector[i] == 6:
                 if enemy.attack_raiser > -5:
                    enemy.out_attack += (round((5/10)*level))
                    print("opponents attack increased")
            elif self.effector[i] == 7:
                if enemy.defence_raiser > -5:
                    enemy.out_defence += (round((5/10)*level))
                    print("opponents defence increased")
            elif self.effector[i] == 8:
                if enemy.speed_raiser > -5:
                    enemy.out_speed += (round((5/10)*level))
                    print("opponents speed increased")
            elif self.effector[i] == 9:
                if enemy.sp_attack_raiser > -5:
                    enemy.out_sp_attack += (round((5/10)*level))
                    print("opponents sp_attack increased")
            elif self.effector[i] == 10:
                if enemy.sp_defence_raiser > -5:
                    enemy.out_sp_defence += (round((5/10)*level))
                    print("opponents sp_defence increased")

sword_slash = move()
down_cut = move()
sheild_bash = move()
fortify = move()
sword_slash.name = "sword slash"
down_cut.name = "down cut"
sheild_bash.name = "sheild bash"
fortify.name = "fortify"
down_cut.power = 60
sheild_bash.power = 60
fortify.power = 0
down_cut.effector = [2]
sheild_bash.effector = [1]
fortify.effector = [7]
sword_slash.ident = 1
down_cut.ident = 2
sheild_bash.ident = 3
fortify.ident = 4

class char:
    health = 100
    max_health = 100
    speed = 25
    attack = 50
    defence = 50
    sp_attack = 50
    sp_defence = 50
    speed_raiser = 0
    attack_raiser = 0
    defence_raiser = 0
    sp_attack_raiser = 0
    sp_defence_raiser = 0
    moveset_name = [sword_slash.name,down_cut.name,sheild_bash.name,fortify.name]
    moveset_id = [sword_slash.ident,down_cut.ident,sheild_bash.ident,fortify.ident]

    def attacks(self, choice):
        output = 0
        if char.moveset_id[int(choice)-1] == 1:
            if sword_slash.physical == 1:
                output = self.temp_attack*sword_slash.power
            else:
                output = self.temp_sp_attack*sword_slash.power
        elif char.moveset_id[int(choice)-1] == 2:
            if down_cut.physical == 1:
                output = self.temp_attack*sword_slash.power
            else:
                output = self.temp_sp_attack*sword_slash.power
        elif char.moveset_id[int(choice)-1] == 3:
            if sheild_bash.physical == 1:
                output = self.temp_attack*sword_slash.power
            else:
                output = self.temp_sp_attack*sword_slash.power
        elif char.moveset_id[int(choice)-1] == 4:
            if fortify.physical == 1:
                output = self.temp_attack*sword_slash.power
            else:
                output = self.temp_sp_attack*sword_slash.power

        if char.moveset_id[int(choice)-1] == 1:
            sword_slash.raiser()
        elif char.moveset_id[int(choice)-1] == 2:
            down_cut.raiser()
        elif char.moveset_id[int(choice)-1] == 3:
            sheild_bash.raiser()
        elif char.moveset_id[int(choice)-1] == 4:
            fortify.raiser()

        
        enemy.out_health -= round(output/enemy.out_defence)

class opponent:
    level = 10
    health = 100
    speed = 25
    attack = 50
    defence = 50
    sp_attack = 50
    sp_defence = 50
    speed_raiser = 0
    attack_raiser = 0
    defence_raiser = 0
    sp_attack_raiser = 0
    sp_defence_raiser = 0
    moveset_name = [sword_slash.name,down_cut.name,sheild_bash.name,fortify.name]
    moveset_id = [sword_slash.ident,down_cut.ident,sheild_bash.ident,fortify.ident]

    def oppattacks(self):
        output = 0
        choice = random.randint(1,4)
        if enemy.moveset_id[int(choice)-1] == 1:
            if sword_slash.physical == 1:
                output = self.out_attack*sword_slash.power
            else:
                output = self.out_sp_attack*sword_slash.power
        elif enemy.moveset_id[int(choice)-1] == 2:
            if down_cut.physical == 1:
                output = self.out_attack*sword_slash.power
            else:
                output = self.out_sp_attack*sword_slash.power
        elif enemy.moveset_id[int(choice)-1] == 3:
            if sheild_bash.physical == 1:
                output = self.out_attack*sword_slash.power
            else:
                output = self.out_sp_attack*sword_slash.power
        elif enemy.moveset_id[int(choice)-1] == 4:
            if fortify.physical == 1:
                output = self.out_attack*sword_slash.power
            else:
                output = self.out_sp_attack*sword_slash.power

        if enemy.moveset_id[int(choice)-1] == 1:
            sword_slash.oppraiser(self.level)
        elif enemy.moveset_id[int(choice)-1] == 2:
            down_cut.oppraiser(self.level)
        elif enemy.moveset_id[int(choice)-1] == 3:
            sheild_bash.oppraiser(self.level)
        elif enemy.moveset_id[int(choice)-1] == 4:
            fortify.oppraiser(self.level)

        char.health -= round(output/char.temp_defence)


char = char()
enemy = opponent()


#define subroutines

def battle():
    global health
    global out_health
    global win
    char.temp_speed = char.speed
    char.temp_attack = char.attack
    char.temp_defence = char.defence
    char.temp_sp_attack = char.sp_attack
    char.temp_sp_defence = char.sp_defence
    char.speed_raiser = 0
    char.attack_raiser = 0
    char.defence_raiser = 0
    char.sp_attack_raiser = 0
    char.sp_defence_raiser = 0
    enemy.level = 10
    enemy.out_health = round(enemy.health*(enemy.level/10))
    enemy.out_speed = round(enemy.speed*(enemy.level/10))
    enemy.out_attack = round(enemy.attack*(enemy.level/10))
    enemy.out_defence = round(enemy.defence*(enemy.level/10))
    enemy.out_sp_attack = round(enemy.sp_attack*(enemy.level/10))
    enemy.out_sp_defence = round(enemy.sp_defence*(enemy.level/10))
    
    battle = 1
    death = 0
    win = 0
    while battle == 1:
        print("your health: "+str(char.health))
        print("opponent health: "+str(enemy.out_health))
        print("chose your attack:")
        for i in range (0,4):
            print(str(i+1) + ". " + char.moveset_name[i])
        choice = input()
        if char.temp_speed >= enemy.out_speed:
            char.attacks(choice)
            if enemy.out_health <= 0:
                win = 1
                battle = 0
            enemy.oppattacks()
            if char.health <= 0:
                battle = 0
                win = 0
        else:
            enemy.oppattacks()
            if char.health <= 0:
                battle = 0
                win = 0
            char.attacks(choice)
            if enemy.out_health <= 0:
                battle = 0
                win = 1

def pathfinder(start, end) :
    surround = [[0,1],[1,0],[0,-1],[-1,0]]
    current = [0,0]
    current[0] = start[0]
    current[1] = start[1]
    step = 0
    test = [0,0]
    hypo = 0
    save = [[0 for i in range (0)] for i in range (0, 100)]
    distance = [0 for i in range (10)]
    minimum = 999
    to_print = ""
    save[0] = start
    path = 0
    fail = 0
    while path == 0:
        step += 1
        distance = [0,0,0,0,0,0,0,0]
        for i in range (0,4):
            test[0] = current[0] + surround[i][0]
            test[1] = current[1] + surround[i][1]
            for j in range (0,step):
                if test == save[j]:
                    fail = 1
            for k in range (6):
                if test[0] == wallX[k] and test[1] == wallY[k]:
                    fail = 1
            if ewall == 1:
                for k in range (6):
                    if test[0] == wallX[k] and test[1] == wallY[k]:
                        fail = 1
            if mwall == 1:
                for k in range (26):
                    if test[0] == wallX[k] and test[1] == wallY[k]:
                        fail = 1
            if grid[test[1]][test[0]] == 1:
                fail = 1
            if test[0] >= alterationX :
                actualX = gridX + extention
            if test[0] >= gridX:
                base = alterationX
            if test[0]<0 or test[0]>actualX or test[1]<0 or test[1]>gridY:
                pass
            elif fail == 1:
                pass
            else:
                distance[i] = step
                hypo = ((test[0]-end[0])**2)+((test[1]-end[1])**2)
                distance[i] += hypo
            actualX = gridX
            fail = 0
        minimum = 999
        for i in range (0,4):
            if distance[i] == 0:
                pass
            elif distance[i] < minimum:
                minimum = distance[i]
                movement = i
        current[0] = current[0] + surround[movement][0]
        current[1] = current[1] + surround[movement][1]
        save[step] += current
    
        if current == end:
            path = 1
    returned_path = []
    returned_path = [[0 for j in range (0)] for i in range (step+1)]
    for i in range (0, step+1):
        to_print += str(save[i]) + " "
        returned_path[i] = save[i]
    return returned_path, step

def astarpathfinder(start, end):
    temp_path = []
    new_save = [[0 for i in range (0)] for j in range (100)]
    path, step = pathfinder(start, end)
    complete = 1
    while complete == 1:
        complete = 0
        for i in range (step-1, 0, -1):
            if complete == 0:
                new_save = [[0 for i in range (0)] for j in range (i)]
                temp_path, temp_step = pathfinder(start, path[i])
                x = len(path)-len(temp_path)
                if len(temp_path) < i :
                    for j in range (0, len(temp_path)):
                        new_save[j] = temp_path[j]
                    for j in range (i+1, step+1):
                        new_save[j-x] = path[j]
                    path = [[0 for k in range (0)] for j in range (0, i-x+1)]
                    for j in range (0, temp_step):
                        path[j] = new_save[j]
                    step = i-x+1
                    complete = 1
                else:
                    pass
            else:
                pass
    print(path)
    return path[1]

def died() :
    global death
    for x in range(40):
        print("")
    print("you were killed")
    print("you lose")
    print("you lasted " + str(turn) + " turns")
    print("you got to level " + str(level))
    print("you got " + str(gold) + " pieces of gold")
    print("would you like to resume from last save or quit?")
    responcec = 0
    while responcec != 1:
        print("y/n")
        yn = input()
        if yn == "y" :
            read_data()
            responcec = 1
        elif  yn == "n":
            death = 1
            responcec = 1

def read_data():
    global flicker
    global toset
    global level
    global cursorX
    global cursorY
    global badguyX
    global badguyY
    global triggered
    global jitter
    global gold
    global turn
    global switch
    toset = 0
    try:
        save_load = open("saved_data","r")

        rotomdex = 0
        readindex = int(save_load.read(1))
        while rotomdex == 0:
            if readindex%9 == 0:
                readindex += int(save_load.read(1))
            else:
                rotomdex = 1
        level = binary_to_deinary(save_load.read(readindex))

        rotomdex = 0
        readindex = int(save_load.read(1))
        while rotomdex == 0:
            if readindex%9 == 0:
                readindex += int(save_load.read(1))
            else:
                rotomdex = 1
        cursorX = binary_to_deinary(save_load.read(readindex))

        rotomdex = 0
        readindex = int(save_load.read(1))
        while rotomdex == 0:
            if readindex%9 == 0:
                readindex += int(save_load.read(1))
            else:
                rotomdex = 1
        cursorY = binary_to_deinary(save_load.read(readindex))

        rotomdex = 0
        readindex = int(save_load.read(1))
        while rotomdex == 0:
            if readindex%9 == 0:
                readindex += int(save_load.read(1))
            else:
                rotomdex = 1
        badguyX = binary_to_deinary(save_load.read(readindex))

        rotomdex = 0
        readindex = int(save_load.read(1))
        while rotomdex == 0:
            if readindex%9 == 0:
                readindex += int(save_load.read(1))
            else:
                rotomdex = 1
        badguyY = binary_to_deinary(save_load.read(readindex))

        rotomdex = 0
        readindex = int(save_load.read(1))
        while rotomdex == 0:
            if readindex%9 == 0:
                readindex += int(save_load.read(1))
            else:
                rotomdex = 1
        gold = binary_to_deinary(save_load.read(readindex))

        rotomdex = 0
        readindex = int(save_load.read(1))
        while rotomdex == 0:
            if readindex%9 == 0:
                readindex += int(save_load.read(1))
            else:
                rotomdex = 1
        turn = binary_to_deinary(save_load.read(readindex))

        rotomdex = 0
        readindex = int(save_load.read(1))
        while rotomdex == 0:
            if readindex%9 == 0:
                readindex += int(save_load.read(1))
            else:
                rotomdex = 1
        gateXC = binary_to_deinary(save_load.read(readindex))

        rotomdex = 0
        readindex = int(save_load.read(1))
        while rotomdex == 0:
            if readindex%9 == 0:
                readindex += int(save_load.read(1))
            else:
                rotomdex = 1
        gateYC = binary_to_deinary(save_load.read(readindex))
        
        triggered = int(save_load.read(1))
        jitter = int(save_load.read(1))
        
    except:
        level = 1
        flicker = 1
        toset = 1

def deinary_to_binary(deinary):
    binary = ""
    found = 0
    while found == 0:
        binary += str(round(deinary%2))
        deinary = ((deinary- (deinary%2))/2)
        if deinary == 0:
            found = 1

    return binary

def binary_to_deinary(binary):
    power = 0
    deinary = 0
    for i in range (0, len(binary)):
        deinary += (int(binary[i])*(2**power))
        power += 1
    return deinary

def save_data():
    templevel = len(deinary_to_binary(level))
    tempcursorX = len(deinary_to_binary(cursorX))
    tempcursorY = len(deinary_to_binary(cursorY))
    tempbadguyX = len(deinary_to_binary(badguyX))
    tempbadguyY = len(deinary_to_binary(badguyY))
    tempgold = len(deinary_to_binary(gold))
    tempturn = len(deinary_to_binary(turn))
    tempgateXC = len(deinary_to_binary(gateXC))
    tempgateYC = len(deinary_to_binary(gateYC))
    save_load = open("saved_data","w")
    
    while len(str(templevel)) > 9:
        save_load.writelines(str(9))
        templevel -= 9
    save_load.writelines(str(templevel))
    save_load.writelines(deinary_to_binary(level))

    while len(str(tempcursorX)) > 9:
        save_load.writelines(str(9))
        templevel -= 9
    save_load.writelines(str(tempcursorX))
    save_load.writelines(deinary_to_binary(cursorX))
    
    while len(str(tempcursorY)) > 9:
        save_load.writelines(str(9))
        templevel -= 9
    save_load.writelines(str(tempcursorY))
    save_load.writelines(deinary_to_binary(cursorY))
    
    while len(str(tempbadguyX)) > 9:
        save_load.writelines(str(9))
        templevel -= 9
    save_load.writelines(str(tempbadguyX))
    save_load.writelines(deinary_to_binary(badguyX))
    
    while len(str(tempbadguyY)) > 9:
        save_load.writelines(str(9))
        templevel -= 9
    save_load.writelines(str(tempbadguyY))
    save_load.writelines(deinary_to_binary(badguyY))
    
    while len(str(tempgold)) > 9:
        save_load.writelines(str(9))
        templevel -= 9
    save_load.writelines(str(tempgold))
    save_load.writelines(deinary_to_binary(gold))
    
    while len(str(tempturn)) > 9:
        save_load.writelines(str(9))
        templevel -= 9
    save_load.writelines(str(tempturn))
    save_load.writelines(deinary_to_binary(turn))

    while len(str(tempgateXC)) > 9:
        save_load.writelines(str(9))
        templevel -= 9
    save_load.writelines(str(tempgateXC))
    save_load.writelines(deinary_to_binary(gateXC))

    while len(str(tempgateYC)) > 9:
        save_load.writelines(str(9))
        templevel -= 9
    save_load.writelines(str(tempgateYC))
    save_load.writelines(deinary_to_binary(gateYC))


    
    save_load.write(str(triggered))
    save_load.write(str(jitter))

    
#main program starts here

flicker = 1
responcec = 0

try:
    save_load = open("saved_data","r")
except:
    print("no saves have been found")
    print("starting new game")
else:
    print("a save has been found")
    print("would you like to resume a game?")
    while responcec != 1:
        print("y/n")
        yn = input()
        if yn == "y" :
            read_data()
            responcec = 1
        elif  yn == "n":
            save_load = open("saved_data","w")
            toset = 1
            level = 1
            responcec = 1
        

while death != 1 :
    if level == 1:
        if flicker == 1:
            if toset == 1:
                cursorX = 0
                cursorY = 0
                badguyX = 3
                badguyY = 7
                gateCX = 6
                gateCX = 6
                jitter = 1
                triggered = 0
                gold = 0
            gridX = 8
            gridY = 8
            alterationX = 0
            extention = 0
            actualX = gridX
            base = 0
            exitX = 8
            exitY = 5
            exitdX = 1
            turn = 0
            ticker = 0
            flicker = 1
            oldcursorX = 0
            oldcursorY = 0
            oldbadguyX = badguyX
            oldbadguyY = badguyY
            textbar = 1
            goldbar = 0
            switch = 0
            noswitch = 0
            switchX[1] = 1
            switchY[1] = 0
            gateX1 = 1
            gateX2 = 1
            gateY1 = 2
            gateY2 = 3
            gateXC = gateX1
            gateYC = gateY1
            nohidden = 4
            for x in range (nohidden):
                hiddenX[x] = random.randint(2,7)
            for y in range (nohidden):
                hiddenY[y] = random.randint(2,7)
            ewall = 0
            mwall = 0
            wallX = [5,5,4,3,2,1]
            wallY = [6,3,4,5,6,7]
            treasureX = 0
            treasureY = 7
            pathfinderX = 0
            pathfinderY = 0
            flicker = 0
            toset = 1
            
    elif level == 2:
        if flicker == 1:
            if toset == 1:
                cursorX = 0
                cursorY = 0
                badguyX = 3
                badguyY = 6
                switch = 0
                jitter = 1
                triggered = 0
            gridX = 7
            gridY = 9
            exitX = 7
            exitY = 6
            treasureX = 0
            treasureY = 8
            nohidden = 5
            for x in range (nohidden):
                hiddenX[x] = random.randint(2,gridX-1)
            for y in range (nohidden):
                hiddenY[y] = random.randint(2,gridY-1)
            wallX = [5,5,4,3,2,1]
            wallY = [4,4,4,4,4,4]
            flicker = 0
            toset = 1
    elif level == 3:
        if flicker == 1:
            if toset == 1:
                cursorX = 0
                cursorY = 2
                badguyX = 7
                badguyY = 2
                switch = 0
                jitter = 1
                triggered = 0
            gridX = 10
            gridY = 5
            exitX = 10
            exitY = 2
            treasureX = 9
            treasureY = 4
            nohidden = 4
            for x in range (nohidden-1):
                hiddenX[x] = random.randint(2,gridX-1)
            for y in range (nohidden-1):
                hiddenY[y] = random.randint(2,gridY-1)
            hiddenX[4] = 1
            hiddenY[4] = 4
            wallX = [6,6,4,2,2,0]
            wallY = [1,3,2,1,3,4]
            flicker = 0
            toset = 1
    elif level == 4:
        if flicker == 1:
            if toset == 1:
                cursorX = 0
                cursorY = 0
                badguyX = 4
                badguyY = 4
                switch = 0
                jitter = 1
                triggered = 0
            gridX = 5
            gridY = 5
            exitX = 5
            exitY = 2
            treasureX = 3
            treasureY = 4
            nohidden = 3
            for x in range (nohidden):
                hiddenX[x] = random.randint(2,gridX-1)
            for y in range (nohidden):
                hiddenY[y] = random.randint(2,gridY-1)
            wallX = [3,1,0,1,2,3]
            wallY = [0,1,2,3,4,2]
            flicker = 0
            toset = 1
    elif level == 5:
        if flicker == 1:
            if toset == 1:
                cursorX = 0
                cursorY = 4
                badguyX = 4
                badguyY = 4
                switch = 0
                jitter = 1
                triggered = 0
            gridX = 5
            gridY = 5
            exitX = 5
            exitY = 2
            treasureX = 2
            treasureY = 1
            nohidden = 5
            for x in range (nohidden):
                hiddenX[x] = 6
            for y in range (nohidden):
                hiddenY[y] = 6
            wallX = [2,1,0,3,3,4]
            wallY = [0,3,3,3,4,3]
            flicker = 0
            toset = 1
    elif level == 6:
        if flicker == 1:
            if toset == 1:
                cursorX = 0
                cursorY = 0
                badguyX = 9
                badguyY = 5
                switch = 0
                jitter = 1
                triggered = 0
            gridX = 5
            gridY = 9
            alterationX = 5
            extention = 5
            actualX = gridX
            base = 0
            exitX = 10
            exitY = 8
            exitdX = 1
            treasureX = 9
            treasureY = 6
            nohidden = 5
            for x in range (nohidden):
                hiddenX[x] = random.randint(2, gridX-1)
            for y in range (nohidden):
                hiddenY[y] = random.randint(2, gridY-1)
            wallX = [9,8,7,6,5,4]
            wallY = [7,7,7,7,7,7]
            flicker = 0
            toset = 1
    elif level == 7:
        if flicker == 1:
            if toset == 1:
                cursorX = 0
                cursorY = 0
                badguyX = 9
                badguyY = 5
                switch = 0
                jitter = 1
                triggered = 0
            gridX = 1
            gridY = 9
            alterationX = 8
            extention = 7
            actualX = gridX
            base = 0
            exitX = 8
            exitY = 8
            exitdX = 1
            treasureX = 9
            treasureY = 6
            nohidden =  1
            for x in range (nohidden):
                hiddenX[x] = 6
            for y in range (nohidden):
                hiddenY[y] = 0
            wallX = [9,8,7,6,5,4]
            wallY = [7,7,7,7,7,7]
            flicker = 0
            toset = 1
    elif level == 8:
        if flicker == 1:
            if toset == 1:
                cursorX = 1
                cursorY = 0
                badguyX = 5
                badguyY = 8
                switch = 0
                jitter = 1
                triggered = 0
            ewall = 1
            gridX = 3
            gridY = 9
            alterationX = 3
            extention = 5
            actualX = gridX
            base = 0
            exitX = 8
            exitY = 8
            exitdX = 1
            treasureX = 9
            treasureY = 6
            nohidden = 5
            for x in range (nohidden):
                hiddenX[x] = random.randint(2, gridX-1)
            for y in range (nohidden):
                hiddenY[y] = random.randint(2, gridY-1)
            wallX = [0,2,1,3,5,7]
            wallY = [2,2,4,4,4,4]
            ewallX = [0,2,4,6,1,3]
            ewallY = [6,6,6,6,8,8]
            flicker = 0
            toset = 1
    elif level == 9:
        if flicker == 1:
            if toset == 1:
                cursorX = 0
                cursorY = 5
                badguyX = 9
                badguyY = 5
                switch = 0
                jitter = 1
                triggered = 0
            mwall = 1
            ewall = 1
            gridX = 11
            gridY = 11
            alterationX = 0
            extention = 0
            actualX = gridX
            base = 0
            exitX = 11
            exitY = 5
            exitdX = 1
            treasureX = 10
            treasureY = 10
            nohidden = 1
            for x in range (nohidden):
                hiddenX[x] = 1
            for y in range (nohidden):
                hiddenY[y] = 5
            wallX = [0,1,2,0,1,2]
            wallY = [4,4,4,6,6,6]
            ewallX = [8,9,10,8,9,10]
            ewallY = [4,4,4,6,6,6]
            mwallX = [5,5,5,5,5,5,5,5,5,4,4,6,6,2,3,4,10,6,7,8,2,3,4,8,6,7]
            mwallY = [1,2,3,4,5,6,7,8,9,4,6,4,6,2,2,2,0,2,2,2,8,8,8,8,8,8]
            flicker = 0
            toset = 1
    elif level == 10:
        if flicker == 1:
            if toset == 1:
                cursorX = 0
                cursorY = 0
                badguyX = 6
                badguyY = 0
                switch = 1
                jitter = 1
                triggered = 0
            ewall = 1
            mwall = 0
            gridX = 7
            gridY = 7
            alterationX = 0
            extention = 0
            actualX = gridX
            base = 0
            exitX = 7
            exitY = 4
            exitdX = 1
            treasureX = 0
            treasureY = 6
            noswitch = 1
            switchX1 = 2
            switchY1 = 0
            gateX1 = 1
            gateX2 = 5
            gateY1 = 2
            gateY2 = 2
            gateXC = gateX1
            gateYC = gateY1
            nohidden = 5
            for x in range (nohidden):
                hiddenX[x] = random.randint(2, gridX-1)
            for y in range (nohidden):
                hiddenY[y] = random.randint(2, gridY-1)
            wallX = [3,3,3,0,2,4]
            wallY = [0,1,2,2,2,2]
            ewallX = [6,0,1,2,3,1]
            ewallY = [2,4,4,4,5,6]
            flicker = 0
            toset = 1
    elif level == 11:
        if flicker == 1:
            if toset == 1:
                cursorX = 2
                cursorY = 0
                badguyX = 2
                badguyY = 6
                switch = 1
                jitter = 1
                triggered = 0
            ewall = 1
            mwall = 0
            gridX = 5
            gridY = 7
            alterationX = 0
            extention = 0
            actualX = gridX
            base = 0
            exitX = 5
            exitY = 6
            exitdX = 1
            treasureX = 0
            treasureY = 3
            noswitch = 1
            switchX1 = 4
            switchY1 = 3
            gateX1 = 2
            gateX2 = 2
            gateY1 = 5
            gateY2 = 1
            gateXC = gateX1
            gateYC = gateY1
            nohidden = 1
            for x in range (nohidden):
                hiddenX[x] = 2
            for y in range (nohidden):
                hiddenY[y] = 2
            wallX = [0,1,3,4,1,3]
            wallY = [1,1,1,1,3,3]
            ewallX = [0,1,3,4,0,1]
            ewallY = [5,5,5,5,6,6]
            flicker = 0
            toset = 1
    elif level == 12:
        if flicker == 1:
            if toset == 1:
                cursorX = 2
                cursorY = 0
                badguyX = 2
                badguyY = 6
                switch = 1
                jitter = 1
                triggered = 0
                gold = 0
            ewall = 1
            mwall = 0
            gridX = 5
            gridY = 7
            alterationX = 0
            extention = 0
            actualX = gridX
            base = 0
            exitX = 5
            exitY = 6
            exitdX = 1
            treasureX = 0
            treasureY = 3
            noswitch = 2
            switchX1 = 4
            switchY1 = 0
            switchX2 = 4
            switchY2 = 3
            gateX1 = 2
            gateX2 = 2
            gateY1 = 1
            gateY2 = 5
            gateXC = gateX1
            gateYC = gateY1
            nohidden = 1
            for x in range (nohidden):
                hiddenX[x] = 2
            for y in range (nohidden):
                hiddenY[y] = 2
            wallX = [0,1,3,4,1,3]
            wallY = [1,1,1,1,3,3]
            ewallX = [0,1,3,4,0,1]
            ewallY = [5,5,5,5,6,6]
            flicker = 0
            toset = 1
    elif level == 13:
        if flicker == 1:
            if toset == 1:
                cursorX = 2
                cursorY = 0
                badguyX = 3
                badguyY = 9
                switch = 1
                jitter = 1
                triggered = 0
                gold = 0
            ewall = 0
            mwall = 1
            gridX = 5
            gridY = 10
            alterationX = 5
            extention = 5
            actualX = gridX
            base = 0
            exitX = 10
            exitY = 7
            exitdX = 1
            treasureX = 1
            treasureY = 9
            noswitch = 2
            switchX1 = 0
            switchY1 = 5
            switchX2 = 3
            switchY2 = 7
            gateX1 = 3
            gateX2 = 4
            gateY1 = 6
            gateY2 = 7
            gateXC = gateX1
            gateYC = gateY1
            nohidden = 15
            for x in range (nohidden):
                hiddenX[x] = random.randint(2,gridX-1)
            for y in range (nohidden):
                hiddenY[y] = random.randint(2,gridY-1)
            wallX = [7,7,7,7,7,7]
            wallY = [1,1,1,1,1,1]
            mwallX = [0,4,1,3,0,2,4,4,5,8,0,1,2,4,9,6,7,1,2,3,4,9,4,5,8,7]
            mwallY = [0,0,2,2,4,4,4,5,5,5,6,6,6,6,6,7,7,8,8,8,8,8,9,9,9,1]
            flicker = 0
            toset = 1
    elif level == 14:
        if flicker == 1:
            if toset == 1:
                cursorX = 4
                cursorY = 14
                badguyX = 4
                badguyY = 1
                switch = 1
                jitter = 1
                triggered = 0
                gold = 0
            ewall = 0
            mwall = 1
            gridX = 9
            gridY = 15
            alterationX = 0
            extention = 0
            actualX = gridX
            base = 0
            exitX = 9
            exitY = 1
            exitdX = 1
            treasureX = 0
            treasureY = 0
            noswitch = 1
            switchX1 = 6
            switchY1 = 0
            gateX1 = 2
            gateX2 = 14
            gateY1 = 0
            gateY2 = 0
            gateXC = gateX1
            gateYC = gateY1
            nohidden = 0
            for x in range (nohidden):
                hiddenX[x] = 2
            for y in range (nohidden):
                hiddenY[y] = 2
            wallX = [6,7,2,6,1,7]
            wallY = [11,11,13,13,14,14]
            mwallX = [4,0,1,2,1,2,6,7,1,2,6,7,1,2,6,7,1,2,6,7,1,2,6,7,1,2]
            mwallY = [0,1,1,1,4,4,4,4,5,5,5,5,7,7,7,7,8,8,8,8,10,10,10,10,11,11]
            flicker = 0
            toset = 1
    elif level == 15:       #add the final level here
        if flicker == 1:
            if toset == 1:
                cursorX = 2
                cursorY = 0
                badguyX = 2
                badguyY = 6
                switch = 1
                jitter = 1
                triggered = 0
                gold = 0
            ewall = 1
            mwall = 0
            gridX = 5
            gridY = 7
            alterationX = 0
            extention = 0
            actualX = gridX
            base = 0
            exitX = 5
            exitY = 6
            exitdX = 1
            treasureX = 0
            treasureY = 3
            noswitch = 2
            switchX1 = 4
            switchY1 = 0
            switchX2 = 4
            switchY2 = 3
            gateX1 = 2
            gateX2 = 2
            gateY1 = 1
            gateY2 = 5
            gateXC = gateX1
            gateYC = gateY1
            nohidden = 1
            for x in range (nohidden):
                hiddenX[x] = 2
            for y in range (nohidden):
                hiddenY[y] = 2
            wallX = [0,1,3,4,1,3]
            wallY = [1,1,1,1,3,3]
            ewallX = [0,1,3,4,0,1]
            ewallY = [5,5,5,5,6,6]
            flicker = 0
            toset = 1
    elif level == 16:
        winner = 1
        print(" --- --- --- --- --- --- --- ")
        print("|   |   | Y | O | U |   |   |")
        print(" --- --- --- --- --- --- --- ")
        print("|   |   | A | R | E |   |   |")
        print(" --- --- --- --- --- --- --- ")
        print("|   |   | T | H | E |   |   |")
        print(" --- --- --- --- --- --- --- ")
        print("| W | I | N | N | E | R | ! |")
        print(" --- --- --- --- --- --- --- ")
        time.sleep(5)
        win()
        death = 1
            
    for x in range (gridX + extention):
        for y in range (gridY):
            grid[x][y] = " "
    
    grid[badguyX][badguyY] = "K"
    
    if switch == 1:
        grid[gateXC][gateYC] = "G"
        if noswitch == 1:
            grid[switchX1][switchY1] = "S"
        elif noswitch == 2:
            grid[switchX1][switchY1] = "S"
            grid[switchX2][switchY2] = "S"

    grid[switchX[0]][switchY[0]] = " "
    
    if jitter == 1 :
        grid[treasureX][treasureY] = "T"
    oldcursorX = cursorX
    oldcursorY = cursorY
    oldbadguyX = badguyX
    oldbadguyY = badguyY
    pathfinderX = badguyX
    pathfinderY = badguyY

    for i in range (6):
        grid[wallX[i]][wallY[i]] = "W"

    if ewall == 1:
        for i in range (6):
            grid[ewallX[i]][ewallY[i]] = "W"

    if mwall == 1:
        for i in range (26):
            grid[mwallX[i]][mwallY[i]] = "W"

    grid[cursorX][cursorY] = "I"

    for i in range (nohidden):
        if cursorX == hiddenX[i] and cursorY == hiddenY[i] :
                grid[cursorX][cursorY] = "O"
    
    for y in range (gridY):
        process = y
        if process >= alterationX and process < gridY :
            actualX = gridX + extention
        top = ""
        if process == exitY or process == (exitY+1):
            top = " ---"
        for x in range (actualX):
            top = top + " ---"
            refresh = refresh + grid[x][y]
            refresh = refresh + " | "
        print(top)
        print(refresh)
        refresh = "| "
        actualX = gridX

    if exitY == (gridY-2):
        top = ""
        if process >= alterationX and process < gridY :
            actualX = gridX + extention
        for i in range (actualX):
            top = top + " ---"
    
    print(top)
    
    textbar = 1
    
    for i in range (nohidden):
        if cursorX == hiddenX[i] and cursorY == hiddenY[i] :
            triggered = 1
            textbar = 0
            print("you triggered a trap")

    if goldbar == 1 :
        print("you got some gold")
        textbar = 0
        goldbar = 0
    
    if textbar == 1:
        print("")
        
    controle = input()
    turn = turn + 1
    if cursorY >= alterationX :
        actualX = gridX + extention
    if cursorX >= gridX:
        base = alterationX
    if controle == "d" :
        if exitdX == 1 and cursorY == exitY and cursorX == (exitX-1):
            level = level + 1
            flicker = 1
            cursorX = cursorX + 1
        elif cursorX != (actualX-1) :
            cursorX = cursorX + 1
    elif controle == "a" :
        if cursorX != 0 :
            cursorX = cursorX - 1
    elif controle == "w" :
        if cursorY != base :
            cursorY = cursorY - 1
    elif controle == "s" :
        if exitdX == 0 and cursorY == exitY and cursorX == (exitX-1):
            level = level + 1
        elif cursorY != (gridY-1) :
            cursorY = cursorY + 1
    elif controle == "save" :
        print("you saved the game")
        save_data()
        textbar = 0
    actualX = gridX
    base = 0

    oldbadguyX = badguyX
    oldbadguyY = badguyY

    try:
        if triggered == 1:
            newbadguy = astarpathfinder([badguyX,badguyY], [cursorX,cursorY])
            badguyX = newbadguy[0]
            badguyY = newbadguy[1]
    except:
        if badguyY >= alterationX :
            actualX = gridX + extention
        if badguyX >= gridX:
            base = alterationX
        if triggered == 1:
            differenceX = abs(cursorX - badguyX)
            differenceY = abs(cursorY - badguyY)
            if differenceX > differenceY :
                ticker = 0
            elif differenceY > differenceX :
                ticker = 1
            elif badguyX == (actualX):
                ticker = 1
            elif badguyY == base:
                ticker = 0
            if ticker == 0  and badguyX != (actualX):
                if badguyX < cursorX :
                    badguyX = badguyX + 1
                elif badguyX > cursorX :
                    badguyX = badguyX - 1
            elif ticker == 1 and badguyY != base :
                if badguyY < cursorY :
                    badguyY = badguyY + 1
                elif badguyY > cursorY :
                    badguyY = badguyY - 1
            
        actualX = gridX
        base = 0

    if switch == 1:
        if noswitch == 1 :
            if cursorX == switchX1 and cursorY == switchY1:
                if gateXC == gateX1 and gateYC == gateY1:
                    gateXC = gateX2
                    gateYC = gateY2
                else:
                    gateXC = gateX1
                    gateYC = gateY1
        elif noswitch == 2 :
            if cursorX == switchX1 and cursorY == switchY1:
                if gateXC == gateX1 and gateYC == gateY1:
                    gateXC = gateX2
                    gateYC = gateY2
                else:
                    gateXC = gateX1
                    gateYC = gateY1
            elif cursorX == switchX2 and cursorY == switchY2:
                if gateXC == gateX1 and gateYC == gateY1:
                    gateXC = gateX2
                    gateYC = gateY2
                else:
                    gateXC = gateX1
                    gateYC = gateY1
    
    for i in range (6):
        if cursorX == wallX[i] and cursorY == wallY[i] :
            cursorX = oldcursorX
            cursorY = oldcursorY
        if badguyX == wallX[i] and badguyY == wallY[i] :
            badguyX = oldbadguyX
            badguyY = oldbadguyY
            if ticker == 1:
                if badguyX < cursorX :
                    badguyX = badguyX + 1
                elif badguyX > cursorX :
                    badguyX = badguyX - 1
            elif ticker == 0:
                if badguyY < cursorY :
                    badguyY = badguyY + 1
                elif badguyY > cursorY :
                    badguyY = badguyY - 1

    if ewall == 1 :
        for i in range (6):
            if cursorX == ewallX[i] and cursorY == ewallY[i] :
                cursorX = oldcursorX
                cursorY = oldcursorY
            if badguyX == ewallX[i] and badguyY == ewallY[i] :
                badguyX = oldbadguyX
                badguyY = oldbadguyY
                if ticker == 1:
                    if badguyX < cursorX :
                        badguyX = badguyX + 1
                    elif badguyX > cursorX :
                        badguyX = badguyX - 1
                elif ticker == 0:
                    if badguyY < cursorY :
                        badguyY = badguyY + 1
                    elif badguyY > cursorY :
                        badguyY = badguyY - 1

    if mwall == 1 :
        for i in range (26):
            if cursorX == mwallX[i] and cursorY == mwallY[i] :
                cursorX = oldcursorX
                cursorY = oldcursorY
            if badguyX == mwallX[i] and badguyY == mwallY[i] :
                badguyX = oldbadguyX
                badguyY = oldbadguyY
                if ticker == 1:
                    if badguyX < cursorX :
                        badguyX = badguyX + 1
                    elif badguyX > cursorX :
                        badguyX = badguyX - 1
                elif ticker == 0:
                    if badguyY < cursorY :
                        badguyY = badguyY + 1
                    elif badguyY > cursorY :
                        badguyY = badguyY - 1

    if switch == 1 :
        if cursorX == gateXC and cursorY == gateYC :
            cursorX = oldcursorX
            cursorY = oldcursorY
        if badguyX == gateXC and badguyY == gateYC :
            badguyX = oldbadguyX
            badguyY = oldbadguyY
            if ticker == 1:
                if badguyX < cursorX :
                    badguyX = badguyX + 1
                elif badguyX > cursorX :
                    badguyX = badguyX - 1
            elif ticker == 0:
                if badguyY < cursorY :
                    badguyY = badguyY + 1
                elif badguyY > cursorY :
                    badguyY = badguyY - 1

    for i in range (6):
        if badguyX == wallX[i] and badguyY == wallY[i] :
            badguyX = oldbadguyX
            badguyY = oldbadguyY
    
    if ewall == 1:
        for i in range (6):
            if badguyX == ewallX[i] and badguyY == ewallY[i] :
                badguyX = oldbadguyX
                badguyY = oldbadguyY

    if mwall == 1:
        for i in range (26):
            if badguyX == mwallX[i] and badguyY == mwallY[i] :
                badguyX = oldbadguyX
                badguyY = oldbadguyY

    if switch == 1:
        if badguyX == gateXC and badguyY == gateYC :
            badguyX = oldbadguyX
            badguyY = oldbadguyY
            
    if cursorX == treasureX and cursorY == treasureY and jitter == 1:
        goldbar = 1
        jitter = 0
        gold = gold + 1

    if cursorX == badguyX and cursorY == badguyY :
        battle()
        if win == 1:
            triggered = 0
        elif win == 0:
            died()
