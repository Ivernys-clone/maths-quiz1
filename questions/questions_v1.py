import random


def get_range():
    while True:
        try:
            num=int(input("Please enter number of questions you would like to play:"))
            if num == integer:
                break
            else:
                print("Please enter a valid input")
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
        print("Correct!")
        score+=1
    else:
        print("You're Wrong!")

print("You got "+str(score)+" right!")
