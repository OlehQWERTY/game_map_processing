# add different types of materials
# save map
# load map
# add check material number < numberOfMaterials

import os.path # cheacking whether file exist
import time # pouse func
#PrintWriter output
# sys.setrecursionlimit(10000) # set recursion limit


timeIt = 0
fieldSize = 25
aList = [[], [], []] # posX posY matterial
tool = 0 # chosen tool

# more than 3 (materials number) beacause of temp 
# solution for error caused pressing toolbox pos > 3
materials = [[255, 0, 20], [0, 255, 20], [0, 20, 255], [255, 0, 20], [255, 0, 20], [255, 0, 20], [255, 0, 20]] 

saveRes = 0

# print(aList)

def setup():
    # real size is height + 100 because of tools panel
    size(800, 600, P2D) # better performans for 2d
    global toolsZone
    toolsZone = 100 # height + toolsZone
    background(255)
    frameRate(60)
    
    # image load
    global imgBrokenGlass
    global imgStone
    global imgTree
    global imgLoad
    global imgSave
    global imgDice
    global imgBin
    
    imgBrokenGlass = loadImage("brokenGlass.png")
    imgStone = loadImage("stone.png")
    imgTree = loadImage("tree.png")
    imgLoad = loadImage("load.png")
    imgSave = loadImage("save.png")
    imgDice = loadImage("dice.png")
    imgBin = loadImage("bin.png") # bin.png

def gameField(): # draw fields
    stroke(127)
    strokeWeight(1)
    fill(255)
    global toolsZone
    for n in range(0, width, fieldSize):
        for m in range(0, height - toolsZone, fieldSize):
            rect(n, m, fieldSize, fieldSize) 

def wall(): # draw rects
    stroke(12)
    strokeWeight(1)
    for i in range(len(aList[0])):
        # print(materials[1])
        # print(aList[2][1])
        fill(materials[aList[2][i]][0], materials[aList[2][i]][1], materials[aList[2][i]][2]) # color according to material
        rect(int(aList[0][i]) * fieldSize, int(aList[1][i]) * fieldSize, fieldSize, fieldSize)

def select(posX, posY): # light of selected field 
    global toolsZone
    stroke(127, 0, 127)
    strokeWeight(2)
    if posX < width/fieldSize and posY < (height - toolsZone)/fieldSize:
        rect(int(posX) * fieldSize, int(posY) * fieldSize, fieldSize, fieldSize)

def mouse():
    posX = int(mouseX/fieldSize)
    posY = int(mouseY/fieldSize)
    global tool
    if  mousePressed and (mouseButton == LEFT):
        # fill(127,255)
        # print(type(aList))
        
        if posX < width/fieldSize and posY < (height - toolsZone)/fieldSize:
            if len(aList[0]) <= 1:
                aList[0].append(posX)
                aList[1].append(posY)
                aList[2].append(tool) # matterial
            else:
                # print(len(aList[0]))
                if not checkElementInList(posX, posY):
                    aList[0].append(posX)
                    aList[1].append(posY)
                    aList[2].append(tool) # matterial
                    
                    # global tool
                    # if(tool > 2): # if tools > 2 (not 0, 1, 2)
                    #     print("Error: not possible color!")
                    #     tool = 0
                    # else:
                    #     print(tool)
                    #     aList[2].append(tool) # matterial
                    
        tPos = toolsPos(posX, posY)
        # print("tPos %d" % tPos)
        # print(tPos)
        if tPos != -1:
            tool = tPos
            # print("tPos %d" % tPos)
            # if tPos == 0:
            #     print("Glass")
            # if tPos == 1:
            #     print("Stone")
            # if tPos == 2:
            #     print("Wood")
            
            if tPos == 4:
                print("Clear")
                clearList()                
            if tPos == 5:
                print("Load")
                load()
            if tPos == 6:
                print("Save")
                global saveRes
                saveRes = save(saveRes+1)
            if tPos == 7:
                print("Autogen")
                clearList() # cleare map befor autogen
                
                # Undel this line it is possible to choose (uncomment) autogen algorithm. ONLY ONE per time!
                
                percentage = 30 # < 80 because of bug in connected with reccursion autogen()
                
                # autogen((percentage * 0.01) * (width/fieldSize) * ((height - toolsZone)/fieldSize)) # (int(points ammount))
                autogenRandDirection(8, percentage) # (max length of points siquence, percentage(from 1 to 100))
                
            time.sleep(1)
                
    elif mousePressed and (mouseButton == RIGHT):
        if checkElementInList(posX, posY):
            index = checkElementInList(posX, posY, True)
            del aList[0][index]
            del aList[1][index]
            del aList[2][index]
    else:
        fill(255)
    return posX, posY
    
def checkElementInList(x, y, mode = False):
    for i in range(len(aList[0])):
        if aList[0][i] == x and aList[1][i] == y:
            if not mode: 
                return True
            else:
                return i
    return False

def toolsPos(posX, posY):
    # tools pos
    # print(posX)
    if posY >= (height - toolsZone)/fieldSize:
        iterToolsX = width/toolsZone
        for i in range(iterToolsX, -1, -1): # -1 because of min toolsPos is 0, next -1 is iterator
            # print((toolsZone/fieldSize))
            if posX >= i*(toolsZone/fieldSize):  
                # print("Tools Zone! %d" % i)
                return i
                break
    return -1

