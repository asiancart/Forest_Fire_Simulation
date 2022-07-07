import random , sys

QUESTIONS = [
    {'question': "How many times can you take 2 apples from a pile of 10 apples?", 'answer': "Once. Then you have a pile of 8 apples.",'accept': ['once', 'one', '1']},
    {'question': 'What begins with "e" and ends with "e" but only has one letter in it?','answer': "An envelope.",'accept': ['envelope']},
    {'question': "Is it possible to draw a square with three sides?",'answer': "Yes. All squares have three sides. They also have a fourth side.",'accept': ['yes']},
    {'question': "What does a towel get as it dries?",'answer': "Wet.",'accept': ['wet']},
    {'question': "Which letter of the alphabet makes honey?",'answer': "None. A bee is an insect, not a letter.",'accept': ['no', 'none', 'not']},
    {'question': "What kind of vehicle has four wheels and flies?",'answer': "An airplane.",'accept': ['airplane', 'plane']},
]

CORRECT_TEXT = ['Correct!', 'That is right.', "You're right.",'You got it.', 'Righto!']
INCORRECT_TEXT = ['Incorrect!', "Nope, that isn't it.", 'Nope.','Not quite.', 'You missed it.']

print('''Trick Questions, by asiancart''')
input('Press Enter to begin...')
random.shuffle(QUESTIONS)
score = 0

for questionNumber, qa in enumerate(QUESTIONS):
    print('\n' * 40)
    print('Question:', questionNumber + 1)
    print('Score:', score, '/', len(QUESTIONS))
    print('QUESTION:', qa['question'])
    response = input(' ANSWER: ').lower()

    if response == 'quit':
        print('Thanks for playing!')
        sys.exit()

    correct = False
    for acceptanceWord in qa['accept']:
        if acceptanceWord in response:
            correct = True

    if correct:
        text = random.choice(CORRECT_TEXT)
        print(text, qa['answer'])
        score += 1
    else:
        text = random.choice(INCORRECT_TEXT)
        print(text, 'The answer is:', qa['answer'])
    response = input('Press Enter for the next question...').lower()

    if response == 'quit':
        print('Thanks for playing!')
        sys.exit()

print("That's all the questions. Thanks for playing!")