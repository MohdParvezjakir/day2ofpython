#problem01: create a list of seven fruit name using user input
list = [] # create a empty list
f1 =input("Enter fruit name:")
list.append(f1) #to append the given input by user
f2 =input("Enter fruit name:")
list.append(f2)
f3 =input("Enter fruit name:")
list.append(f3)
f4 =input("Enter fruit name:")
list.append(f4)
f5 =input("Enter fruit name:")
list.append(f5)
f6 =input("Enter fruit name:")
list.append(f6)
f7 =input("Enter fruit name:")
list.append(f7)
print(input(f"your fruitname is\n{list}"))

#problem02: exept the marks from 6 student and print them in sorted manner
list2 = []
n1 =int(input("Enter your number:"))
list2.append(n1)
n2 =int(input("Enter your number:"))
list2.append(n2)
n3 =int(input("Enter your number:"))
list2.append(n3)
n4 =int(input("Enter your number:"))
list2.append(n4)
n5 =int(input("Enter your number:"))
list2.append(n5)
n6 =int(input("Enter your number:"))
list2.append(n6)
list2.sort()
print(list2)



#check that a tuple type can be change in python

tuple = (1,2.55,"parvez")
tuple[3]= "mohd" # it's give a error that means is tuple is immutable


# write a program to sum a list which contain minimum 4 number
list3 = [1,2,3,4]
print(sum(list3))
#count the zero  umber in folowing tuple
_a = (0,6,7,0,6,0)
print(_a.count(0)) # output is three