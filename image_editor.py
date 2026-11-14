import numpy as np
import cv2

img = input("image loaction:-")
image = cv2.imread(img)

if image is None:
    print("ERROR 404: INPUT THE IMAGE FIRST!!")
    exit()
else:
     print("WELL DONE!! SUCCESFULLY IMAGE IS LOAD")

def save():
    ssb = input("you want show , save or both ??? :->")
    if ssb == "show":
        cv2.imshow("NEW_IMAGE_EDITIED",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif ssb == "save":
        filename = input("FILE NAME FOR SAVING THE FILE IN (jpeg,png,jpg) format:-")
        cv2.imwrite(filename,image)
    elif ssb == "both":
        cv2.imshow("NEW_IMAGE_EDITIED",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()  

        filename = input("FILE NAME FOR SAVING THE FILE IN (jpeg,png,jpg) format:-")
        cv2.imwrite(filename,image)      

    

def line():
    print("INPUT:-")
    x1 = int(input("enter the x1:-"))
    y1 = int(input("enter the y1:-"))
    x2 = int(input("enter the x2:-"))
    y2 = int(input("enter the y2:-"))
    thick = int(input("enter thickness:-"))
    print("note default color is blue")
    color = (255,0,0)
    pt1 = (x1,y1)
    pt2 = (x2,y2)
    cv2.line(image,pt1,pt2,color,thick)
    save()

def circle():
    print("INPUT:-")
    x = int(input("enter the x1:-"))
    y = int(input("enter the y1:-"))
    radius = int(input("enter radius:-"))
    thick = int(input("enter thickness:-"))
    print("note default color is blue")
    color = (255,0,0)
    center = (x,y)
    cv2.circle(image,center,radius,color,thick)
    save()

def rect():
    print("INPUT:-")
    x1 = int(input("enter the x1:-"))
    y1 = int(input("enter the y1:-"))
    x2 = int(input("enter the x2:-"))
    y2 = int(input("enter the y2:-"))
    thick = int(input("enter thickness:-"))
    print("note default color is blue")
    color = (255,0,0)
    pt1 = (x1,y1)
    pt2 = (x2,y2)
    cv2.rectangle(image,pt1,pt2,color,thick)
    save()

def text():
    print("INPUT:-")
    txt = input("WHAT YOU SHOWING IN THE TEXT:->")
    fontsize = float(input("enter the font size:-"))
    print("now enter the parameter:-")
    x = int(input("enter the paramter x:-"))
    y = int(input("enter the parameter y:-"))
    org = (x,y)
    thick = int(input("enter thickness:-"))
    color = (255,0,0)
    print("note default color is blue")
    cv2.putText(image,txt,org,cv2.FONT_HERSHEY_DUPLEX,fontsize,color,thick)
    save()

opr = input("WHICH OPERATION {LINE(L),CIRCLE(C),RECTANGLE(R),TEXT(T)}:-")
if opr == 'L':
    line()
elif opr == "C":
    circle()
elif opr == "R":
    rect()
elif opr == "T":
    text() 
else:
    print("!! WARNING !! INVALID INPUT !! ")        