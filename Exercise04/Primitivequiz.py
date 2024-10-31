#steps
#1 Put together an application that asks the user, "What is the capital of France?"after which you await their reply.
#2 The application should indicate that the message entered is accurate if they type the right response ("Paris").
#3 if the answer is wrong, it would print incorrect

#giving the variable question.
Answer = input("What is the capital of France?:")
if Answer =="Paris" : #selecting the answer of the question
    print("the answer is correct!") #if the answer in Paris then it is correct
else:
    print("the answer is wrong.") #answer is wrong should be written if it is anything other than Paris