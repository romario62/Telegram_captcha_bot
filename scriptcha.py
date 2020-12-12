import os, random
cap_base = []
filename = random.choice(os.listdir("samples/"))
print(filename)
s = filename[:5]
print(s)

'''otvet = str(input())
if otvet in filename:
    print('succes')
else:
    print('no')'''