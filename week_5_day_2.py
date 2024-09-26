#  collection = single "variable" used to store multiple values
#  lists = [] ordered and changeable. Duplicates OK
#  Set = {} unordered a immutable, but Add/Remove OK. NO duplicates
#  Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["Apple", "orange", "banana", "coconut","starwberry","watermelon"]

# print(dir(fruits)) #gives what we can do with the variable (attributes) 
# print(help(fruits)) #helpful information about function
# print(len(fruits)) #gives you the length
# print(fruits[::-1]) #makes backwards
# print(fruits[::2]) #every second fruit

for fruit in fruits:
    print(fruit) 

fruits.append("pineapple") #adds a word to the end of the list
fruits.remove("apple") # removes a word
fruits.insert(0,"pineapple") #inserts
fruits.sort() #puts everything in alphabetical order
fruits.reverse() #reverses list
fruits.clear() #clears everything
print(fruits.index("apple"))

fruits[0] = "pineapple" #reassign values