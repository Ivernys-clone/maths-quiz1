
   
   
inst = input("Would you like to read the instructions?\na)Yes\nb)no\nEnter here: ").upper()
   
if inst == "YES" or inst == "Y" or inst == "A":
    print("""The instructions are simple you will be given a random generated maths quiz
Read the question and answer it.
Example: 1+1:  <--Put your answer here
Answer:  Example: 1+1: 2 <--Put your answer here
You can choose the number of rounds you would like to play.
You will be promted to enter a number of questions you want to play.""")

elif inst == "NO" or inst == "N" or inst == "" or inst == "B":
    print("Continues")
