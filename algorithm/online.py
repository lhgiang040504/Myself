'''import sys


online = []
while True:
    inputs = sys.stdin.readline().strip().split()

    if inputs[0] == "1":
        online.append(inputs[1])
        online.sort()
    elif inputs[0] == "2":
        if inputs[1] in online:
            sys.stdout.write(str(online.index(inputs[1])) + "\n")
        else:
            sys.stdout.write("0\n")
    else:
        break


'''
import sys

def add_userid(online, usernameid):
    if usernameid > online[-1]:
        online.append(usernameid)
        return
    for i in range(len(online)):
        if usernameid < online[i]:
            online.insert(i, usernameid)
            return

def find_user_index(online, username):
    try:
        return online.index(username)
    except ValueError:
        return 0 
    
online = [0]
check = set()
while True:
    inputs = list(map(int, sys.stdin.readline().strip().split()))
    if inputs[0] == 1:
        if inputs[1] not in check:
            add_userid(online, inputs[1]) 
            check.add(inputs[1])
    elif inputs[0] == 2:
        user_index = find_user_index(online, inputs[1])
        sys.stdout.write(str(user_index) + "\n")
    else:
        break