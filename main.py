import matplotlib.image as mpimg
import numpy as np


filename=input()
image = mpimg.imread(filename)
keys=[ord(s)-ord('A') for s in input().split()]


delta=400//3
diameter=30
score=0
def value(i,j):
    center=(50+delta*j, 50+delta*i)
    r=int(diameter/2)
    r-=2
    count=0
    for x in range(-r, r+1):
        for y in range(-r, r+1):
            if x*x+y*y<=r*r:
                if image[center[1]+y][center[0]+x][0]==0:
                    count+=1
    if count>=(0.75)*(np.pi)*r*r:
        return 1
    return 0
for i in range(4):
    ans=[value(i,j) for j in range(4)]
    correctans=[keys[i]==j for j in range(4)]        
    score+=(ans==correctans)
print(score)
