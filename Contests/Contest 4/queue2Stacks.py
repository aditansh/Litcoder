import sys

def enqueue(val):
    stack1.append(val)

def dequeue():
    if len(stack2) == 0 and len(stack1) == 0:
        return -1
    elif len(stack2) == 0 and len(stack1) > 0:
        while len(stack1) > 0:
            stack2.append(stack1.pop())
        return stack2.pop()
    else:
        return stack2.pop()

def peek():
    if len(stack2) == 0 and len(stack1) == 0:
        return -1
    elif len(stack2) == 0 and len(stack1) > 0:
        while len(stack1) > 0:
            stack2.append(stack1.pop())
        return stack2[-1]
    else:
        return stack2[-1]

stack1 = []
stack2 = []

operations = input().split(",")
for operation in operations:
    operator = operation.split(" ")[0]
    if operator == "1":
        enqueue(int(operation.split(" ")[1]))
    elif operator == "2":
        dequeue()
    elif operator == "3":
        print(peek())