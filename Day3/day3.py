# web1 = "facebook"
# acc1 = "theshortcut"
# pass1 = "1234"
#
# web2 = "Twitter"
# acc2 = "thelogcut"
# pass2 = "4342"
#
# ctn = True
# while ctn:
#
#     print("what website acc and passw do you wanna see? choose a number.")
#     print("1. facebook")
#     print("2. theshortcut")
#     answer1 = int(input(">> "))
#
#     if answer1 == 1:
#         print("This is your facebook account: {}" .format(acc1))
#         print("This is your facebook password: {}" .format(pass1))
#
#     elif answer1 == 2:
#         print("This is your Twitter account: {}" .format(acc2))
#         print("This is your Twitter password: {}" .format(pass2))
#     else:
#         print("There is no such thing, please retry.")
#
#
#     wish = input("do you wish to continue? Y/N")
#     # if wish == "Y"
#     if wish.lower() == 'yes' or wish.lower() == 'y'
#     ctn = True
#     elif wish.lower() == "no" or wish.lower( == 'n')
#         print("bye bye")
#         break
#     else:
#         print("what do you mean?")
#         wish = input("do you wish to continue?Y/N")
#         ctn = False
        break

        # FUNCTIONS a group of codes put together to do smth noted def+name


def sum(first,second):
    result = first + second
    return result

r1 = sum(1,2)
r2 = sum(3,5)
r3 = sum(199,456)

print(r1, r2, r3)

# can be also empty function written def sum() always wth space inside ()

def say_hi():
    print("hello friend!")

say_hi()

def say_hello(*args):  #for when you do not know how many items are in list use (*args)
    for arg in args:
        print(f"hello, {arg}")

say_hello("Daniel","Kim","A","B")

#
def say_hello(*args, **kwargs): # * for arg and ** for key word args
    print(args) #data is shown as tuple to make sure data is not changed
    print(kwargs) #format dictionary because kwargs is key word arguments

say_hello("Daniel","Kim", age = 20, height = 180)

tup1 = (
    {"key1":"val1"},
    {"key2":"val2"}
    )

print(type(tup1))
print(tup1[0])
print()
print(type(tup1[0]))

tup1[0]["key3"] = "val3"

print(tup1[0])

#UNPACKAGING, READ AND WRITE FILES

from sys import argv

script, first_val, second_val, third_val = argv

print("the first argument is {}".format(first_val))
print("the second argument is {}".format(second_val))
print("the third argument is {}".format(third_val))
print("you are running the script {}".format(script))
#
#here is used multiple assignment, more variab at the same time assign

from sys import argv

script, user_name = argv

prompt = "> "

print("Hi {}, I'm the {} script".format(user_name,script))
print("I'd like to ask you a question")
print("Do you like me, {}".format(user_name))
likes = input(prompt)

print("thanks, I {} like you too".format(likes))


from sys import argv

script, filename = argv

txt_file = open(filename) #open is function

print("here is your file name: {}".format(filename))
print("here is the content inside of it")
print(txt_file.read()) #read is method,same is close .close .read
txt_file.close()

from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print("if you dont want to do that, press Ctrl + C")
print("or press enter if you wanna continue")

input("?")

print("opening the file....")
target = open(filename, "w")
print("Truncating the file now. Goodbye!")
target.truncate()

print("now im going to ask you 3 lines")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write this into your file")

# target.write(line1) #has alternative in one single line written underneath
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')

target.write(f"{line1}\n{line2}\n{line3}\n")

print("done!")
target.close()
