"""Worldle"""

def solve():
    """solve the wordle"""
    answers = read_text()
    guess = 'raise'
    print("'x' represents a grey square\n'y' represents a yellow square\n'g' represents a green square\ne.g. 'xxYGx'")
    print("\nTry '{}'".format(guess))
    code = get_input()
    while code != 'ggggg':
        answers = reduce_answers(code, answers, guess)
        guess = best_guess(guess, code, answers)
        print("\nTry '{}'".format(guess))
        code = get_input()

def read_text():
    """read text files of answers and sorts, returning a list of valid answers"""
    f = open('C:/Users/user/OneDrive/Documents/wordle-answers-alphabetical.txt', 'r')
    answers_raw = f.readlines()
    f.close()
    answers_raw.sort()
    answers = []
    for answer in answers_raw:
        answer = answer.replace('\n','')
        answers.append(answer)
    return answers

def best_guess(guess, code, answers): # this needs optimizing
    """Takes a list of valid answers and chooses one that reduces the amount of valid answers by the most"""
    #gy_letters = []
    #for i, x in enumerate(code):
    #    if x == 'y' or x == 'g':
    #        gy_letters.append(guess[i])
    #results = []
    #for word1 in answers:
    #    for letter in gy_letters:
    #         word1 = word1.replace('letter','')
    #    shared_chars = 0
    #    for word2 in answers: 
    #        for char in word1:
    #            if word2.__contains__(char):
    #                shared_chars += 1
    #    results.append((word1, shared_chars))
    #results.sort(key = lambda x: x[1])
    ##print("There are {} valid words remaining.".format(len(results)))
    #if len(results) > 0:
    #    guess = results[-1][0]
    #else:
    #    print('Error, no words remaining')


    results = []
    for word1 in answers:
        elim_words = []
        for letter in word1:
            for word2 in answers:
                if not word2.__contains__(letter):
                    elim_words.append(word2)
        results.append((word1, len(elim_words)))
    results.sort(key = lambda x: x[1])
    if len(results) > 0:
        guess = results[-1][0]
    else:
        print('Error, no words remaining')        
    return guess

def get_input():
    """"Ask the user to input the result of the previous selection and returns it as a string"""
    code = input('Input code: ')
    return code

def reduce_answers(code, answers, guess):
    """Takes a code and a list of answers and filters answers by the code"""
    for i, x in enumerate(code):
        y_letters = []
        if x == 'y':
            letter = guess[i]
            for answer in answers:
                if not answer.__contains__(letter):
                    answers[answers.index(answer)] = '-----'
                    y_letters.append(letter)
    for i, x in enumerate(code): #ideally adapt this so grey letters don't count if if they are doubles of yellows
        if x == 'x':
            letter = guess[i]
            for answer in answers:
                if answer.__contains__(letter) and not y_letters.__contains__(letter):
                    answers[answers.index(answer)] = '-----'
    for i, x in enumerate(code):
        if x == 'g':
            letter = guess[i]
            for answer in answers:
                if answer[i] != letter:
                    answers[answers.index(answer)] = '-----'
    for i, x in enumerate(code):
        if x == 'y':
            letter = guess[i]
            for answer in answers:
                if answer[i] == letter:
                    answers[answers.index(answer)] = '-----'
    fixed = []
    for answer in answers:
        if answer != '-----':
            fixed.append(answer) 
    answers = fixed
    print(answers)

    return answers

solve()