def is_number(s): # checking string is_number
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def load():
    i = 0
    dirPath = "C:/Git/game_map_processing/"
    filePath = "maps/map" + "load" + ".txt"
    if os.path.isfile(dirPath + filePath):
        lines = loadStrings(dirPath + filePath)
        for line in lines:
            # print(line + "kfjgnf" + str(i))
            line = line.replace("[", "")
            line = line.replace("]", "")
            line.split(',')
            # print(line)
            if i == 0 or i == 2 or i == 4: # i = 1, 3, 5 is /n strings
                # print(line + "kfjgnf" + str(i))
                for val in line:
                    # print(val)
                    # val.replace(",", "")
                    print(val)
                    if is_number(val): # other lines is ',' lines
                        if i == 0:
                            aList[i].append(int(val)) 
                        else:
                            aList[i/2].append(int(val))    
            i+=1
    else:
        print("Error: can't open mapload.txt or file doesn't exist!")
    
def save(i = 0):
    # print(i)
    dirPath = "C:/Git/game_map_processing/"
    filePath = "maps/map" + str(i) + ".txt"
    
    if os.path.isfile(dirPath + filePath):
        print("File: " + filePath + " in: " + filePath + " is already exist!")
        return save(i + 1)
    else:
        
        output = createWriter(str(filePath))
        
        global aList
        for item in aList:
            output.println("%s\n" % item)
        
        # output = createWriter(str(filePath))
        # output.println(str(i)) # Write the coordinate to the file
        output.flush() # Writes the remaining data to the file
        output.close() # Finishes the file
        
        print("Saved")
        return i
    
        # print(os.path.abspath(filePath)) # saves to C:\Users\Oleg\AppData\Local\Temp\game_map_processing1973036018282129998\maps\map0.txt
        # print(dirPath + filePath)
        # print(os.path.isfile(dirPath + filePath)) # print(os.path.isfile("C:\Git\game_map_processing\map0.txt"))
        
        # if os.path.isfile("maps/map0.txt"): # os.path.exists(output):
        #     print("File exist!")
        # else:
        #     print("file isn't exist!")
    
        # exit() # Stops the program
    
def autogen(i=0): # random points
    if (i > 0) and (i < (width/fieldSize) * (height - toolsZone)/fieldSize):
        
        posX = int(random(width/fieldSize))
        posY = int(random((height - toolsZone)/fieldSize))
        randColor = int(random(3))
        
        aList[0].append(posX)
        aList[1].append(posY)
        aList[2].append(randColor) # matterial
        
        # print("posX[%d] = %d, posY[%d] = %d" % (i, posX, i, posY))
        i-=1
        autogen(i)
    else:
        return True
    
    return False

def randDirection(flag = True):
    if flag == True:
        directions = [[-1, 1], [0, 1], [1, 1], \
                      [-1, 0], [1, 0], \
                      [-1, -1], [0, -1], [1, -1]]
    else:
        directions = [[0, 1], \
                      [-1, 0], [1, 0], \
                      [0, -1]]
        
    return directions[int(random(len(directions)))]

def autogenRandDirection(i=2, percentage = 20): # random direction; i - it is max of steps per one time
    # print((percentage * 0.01) * (width/fieldSize) * ((height - toolsZone)/fieldSize))
    if percentage >= 100: 
        percentage = 100 
        print("Percentage out of max range!")
    elif percentage < 1:
        percentage = 1
        print("Percentage out of min range!")
    else:
        for n in range(int((percentage/i * 0.01) * (width/fieldSize) * ((height - toolsZone)/fieldSize))):
            posX = int(random(width/fieldSize))
            posY = int(random((height - toolsZone)/fieldSize))
            randColor = int(random(3))
            
            # first point
            aList[0].append(posX)
            aList[1].append(posY)
            aList[2].append(randColor) # matterial
            
            for m in range(i - 1):  # without firs point
                direction = randDirection(False) # can be called with True key (True - <, >, ^, v False - 8 directions)
                if checkElementInList(posX, posY, True):
                    posX = posX + direction[0]
                    posY = posY + direction[1]
                    if posY >= (height - toolsZone)/fieldSize:
                        posY=posY-1
                    aList[0].append(posX)
                    aList[1].append(posY)
                    aList[2].append(randColor) # matterial
                else:
                #     i=i-1
                    break
                # print('n= ' + str(n) + ' posX= ' + str(posX) + ' posY= ' + str(posY) + ' randColor= ' + str(randColor))
            # print(randDirection())
        return True
        
    
        
def clearList(ammount = 0):
    if ammount <= 0:
        ammount = len(aList[0])

    del aList[0][0:ammount]
    del aList[1][0:ammount]
    del aList[2][0:ammount]   
    
    
def draw():
    # background(255)
    gameField()
    global timeIt
    timeIt += 1

    global saveRes
    if not timeIt % 120: # ones per second
        # autogen(10)
        # print("Iteration")
        # saveRes = save(saveRes+1)
        pass

    #     x = random(0, width / fieldSize)
    #     y = random(0, height / fieldSize)
    #     # print(int(random(0, width / fieldSize)))

    posX, posY = mouse() 
    # print(posX, posY)
    select(posX, posY)
    if len(aList[0]) > 1:
        wall()
    
    global toolsZone
    
    # images show
    global imgBrokenGlass
    global imgStone
    global imgTree
    global imgLoad
    global imgSave
    global imgDice
    global imgBin
    
    image(imgBrokenGlass, 0, height - toolsZone, toolsZone, toolsZone)
    image(imgStone, toolsZone, height - toolsZone, toolsZone, toolsZone)
    image(imgTree, toolsZone * 2, height - toolsZone, toolsZone, toolsZone)
    
    image(imgBin, toolsZone * 4, height - toolsZone, toolsZone, toolsZone)
    image(imgLoad, toolsZone * 5, height - toolsZone, toolsZone, toolsZone)
    image(imgSave, toolsZone * 6, height - toolsZone, toolsZone, toolsZone)
    image(imgDice, toolsZone * 7, height - toolsZone, toolsZone, toolsZone)
