# add different types of materials
# save map
# load map
# add check material number < numberOfMaterials

import os.path # cheacking whether file exist
import time # pouse func
#PrintWriter output

timeIt = 0
fieldSize = 100
aList = [[], [], []] # posX posY matterial
tool = 0 # chosen tool

materials = [[255, 0, 20], [0, 255, 20], [0, 20, 255]]
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
    
    imgBrokenGlass = loadImage("brokenGlass.png")
    imgStone = loadImage("stone.png")
    imgTree = loadImage("tree.png")
    imgLoad = loadImage("load.png")
    imgSave = loadImage("save.png")

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
            
            if tPos == 5:
                print("Load")
                load()
                
                time.sleep(1)
            if tPos == 6:
                print("Save")
                global saveRes
                saveRes = save(saveRes+1)
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
    
def draw():
    # background(255)
    gameField()
    global timeIt
    timeIt += 1

    global saveRes
    if not timeIt % 60: # ones per second
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
    
    image(imgBrokenGlass, 0, height - toolsZone, toolsZone, toolsZone)
    image(imgStone, toolsZone, height - toolsZone, toolsZone, toolsZone)
    image(imgTree, toolsZone * 2, height - toolsZone, toolsZone, toolsZone)
    
    image(imgLoad, toolsZone * 5, height - toolsZone, toolsZone, toolsZone)
    image(imgSave, toolsZone * 6, height - toolsZone, toolsZone, toolsZone)
