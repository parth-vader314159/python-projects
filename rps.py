import random    

print("lets play rock paper scissor")

user_inp = input("choose one - rock, paper, scissor")
print(f"you chose - {user_inp} ")

dict_rps = {
    1: "rock",
    2: "paper",
    3: "scissor"
    }

def inpt():
    agn = input()


rand_sel = random.choice(list((dict_rps.values()))) 
# use dict_name.values to show the value that is chosen
print(f"the computer chose -  {rand_sel}")

if user_inp == rand_sel:
    print("invalid")
elif (user_inp == "rock" and rand_sel == "scissors") or\
     (user_inp == "paper" and rand_sel == "rock") or\
     (user_inp == "scissor" and rand_sel == "paper"):
     print("you win!!")
else: print(" i win!!")

     
 
