# add different types of materials
# save map
# load map
# add check material number < numberOfMaterials

# imgBrokenGlass = PImage
# imgStone = PImage
# imgTree = PImage 

timeIt = 0
fieldSize = 25
aList = [[], [], []] # posX posY matterial
tool = 0 # chosen tool

materials = [[255, 0, 20], [0, 255, 20], [0, 20, 255]]


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
    
    imgBrokenGlass = loadImage("brokenGlass.png")
    imgStone = loadImage("stone.png")
    imgTree = loadImage("tree.png")


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
        print(materials[1])
        print(aList[2][1])
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
                    
        tPos = toolsPos(posX, posY)
        print("tPos %d" % tPos)
        # print(tPos)
        if tPos != -1:
            tool = tPos
            print("tPos %d" % tPos)
            # if tPos == 0:
            #     print("Glass")
            # if tPos == 1:
            #     print("Stone")
            # if tPos == 2:
            #     print("Wood")
            
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
    if posY > (height - toolsZone)/fieldSize:
        iterToolsX = width/fieldSize/4
        for i in range(iterToolsX, -1, -1): # -1 because of min toolsPos is 0, next -1 is iterator
            if posX >= i*4:  
                # print("Tools Zone! %d" % i)
                return i
                break
    return -1
    
def draw():
    # background(255)
    gameField()
    global timeIt
    timeIt += 1

    # if not timeIt % 60: # ones per second
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
    
    image(imgBrokenGlass, 0, height - toolsZone, 100, 100)
    image(imgStone, 100, height - toolsZone, 100, 100)
    image(imgTree, 200, height - toolsZone, 100, 100)
