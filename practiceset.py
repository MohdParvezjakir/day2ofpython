#problem01:Write a python program to display a user entered name followed by Good Afternoon using input () function. 
name = input("Enter your name:")
print(f"good afternoon, {name}")



#problem02:  Write a program to fill in a letter template given below with name and date
latter = """<name>
congratulation you are selected!
<date>
"""
a = input("Enter your name:")
b = input("Date")
c = latter.replace("<name>",f"{a}").replace("<date>",f"{b}") #to replace name and date from user input
print(c)


# write a programe to  find double space in a strings
str = "there is a duoble  space in this strings"
print(str.find("  "))

