#make a magic 8 ball
import random
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

print('hello, I am the Magic 8 Ball, what is your name?')
name = input()
print('hello ' + name)


def Magic8Ball():
    print('I am very wise. Ask me a question.')
    input()
    print (answers[random.randint(0, len(answers)-1)] )
    Replay()
    

def Replay():
    print ('I hope that was helpful, do you have another question?')
    reply = input()
    if reply == 'Yes':
        Magic8Ball()
    else:
        print('thank you for talking to me')
        exit()

Magic8Ball()
