#!/usr/bin/env python
# coding: utf-8

# In[ ]:


expenses=[{'name': "dinner", 'cost':100, 'date':r"20/4/2023"}]


# In[8]:



print("What do you want to do? -\n"
        "1. Add\n" 
        "2. Remove")
option = input()
def find_index_item(myTempList, item_name):
    result = -1
    length = len(myTempList)
    for i in range(length):
        if myTempList[i]['name'] == item_name:
            result = i
    return result
def remove_item(myTempList, item_name):
    if find_index_item(myTempList, item_name) > -1:
        del myTempList[find_index_item(myTempList, item_name)]
    else:
        print(item_name + " not in list")
def add_item(myTempList, item):    
    myTempList.append(item)
if option == '1':
    name_input = input("Item name: ")
    cost_input = int(input("Item cost: "))
    date_input = input("Date: ")
    item = {'name': name_input, 'cost':cost_input, 'date':date_input}
    add_item(expenses, item)
    print("Your expenses: ", expenses)
elif option == '2':
    name_input = input("Item name: ")
    remove_item(expenses, name_input)
    print("Your expenses: ", expenses)
else:
    print("Invalid input")


# In[ ]:




