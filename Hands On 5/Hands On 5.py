'''
def main():
    with open("pig_dice_rules.txt", 'r') as my_file:
        print(my_file.read())
if __name__=="__main__":
    main()


inv = "wizard_inventory.txt"
all_item = "wizard_all_items.txt"
import random

def main():
    print("The Wizard Inventroy Program")
    print("COMMAND MENU")
    print("walk - Walk down the path","show - Show all items","drop - Drop an item","exit - Exit program",sep="\n")
    while True:
        choice = input()
        if choice.lower()=="walk":
            walk()
        elif choice.lower()=="show":
            show()
        elif choice.lower()=="drop":
            drop()
        else:
            exit()
        

def walk():
    loot=[]
    with open(all_item, 'r') as my_file:
        loot=my_file.readlines()
    
    drops=random.randrange(9)
    print("Command: walk")
    print("While walking down a path, you see ",loot[drops],". Do you want to grab it? (y/n):",sep='')
    choice=input()
    
    with open(inv,'r') as my_file:
        lines=len(my_file.readlines())
        if lines==4:
            print("You can't carry any more items. Drop something first.")
            return
    
    with open(inv, 'a') as my_file:
        if choice.lower()=='y':
            item=loot[drops]
            my_file.write(item)
            print("you picked up a",loot[drops])
    
def show():
    with open(inv, 'r') as my_file:
        print(my_file.read())
    
def drop():
    wizinv=[]
    with open(inv, 'r') as my_file:
        wizinv=my_file.readlines()
        lines=len(wizinv)
        if lines==0:
            print("Inventory Empty.")
            return

    for i in range(len(wizinv)):
        if wizinv[i]!='':
            print(i+1,". ",wizinv[i],sep="")
    
    dropped=int(input("Number: "))
    wizinv[dropped-1]=''
    
    with open(inv, 'w') as my_file:
        for i in range(len(wizinv)):
            item=wizinv[i]
            my_file.write(item)
    
if __name__=="__main__":
    main()
'''    


sales='monthly_sales.csv'
import csv

def main():
    print("Monthly Sales Program")
    menu()

def menu():
    print("COMMAND MENU")
    print("monthly - View monthly sales","yearly	- View yearly sumary","edit	- Edit sales for a month","exit	- Exit program",sep='\n')
    
    while True:
        saleList = []
        with open(sales) as my_file:
            reader = csv.reader(my_file, delimiter=',')
            for row in reader:
                saleList.append(row)
        
        choice=input()
        if choice.lower()=="monthly":
            monthly(saleList=saleList)
        elif choice.lower()=="yearly":
            yearly(saleList=saleList)
        elif choice.lower()=="edit":
            edit(saleList=saleList)
        else:
            exit()


def monthly(saleList):
    for i in range(12):
        for j in range(1):
            print(saleList[i][j],' - ',saleList[i][j+1])


def yearly(saleList):
    total=0
    average=0
    for i in range(12):
        total+=int(saleList[i][1])
    average=total/12
    print("COMMAND: YEARLY")
    print("Yearly Total: ",total,"\nMonthly Average: ",average)


def edit(saleList):
    print("COMMAND EDIT")
    choice=input("Three-letter Month (e.g. mar oct aug etc): ")
    for i in range(len(saleList)):
        if choice.lower()==saleList[i][0].lower():
            print(saleList[i][0],"Sales were",saleList[i][1])
            found=i
    Amount=input("Change to: ")
    saleList[found][1]=str(Amount)
    print("Sales amount for",saleList[i][0],"was modified to",saleList[found][1])
    
    with open(sales,'w+',newline='') as my_file:
        writer=csv.writer(my_file)
        writer.writerows(saleList)
                
    
    
if __name__=="__main__":
       main() 