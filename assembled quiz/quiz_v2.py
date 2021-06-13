#The following program is a Mathematics Quiz worked in Python
# This program is to challenge those who want to test their own skills in Math
#imports random module
import random
print("**************************\nWelcome to Jims maths quiz\n**************************")

#using funtions to ask for name and .isalpha to catch errors
def user_details(name): #using def to be able to call the function many times easily
    print("Hello", name,) # greeting user
while True: #starting a loop
    name = input("Please enter your first name : ").capitalize() #asking name.
    if name.isalpha(): # .isalpha to trap errors
            break # breaking the loop

    else:
        print("=========================")
        print("Please enter only letters")
        print("=========================")

#Outputs the function
user_details(name)

#Asking if they want to know the quiz rules
def instructions():
    while True:
   
        inst = input("Would you like to read the instructions?\na)Yes\nb)no\nEnter here: ").upper()
   
        if inst == "YES" or inst == "Y" or inst == "A":
            print("""The instructions are simple you will be given a random generated maths quiz
Read the question and answer it.
Example: 1+1:  <--Put your answer here
Answer:  Example: 1+1: 2 <--Put your answer here
You can choose the number of rounds you would like to play.
You will be prompted to enter a number of questions you want to play.
""")
            break
        if inst == "NO" or inst == "N" or inst == "" or inst == "B":
            break
        else:
            print("=============================\nPlease enter the options only\n=============================")
      
#Outputs the function   
instructions()
#Asks user if they want to quit the Quiz

def status(): 
  while True: #Starting a loop
    shutdown = input("\nDo you wish to play this quiz?  \na)Yes\nb)no\nEnter here:").upper()
    if shutdown == "YES" or shutdown == "Y" or shutdown == "A" or shutdown == "":
      break
    else:
        print("\nThank you please play the quiz again")
        exit()
status()
        
def rounds():
            global num, total
            while True:
                        try:
                         
                                    num = int(input("\nPlease enter the number of questions you would like to answer between 1-10: "))
                                    if 0<num<=10: #not allowing less than 1 and more than 10
                                                break
                                    else:
                                                print("\n==============================\nPlease enter numbers 1-10 only\n==============================")
                        except:
                                    print("\n=========================\nPlease enter numbers only\n=========================")

            total = num
rounds()

print("\nNote: If you ever want to leave the quiz enter xxx\n")
#Sets score to 0
score=0
#Initialises dictionary
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
   
    #adds questions to the dictionary
    if not question in questions.keys():
      questions.update({question:answer})
    else:
      continue
   

#Checks if the answer is right or wrong
for q in questions.keys():
    user_answer=input(q)
    if questions.get(q)==user_answer:
        print("\n*****************\nYou got it right!\n*****************\n")
        
        score+=1
    else:
        print("\n#################\nYou got it wrong!\n#################\n")
#Outputs the users score and percentage
print("\n**************************************************\n")
print("Thank you for using Jim's maths quiz")
#str converts int to string
print("Your final score is "+str(score)+" out of "+str(total))
#Creates percentage
print(name+" you scored",round((score/total)*100),"%")
print("""If there was anything to your disliking or something you would like to change 
please contact me at 19180@students.mrgs.school.nz""")
print("Thanks for playing")
##for k,v in questions.items():
##    print(k,v)
