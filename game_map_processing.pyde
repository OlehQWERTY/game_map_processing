timeIt = 0
fieldSize = 50
aList = [[], []]

print(aList)

def setup():
    size(800, 600, P2D)
    background(0, 0, 0)
    frameRate(60)

def gameField():
    stroke(127)
    fill(255)
    for n in range(0, width, fieldSize):
        for m in range(0, height, fieldSize):
            rect(n, m, fieldSize, fieldSize) 
            
def wall():
    stroke(12)
    fill(0)
    for i in range(len(aList[0])):
        # print(aList[0][i])
        # print("_________________")
        rect(int(aList[0][i]) * fieldSize, int(aList[1][i]) * fieldSize, fieldSize, fieldSize)
        
def select(x, y, a = 0):
    if a == 1:
        stroke(127, 0, 127)
    else:
        stroke(12)
    
def mouse():
    if  mousePressed:
        fill(127,255)
        print(mouseX, mouseY)
        # wall(x, y)
        
        aList[0].append(int(mouseX/fieldSize))
        aList[1].append(int(mouseY/fieldSize))
        # wall(int(mouseX/fieldSize), int(mouseY/fieldSize))
    else:
        int(mouseX/fieldSize)
        int(mouseY/fieldSize)
        fill(255)
        
    ellipse(mouseX, mouseY, 10, 10)
    # wall(int(mouseX/fieldSize), int(mouseY/fieldSize))
    return mouseX, mouseY
    
    
    
def draw():
    gameField()
    global timeIt
    global x, y
    timeIt += 1

    # if not timeIt % 60:
    #     x = random(0, width / fieldSize)
    #     y = random(0, height / fieldSize)
    #     # print(int(random(0, width / fieldSize)))
        
    # wall(x, y)

    x, y = mouse() 
    print(x, y)
    if len(aList[0]) > 2:
        wall()
        
    select(int(x/fieldSize), int(y/fieldSize), a = 0)
    
    
    
    # line(12, 25, 56, 85)
    
            
            # print(n)
            
            
    # if  mousePressed:
    #     fill(0)
    # else:
    #     fill(255)
    # ellipse(mouseX, mouseY, 80, 80)
