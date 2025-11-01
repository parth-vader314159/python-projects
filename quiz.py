print("welcome to my quiz game")

appr = input("do you want to play the game")

if appr.lower() == "yes":
  print("lets begin :)")
elif appr.lower() == "no":
  print(":(")
else:
  print(">:(")

score = 0

# question 1
answer = input("what is the full form of cpu")
if answer.lower() == "central processing unit":
  print("correct")
  score =+ 4
elif answer.lower() != "central processing unit":
  print("incorrect")
  score -= 1
else : print("unanswered")

# question 2
answer = input("what does RAM store - temporary or permamnt data")
if answer.lower() == "temporary":
  print("correct")
  score =+ 4
elif answer.lower() != "temporary":
  print("incorrect")
  score -= 1
else : print("unanswered")

# question 3
answer = input("what is the brain of computer called")
if answer.lower() == "central processing unit":
  print("correct")
  score =+ 4
elif answer.lower() != "central processing unit":
  print("incorrect")
  score -= 1
else : print("unanswered")

# question 4
answer = input("what language does a computer understand")
if answer.lower() == "binary":
  print("correct")
  score =+ 4
elif answer.lower() != "binary":
  print("incorrect")
  score -= 1
else : print("unanswered")

# question 5
answer = input("what does www stand for")
if answer.lower() == "world wide web":
  print("correct")
  score =+ 4
elif answer.lower() != "world wide web":
  print("incorrect")
  score -= 1
else : print("unanswered")

# question 6
answer = input("who founded microsoft")
if answer.lower() == "bill gates":
  print("correct")
  score =+ 4
elif answer.lower() != "bill gates":
  print("incorrect")
  score -= 1
else : print("unanswered")

# question 7
answer = input("what device is used to print")
if answer.lower() == "printer":
  print("correct")
  score =+ 4
elif answer.lower() != "printer":
  print("incorrect")
  score -= 1
else : print("unanswered")

# question 8
answer = input("what type of memory is non volatile")
if answer.lower() == "rom":
  print("correct")
  score =+ 4
elif answer.lower() != "rom":
  print("incorrect")
  score -= 1
else : print("unanswered")

# question 9
answer = input("what keuy is used to delete characters on the left to the cursor")
if answer.lower() == "backspace":
  print("correct")
  score =+ 4
elif answer.lower() != "backspace":
  print("incorrect")
  score -= 1
else : print("unanswered")

# question 10
answer = input("whawt part of the computer is sued to show output visually")
if answer.lower() == "display":
  print("correct")
  score =+ 4
elif answer.lower() != "display":
  print("incorrect")
  score -= 1
else : print("unanswered")



print(score)

print ("thanl you for attempting the quiz")