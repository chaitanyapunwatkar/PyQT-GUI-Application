from PIL import Image
import os
import random as rd
os.mkdir('Item1')
count = 1

for x in range(10):
    for j in range(2):
        for i in range(1,5):
            img = Image.open("test{0}.jpg".format(i))
            img.save("Item1\{0}.jpg".format(count))
            count+=1

    img_bad = Image.open("bad{}.jpg".format(rd.randint(1,5)))
    img_bad.save("Item1\{0}.jpg".format(count))
    count+=1
    img = Image.open("test{}.jpg".format(rd.randint(6,7)))
    img.save("Item1\{0}.jpg".format(count))
    count+=1

print(count)
