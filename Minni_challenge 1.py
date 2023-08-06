
#Mini Challenge 1
#Write a code that takes in 2 lists x = [-1 -4 -7] and y = [-3 7 4] and calculates the absolute sum

def my_function():
    x=[-1,-4,-7]
    y=[-3,7,4]
    z=sum(x+y)
    return z

print(my_function())

#Mini Challenge 2
#Write a code that takes in two inputs (number of items bought and prices) from the user and calculate the total account balance
def total_():
    items=input("How many items did you buy?")
    items=int()
    input_prices=input("What are the prices of those items(NOTE: use space to separate the prices)  ").split()
    prices=[int(item) for item in input_prices]
    print(prices)
    return sum(prices)

total_()
#
# print(total_())

#Mini challenge 3
#Repeat mini challenge 2 (Write a code that takes in two inputs from the user and calculates the total) using lambda expressions insteadit
total= lambda x= input('how many items did you buy'), y= input('what are the prices os those items(NOTE: use space to separate the prices)').split : [int(item) for item in y]
total

#Mini challenge 4
cubic_value=lambda x:x/3
cubic_value(8)

my_list= list(range(-10, 11))
print(my_list)
generator1 = list(map ( lambda x:x**2 , my_list))
generator1

#Mini challenge5
#Write a code from the user that takes in a range (upper and lower bounds) and returns a list of positive and even numbers only
my_list2= list(range(-6, 8))
print(my_list2)

evenandpositive = list(  filter(lambda x: (x>=1) , my_list2) )

