import sys

class Editor:
    def __init__(self):
        self.arr = [""]
    
    def insert(self, string):
        self.arr.append(self.arr[-1] + string)
    
    def delete(self, k):
        if len(self.arr) < 2:
            return
        elif len(self.arr[-1]) < k:
            self.arr.append("")
        else:
            self.arr.append(self.arr[-1][:-k])

    def get(self, k):
        if len(self.arr) < 2:
            return
        elif len(self.arr[-1]) < k:
            return
        else:
            print(self.arr[-1][k-1])

    def undo(self):
        if len(self.arr) > 1:
            self.arr.pop()
        else:
            return


editor = Editor()
operations = input().split(",")
for operation in operations:
    operator = operation.split(" ")[0]
    if operator == "1":
        editor.insert(operation.split(" ")[1])
    elif operator == "2":
        editor.delete(int(operation.split(" ")[1]))
    elif operator == "3":
        editor.get(int(operation.split(" ")[1]))
    elif operator == "4":
        editor.undo()