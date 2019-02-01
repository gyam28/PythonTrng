"hello world"
'this is a string'
# print("""
# gdsdsd
# gsfgsd
# fgdgfs""")

#participants =35
#string1 = "we have total {} participants" .format(participants)
#string2 = f"we have total {participants} participants"

#print(string2)

#howmuch = input("how much did you pay? ")

#print("Are you kidding?")
#answer = input(">>>")

#print(howmuch)
#print(answer)

#STRING methods
#split a string at a specific character or location
# print("this is a string".split(" "))

# replace a character
new_str = "Jacky-Chan-20".replace("-"," ")

#count how many times a value appears in the string

# print(new_str.count('a'))

#how long/how manu characters are there
length = len(new_str)
strip = new_str.strip()

# print(strip)

t = new_str.startswith('T')
# print(t)


#INDEXING

str = "hello ladies"
f = str[0]

# print(f)

g = str[-1]
# print(g)

#SLICING obs. the last range number will not be counted in the result, just the
#one before it eg. element no.6
# slice = [2:7]
# print(slice)

#integer int()
# float float()
# string str()
# boolean bool)

#BOOLEANS
# true and false are 1 and 0 in numeric terms
# true or false will give true

#boolean exercise
# 1. true
# 2. false
# 3.true

#non-primitive data types
#list, a collection of values,
list1 = [1,2,3,"text",2.0,True]
l = len(list1)
# print(l)

list1[5] = False
# print(list1)

#LIST METHODS
#appending
list1.append(35)
# print(list1)

#Pops, take out the last element of a list
list1.pop()
# print(list1)

#INSERTION inserts elements in specific order
list1.insert(3, 567)
# print(list1)

# #SLICING, takes a chunk of the list to print out
# slice = list1[2:6]
# # print(slice)
#
# # print(list1)
# bw = list1[::-1]
# # print(bw)
#
# #TUPPLE
# tup = (1,23,4)
# # tup[1] = "cool"
# # print(tup) cannot be changed on the content inside only if created a new one
#
# tupp = ("hello",1,2,4.5,True)
# tupp2 =(10,20,30,False,True)
# tupp3 = tupp + tupp2
# # print(tupp3)
# # print(20 in tupp3)
# #
#
# lst = ["Jacky Chan", "Chuck Norris", "Bruce Lee"]
# # for el in lst:
#     # print(el)

#DICTIONARY for every key there is a value, never duplicate keyword, value can duplicate
# dictionary = {
#     "key1": "value 1",
#     "Don": "cool",
#     "TheShortcut": "great",
#
# }
# dictionary['key3'] = "new value"
# print(dictionary)
# print(dictionary['key3'])
# dictionary['key1'] = "new value"
# print(dictionary)

#IF CONDITION

# guess_number = int(input("choose your number, please!"))
# print(guess_number)
# right_answer = 3
#
# if guess_number == right_answer:
#     print("super! you're right!")
# else:
#     print("No, wrong answer!")

#ELSE IF STATEMENT like IF statement but has more conditions to check

# guess_number = int(input("choose your number, please!"))
# print(guess_number)
# right_answer = 3
#
# if guess_number == 1:
#     print("no,no, higher!")
# elif guess_number == 2:
#     print("No, almost there!")
# elif guess_number == right_answer:
#     print("yay!right answer!")
# else:
#     print("nooo, wrong again...")

#LOOPS blocks of code that keep repeating themself until certain conditions
 # are or not met

# count = 0
# while count < 10 and count > = 0:
#         print(count)
#         count += 1 #count = count +1 or if count -= 1 is count - 1
#
# print("done!")
# #control + C stops any operation
#
# count = 10
# while True:
#     if count == 0
#     break
# print("done!")

#FOR loop for an element in smth insert or do smth

for a in "Hello":
    print(a.upper())

the_list = [1,2,34,6]
for a in the_list :
    if a in the_list[0:3]:
    print(a)
else:
    print("naaah")
