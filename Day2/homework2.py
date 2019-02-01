website = ["Facebook", "Gmail", "Twitter"]
accountName = ["myacc@gmail.com", "myawesomeacc@yahoo.com", "myoldacc@aol.com"]
password = ["1n2fd3ef4", "ds1dc1cd1cs1", "fds1cdsc2cd3"]

active = True

while active:
    key = 1
    for names in website:
        print(f"{key} {names}")
        key = key + 1

    choice = int(input("what website's password do you want to see?\n"))


    if choice == 1:
        print("\nWebsite 1.", website[0], "\nAccount name: ", accountName[0],"\npassword: ",password[0])
    elif choice == 2:
        print("\nWebsite 2.", website[1],"\nAccount name: ", accountName[1],"\npassword: ",password[1])
    else:
        print("\nWebsite 3.", website[2],"\nAccount name: ", accountName[2],"\npassword: ",password[2])

    choice2 = input("\nDo you want to continue? Y/N\n")

    if choice2 == "Y" or choice2 == "Yes" or choice2 =="yes" or choice2 =="YES" or choice2 =="y":
        active = True
    elif choice2 == "N" or choice2 =="No" or choice2 =="no" or choice2 =="NO" or choice2 =="n":
        active = False
