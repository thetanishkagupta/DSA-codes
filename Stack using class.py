class Stack(object):
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if self.isemptay():
            return("Stack is Empty")
        else:
            return self.items.pop()

    def peek(self):
        if self.items:
            print(self.items[-1])
        else:
            return None

    def isempty(self):
        if self.items == []:
            return True
        else:
            return False

    def size(self):
        print(len(self.items))

    def display(self):
        print(self.items)

if __name__ == '__main__':
    stack = Stack()
while True:
    print("Select the Operation 1.Push 2.Pop 3.Peek 4.Size 5.Display 6.Quit")
    choice = int(input())
    if choice == 1:
        x = int(input("enter the data: "))
        stack.push(x)
        print(x,"pushed successfully")
    elif choice == 2:
        p = stack.pop()
        print(p,"popped out successfully")
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.size()
    elif choice == 5:
        stack.display()
    elif choice == 6:
         break
    else:
         print("Enter the correct option!!")
