#Queue In Python

#Basic
Rear = 0
c = []
MAX = 5

#Enqueue/Add
def Enqueue():
    global Rear,MAX
    if len(c) == MAX:
        print("Queue IS FULL")
    else:
        print("Please Enter the Number")
        k = int(input())
        c.append(k)
        Rear +=1

#Dequeue/Delete
def Dequeue():
    global Rear,MAX
    if len(c) == 0:
        print("Queue is empty")
    else:
        c.pop(0)
        Rear = Rear -1

#Peek
def Peek():
    print("The Whole Queue is ", c)

#Main Container
for i in range(989898):
    print("Please Enter Your Choice")
    print("(1) Enqueue")
    print("(2) Dequeue")
    print("(3) Peek")
    print("(4) Quit")
    n = int(input())
    if n == 1:
        Enqueue()
        print("")
    if n == 2:
        Dequeue()
        print("")
    if n == 3:
        Peek()
        print("")
    if n == 4:
        print("Thank You")
        break
    else:
        pass