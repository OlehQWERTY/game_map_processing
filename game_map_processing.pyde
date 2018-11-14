# add different types of materials
# save map
# load map

PImage imgBrokenGlass
PImage imgStone
PImage imgTree

timeIt = 0
fieldSize = 25
aList = [[], []]

print(aList)

def setup():
    size(800, 600, P2D) # better performans for 2d
    background(0, 0, 0)
    frameRate(60)
    
    imgBrokenGlass = requestImage("brokenGlass.png")
    imgStone = loadImage("stone.png");
    imgTree = loadImage("tree.png");

def gameField(): # draw fields
    stroke(127)
    strokeWeight(1)
    fill(255)
    for n in range(0, width, fieldSize):
        for m in range(0, height, fieldSize):
            rect(n, m, fieldSize, fieldSize) 

def wall(): # draw rects
    stroke(12)
    strokeWeight(1)
    fill(0)
    for i in range(len(aList[0])):
        rect(int(aList[0][i]) * fieldSize, int(aList[1][i]) * fieldSize, fieldSize, fieldSize)

def select(posX, posY): # light of selected field 
    stroke(127, 0, 127)
    strokeWeight(2)
    rect(int(posX) * fieldSize, int(posY) * fieldSize, fieldSize, fieldSize)

def mouse():
    posX = int(mouseX/fieldSize)
    posY = int(mouseY/fieldSize)
    if  mousePressed and (mouseButton == LEFT):
        fill(127,255)
        # print(type(aList))
        if len(aList[0]) <= 1:
            aList[0].append(posX)
            aList[1].append(posY)
        else:
            print(len(aList[0]))
            if not checkElementInList(posX, posY):
                aList[0].append(posX)
                aList[1].append(posY)
    elif mousePressed and (mouseButton == RIGHT):
        if checkElementInList(posX, posY):
            index = checkElementInList(posX, posY, True)
            del aList[0][index]
            del aList[1][index]
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
    
def draw():
    gameField()
    global timeIt
    timeIt += 1

    # if not timeIt % 60: # ones per second
    #     x = random(0, width / fieldSize)
    #     y = random(0, height / fieldSize)
    #     # print(int(random(0, width / fieldSize)))

    posX, posY = mouse() 
    print(posX, posY)
    select(posX, posY)
    if len(aList[0]) > 1:
        wall()
        
    image(imgBrokenGlass, 0, 0);
    image(imgStone, 0, 0);
    image(imgTree, 0, 0);
    # image(img, 0, 0, width/2, height/2);
        


  
    
