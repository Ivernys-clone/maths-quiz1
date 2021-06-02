def user_details(name):
    print("Hello", name,)
#Determine if the input only consists of string, if no ask user to input only letters
while True:
    name = input("Please Enter Your Name : ").capitalize()
    if name.isalpha():
        break

    else:
        print("=========================")
        print("Please Enter Only Letters")
        print("=========================")

#Outputs the function
user_details(name)

'''This is my next change for asking user details
in the previous program the name accepted numbers
and age and yearlevel accepted string. I will create
proper datatypes so that name will accepts only strings
and age and yearlevel wil only accept numbers. I have also
used a function so that I don't have to write it over and over again.
I have also used .upper() so that the name is capatalized.
I have also made adjustments to the general U.I'''
