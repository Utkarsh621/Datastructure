#stack using Python

#Basic
TOP=0
MAX=5
c=[]

def Push():
    global TOP
    if TOP==MAX:
        print("Stack is FULL")
    
    else:
        print("Please Enter the number")
        k = int(input())
        c.append(k)
        TOP += 1

def Pop():
    global TOP
    if TOP == 0:
        print("Stack EMPTY")
    else:
        c.pop()
        TOP -= 1

def Display():
    print("------------")
    for i in reversed(range(len(c))):
        print(c[i])

#Main Container
for i in range(989898):
    print("Please Enter Your Choice")
    print("(1) Push")
    print("(2) Pop")
    print("(3) Display")
    print("(4) Quit")
    n = int(input())
    if n == 1:
        Push()
        print("")
    if n == 2:
        Pop()
        print("")
    if n == 3:
        Display()
        print("")
    if n == 4:
        print("Thank You")
        break
       
