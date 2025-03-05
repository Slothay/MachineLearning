import numpy as np

def distance(x1,y1,x2,y2):
    point_distance = np.sqrt((y2-y1)**2 + (x2-x1)**2)
<<<<<<< HEAD

    return point_distance

x1=0
x2=3
y1=0
y2=4

print(distance(x1,y1,x2,y2))
=======
    return point_distance


x1=0
y1=0
x2=3
y2=4

print(distance(x1,y1,x2,y2))
>>>>>>> f28d5023d7e7b822b96e408b6342d698c10c7e69
