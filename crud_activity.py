checklist = []
#create
def create(item):
    checklist.append(item)
#read
def read(index)
    if index > range(checklist):
        print("Please enter a valid index")
    else:
        print(f"At index {index}, you have {checklist[index]}")
#update
def update(index, item):
     if index > len(checklist):
        print("Please enter a valid index")
    checklist[index] = item
#destroy
def destroy(index):
    if index >= len(checklist):
        prin("Enter a valid index")
    checklist[index].remove()
       

