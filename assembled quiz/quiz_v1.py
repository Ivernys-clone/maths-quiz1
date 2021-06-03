#The following program is a Mathematics Quiz worked in Python.
# This program is to challenge those who want to test their own skills in Math.
import random

#Define the function
def user_details(name):
    print("Hello", name,)
#Determine if the input only consists of string, if no ask user to input only letters
while True:
    name = input("Please Enter Your Name")
    if name.isalpha():
            break

    else:
        print("Please Enter Only Letters")


#Outputs the function
user_details(name)

#Define the function
def instructions():
    while True:
   
        inst = input("Would you like to read the instructions?\na)Yes\nb)no\nEnter here").upper()
   
        if inst == "YES" or inst == "Y" or inst == "A":
            print("""You will be given maths questions
Please answer them""")
            break
        if inst == "NO" or inst == "N" or inst == "" or inst == "B":
            break
        else:
            print("Please enter the options only")
      
#Outputs the function   
instructions()
#Asks user if they want to quit the Quiz
shutdown = input("Do you wish to play this quiz?  \nPress any key to continue \nEnter NO to exit quiz \nEnter here:").upper()

while True:  
    if shutdown == "NO" or shutdown == "N" :
        print("Okay, thank you for using the quiz")
        exit()
    else:
        break
def rounds():
            global num, total
            while True:
                        try:
                         
                                    num = int(input("Please enter the number of questions you would like to answer between 1-10: "))
                                    if 0<num<=10:
                                                break
                                    else:
                                                print("Please enter numbers 1-10 only")
                        except:
                                    print("Please enter numbers only")

            total = num
rounds()
#Sets score to 0
score=0
#initialises dictionary
questions = {}

#Maths questions are randomly generated with number betweem 0 and 10 
#(+, -, *) operators are chosen at random.
for i in range(num):
    int_a = random.randint(0,10)
    int_b = random.randint(0,10)
    operators = ['+','-','*']
    operator_value = random.choice(operators)
    question = str(int_a)+" "+operator_value+" "+str(int_b)
    answer = str(eval(question))
    question+=": "
   
    #adds the question to the dictionary of questions
    if not question in questions.keys():
      questions.update({question:answer})
    else:
      continue
   

#Iterates through the dictionary questions and response respectively
for q in questions.keys():
    user_answer=input(q)
    if questions.get(q)==user_answer:
        print("You got it right!")
        
        score+=1
    else:
        print("You got it wrong!")
#Outputs the users score and percentage
#str converts int to string
print("Your final score is "+str(score)+" out of "+str(total))
#Creates percentage
print("Thanks for playing")
##for k,v in questions.items():
##    print(k,v)
