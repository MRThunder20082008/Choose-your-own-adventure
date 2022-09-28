Character = input ("What is your name? ")
print("welcome " +  Character)

q1 = input ("You are walking on a road and you see an old man. will you talk to him? write 'yes' or 'no' ")

if q1 == 'yes':
    op1 = input ("He says that a killer is on the loose and asks you if you can kill the killer? write 'yes ' to accept the quest or 'no' to decine ")
    if op1 == 'yes':
        op1q1 = input ("you have accepted and go to the market to get weapons. will you pick a 'sword' or 'ax'? ")
        print("you have picked the " + op1q1)
    elif op1 == 'no':
        print("the old man gets mad and kill you.")
        
elif q1 == 'no':
    op2_q1 = input ("you walk past him and reach a fork in the road. write 'left' to go left or 'right' to go right ")

else:
    print("you have not chosen anything and you die!")
    quit()