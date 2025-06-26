from random import randint
import textgraph


from getkey import getkey, keys
import os
import random
from datetime import datetime

words = []


def clear():
    os.system("cls")


with open('words.txt', 'r') as file:
    # Iterate over each line in the file object
    for line in file:
        processed_line = line.strip()
        if (len(processed_line) > 2 and "'" not in processed_line):
            words.append(processed_line)
characters = []
pressed = []
state = 1


def on_press(key):
    clear()
    print("".join(chars))
    print("".join(pressed))
    if (key == Key.esc):
        print("Escape")
        return False
    pressed.append(str(key))


print("PythonType")
print("Length: ")
wlen = int(input(":"))
ranwords = [random.choice(words) for i in range(wlen)]
chars = list(" ".join(ranwords))
print("".join(chars))
print("".join(pressed))
times = []
beg = datetime.now()
st = datetime.now()
grouping = []
c = 0

while True:
    key = getkey()
    if (key in list("abcdefghijklmnopqrstuvwxyz ")):
        pressed.append(key)
        clear()
        print("".join(chars))
        print("".join(pressed))
        if (len(pressed) == 1):
            st = datetime.now()
            beg = datetime.now()
        if (len(pressed) % 2 == 0):
            times.append(datetime.now() - st)
            grouping.append("".join(pressed[-2:]))
            c += 1
            st = datetime.now()

    if (key == keys.ENTER):
        print()
        wpmda = ([60/((int(x.microseconds) + int(x.seconds) * 1000000) /
              1000000) * (len(grouping[times.index(x)])/5) for x in times])
        print(textgraph.vertical(wpmda))
        dif = datetime.now() - beg
        print(60/((int(dif.microseconds) + int(dif.seconds) * 1000000)/1000000)
              * (len(pressed)/5))
        break