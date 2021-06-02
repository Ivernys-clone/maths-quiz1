import random
    
def get_range():
        while True:
            
            num = input("\nPlease enter number of questions you would like to play:")
            print("Shows questions")
            try:
           
                num = int(num)
            except ValueError:
                print("=========================")
                print("Please Enter Only Numbers")
                print("=========================")
            else:
                break
    
        return num
num=get_range()


score=0

questions = {}


for i in range(num):
    int_a = random.randint(0,10)
    int_b = random.randint(0,10)
    operators = ['+','-','*']
    operator_value = random.choice(operators)
    question = str(int_a)+" "+operator_value+" "+str(int_b)
    answer = str(eval(question))
    question+=": "
   

    if not question in questions.keys():
      questions.update({question:answer})
    else:
      continue
   


for q in questions.keys():
    user_answer=input(q)
    if questions.get(q)==user_answer:
        print("\n*****************\nYou got it right!\n*****************\n")
        
        score+=1
    else:
        print("\n#################\nYou got it wrong!\n#################\n")

print("You got "+str(score)+" right!",float(score/len(questions))*100,"%")
