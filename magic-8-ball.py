import random

# Answer List
answers = ["My sources can confirm it", "It is decidedly so", "As I see it, Yes", "Signs point to yes", "Yes", "No", "You may not rely on it", "My sources say no", "My reply is no", "Don't count on it", "Reply not clear", "Concentrate and ask again", "404 answer not found", "I'm having dinner, ask later", "Reply hazy"]

def Magic8Ball(): # Function for printing the answers for question
    print('Ask me a question: ↓')
    input()
    print("Answer ↓")
    print (answers[random.randint(0, len(answers))] ) # from answers list, pick a random number between 0 and length of the answers list, and print the corresponding answer to the number
    print("Answer ↑")
    print('I hope that helped!')
    Replay()

def Replay(): # Asks user for replay...
    # ambiguous part ↓
    print ('Do you have another question? [Y/N] ')
    reply = input()
    reply = reply.upper()
    if reply == 'Y':
        Magic8Ball()
    elif reply == 'N':
        exit()
    else:
        print('My apologies, I did not catch that. Please repeat.')
        Replay()

Magic8Ball()
