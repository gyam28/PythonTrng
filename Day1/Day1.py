print("hello world")
#this will not appear when executed
print("hello")
print(' hi ')
print("2 + 2")
print(2+2)

#variables
daniel = "Handsome"
print(daniel)
print("this guy is",daniel)

apple = 10
orange = 15
basket = apple + orange
bill = basket * 10

print("we've bought",apple,"apples")
#text names integer value
print("you've also bought",orange,"oranges")
#text names integer value
print("your basket is now {} fruits in it".format(basket))
# basket now has sum with {} of integers - string formatting to read!!!
print("you have to pay %d Dollars" %bill)
# the bill variable is the total of basket * 10
# .method is format for methods

print("we have {apple} apples")
print("we have{0} apple, and {1}".format(apple, orange))
