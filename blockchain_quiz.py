import time

print("Welcome to my blockchain quiz!")
time.sleep(1)

playing = input("Do you want to play? (yes/no) ")
time.sleep(1)

if playing.lower() != "yes":
    quit()

print("Okay! Let's play")
time.sleep(1)
score = 0

print("Question number 1.")
time.sleep(2)

answer = input("Who was the creator of Bitcoin? ")
if answer.lower() == "satoshi nakamoto":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Question number 2.")
time.sleep(2)

answer = input("Which consensus mechanism does Ethereum use? ")
if answer.lower() == "proof of stake":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Question number 3.")
time.sleep(2)

answer = input("What does dApp stand for? ")
if answer.lower() == "decentralised app":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Question number 4.")
time.sleep(2)

answer = input("In which year did FTX collapse? ")
if answer.lower() == "2022":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")