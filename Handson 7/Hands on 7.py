'''
def main():
    print("Tip calculator")
    while True:
        try:
            bill=float(input("Cost of meal: "))
            if bill<=0:
                print("Must be greater than 0")
                continue
            break
        except ValueError:
            print("Must be a valid decimal number")

    while True:
        try:
            tip=int(input("Tip Percentage: "))
            if tip<0:
                print("Must not be less than 0%")
                continue
            break
        except ValueError:
            print("Must be a valid integer")

    print("Cost of meal:",bill)
    print("Tip percentage:",tip,"%",sep='')
    print("tip amount:",(bill*(tip/100)))
    print("Total final bill:",(bill+(bill*(tip/100))))

if __name__=="__main__":
    main()




'''
inv = "wizard_inventory.txt"
all_item = "wizard_all_items.txt"
import sys
import random

def main():
    print("The Wizard Inventroy Program")
    print("COMMAND MENU")
    print("walk - Walk down the path","show - Show all items","drop - Drop an item","exit - Exit program",sep="\n")
    
    while True:
        try:
            choice = input()
            if choice.lower()!="walk" and choice.lower()!="drop" and choice.lower()!="show" and choice.lower()!="exit":
                print("Invalid Response, try again")
                continue
            if choice.lower()=="walk":
                walk()
            elif choice.lower()=="show":
                show()
            elif choice.lower()=="drop":
                drop()
            else:
                sys.exit()
        except ValueError:
            print("Invalid Response")

    

def walk():
    loot=[]
    
    while True:
        try:
            with open(all_item, 'r') as my_file:
                loot=my_file.readlines()
            break
        except FileNotFoundError:
            print("Could not find items file.\nExiting program. Bye!")
            sys.exit()
    
        
    
    drops=random.randrange(9)
    print("Command: walk")
    print("While walking down a path, you see ",loot[drops],". Do you want to grab it? (y/n):",sep='')
    
    while True:
        try:
            choice=input()
            if choice.upper() !='Y' and choice.upper()!='N':
                print("Invalid Response, try again")
                continue
            break
        except ValueError:
            print("Invalid response")
    

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
    try:
        with open(inv, 'r') as my_file:
            print(my_file.read())
    except FileNotFoundError:
        print("You have no inventory file, wizard will start with empty inventory")
        with open(inv, 'w') as my_file:
            my_file.write("")
    
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
                
    while True:
        try:
            dropped=int(input("Number: "))
            if len(wizinv)<(dropped-1):
                print("Invalid Response, try again")
                continue
            break
        except ValueError:
            print("Value incorrect, try again")
        
    wizinv[dropped-1]=''
    
    with open(inv, 'w') as my_file:
        for i in range(len(wizinv)):
            item=wizinv[i]
            my_file.write(item)
    
if __name__=="__main__":
    main()
    