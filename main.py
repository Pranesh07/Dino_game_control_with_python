import pyautogui
from PIL import Image, ImageGrab
import time
from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(300,420):
        for j in range(400,450):
            if data[i,j] <100:
                hit("up")
                return True
    for i in range(280,420):
        for j in range(200,377):
            if data[i,j] <100:
                hit("down")
                return True
    return False

if __name__=="__main__":
    print("Hey... Dino game about to start in 3 Seconds")
    time.sleep(3)
    # hit("up")
    while True:
        image= ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
            
    # print(asarray(data))
    # for i in range(280,420):
    #     for j in range(380,450):
    #         data[i,j]=0
    # for i in range(280,420):
    #     for j in range(200,377):
    #         data[i,j]=170
    # image.show()
