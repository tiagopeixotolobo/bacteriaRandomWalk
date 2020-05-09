import numpy as np
import copy
import random
import matplotlib.pyplot as plt
import os
import subprocess

def randomDir(i, j,sx,sy):
    direction = random.randrange(1, 5, 1)
    if direction == 1:
        k = i - 1
        n = j
    if direction == 2:
        k = i + 1
        n = j
    if direction == 3:
        k = i
        n = j - 1
    if direction == 4:
        k = i
        n = j + 1

    if (n < 0):
        n = 0
    if (k < 0):
        k = 0
    if (k>=sx):
        k = sx-1
    if (n>=sy):
        n=sy-1

    return k, n


sizeGridx = 100
sizeGridy = 100

Aold = np.zeros((sizeGridx, sizeGridy))

# Initial Conditions
Aold[50, 50] = 1  # 1 bacteria in the site 5,5

nIterations = 50
# auxiliar matrix to avoid iterating over new values while not finishing one single loop
Anew = copy.deepcopy(Aold)

files = []

fig, ax = plt.subplots(figsize=(5, 5))
plt.cla()
plt.imshow(Anew, extent=[0, 1, 0, 1])
fname = '_tmp%03d.png' % 0
plt.savefig(fname)
files.append(fname)

for m in range(1,nIterations):
    for i in range(0, Aold.shape[0]):
        for j in range(0, Aold.shape[1]):
            if Aold[i][j] != 0:
                (k, n) = randomDir(i, j,sizeGridx,sizeGridy)
                Anew[k, n] = Aold[k,n] + 1
    fname = '_tmp%03d.png' % m
    plt.imshow(Anew, extent=[0, 1, 0, 1])
    Aold = copy.deepcopy(Anew)
    plt.savefig(fname)
    files.append(fname)

out_movie = "ffmpeg -r 10 -i _tmp%03d.png -r ntsc test.mp4"
print(out_movie)
subprocess.call("ffmpeg -r 10 -i _tmp%03d.png -r ntsc"+str(out_movie), shell=True)


for fname in files:
    os.remove(fname)
