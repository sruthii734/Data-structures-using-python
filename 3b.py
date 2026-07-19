class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
top = None
def push():
    global top
    data = input("Enter book title: ")
    newNode = Node(data)

    if top is None:
        newNode.next = None
    else:
        newNode.next = top

    top = newNode
    print("Book inserted successfully")
def pop():
    global top

    if top is None:
        print("Stack is empty!!!")
    else:
        temp = top
        print("Deleted book:", temp.data)
        top = top.next
def display():
    global top
    if top is None:
        print("Stack is empty!!!")
    else:
        temp = top
        print("Stack Elements:")
        while temp is not None:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("NULL")
while True:
    print("\nSTACK USING LINKED LIST")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
           
