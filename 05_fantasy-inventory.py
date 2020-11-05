###################################################################
#File Name: 05_fantasy-inventory.py
#Author: Joseph Feldmeyer
#Email: joseph.k.feldmeyer@gmail.com
#Creation Date: 2020-11-05

#Description:  Create two functions: 
#               1. displayInventory() - takes in a dictionary of 
#               item:itemcounts and prints all items in following 
#               format: 
#               itemcount item ... 
#               Total number of items: total 
#
#               2. addToInventory() - takes in a inventory dict 
#               and a list of loot, and adds the loot to the inv. 

###################################################################

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory): 
    print("Iventory: ") 
    item_total = 0
    for k, v in inventory.items(): 
        print(str(v) + ' ' + k) 
        item_total += v 
    print("Total number of items: " + str(item_total) ) 

displayInventory(stuff) 


def addToInventory(inventory, addedItems): 
    for item in addedItems: 
        inventory.setdefault(item, 0) 
        inventory[item] += 1
    return(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
