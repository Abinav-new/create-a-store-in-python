# let's create a store in python
print("Welcome to Abinav Store")
name = input("What is your name\n")
print("Hello " + name + ", thank you so much for coming today\n\n\n")
if name == "Ben" or name == "Patricia" or name == "Loki":
  evil_status = input("Are you evil?\n")
  good_deeds = int(input("How many good deeds you have done: \n"))
  if evil_status == "Yes" and good_deeds < 4:
    print("Get Out")
    exit()
  else:
    print("Hello " + name + ", thank you so much for coming today\n\n\n")
menu = "Pen, Pencil, Etc"
print(name + ", What Would you like on our menu today?, What do you want from we are have from our\n" + menu)
order = input()
print("Sounds good " + name + ", we'll have your item pack in a bag " + order)
price = int(input("Put a price value: \n"))
quantity = input("How many " + order + ", do you want: \n")
total = price * int(quantity)
print("Thank you your total is: ", total)
#that's it
