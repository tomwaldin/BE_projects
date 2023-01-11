"""Worldle"""

import numpy as np

def read_text():
    """read text files of answers, combine them and sort"""
    f = open('C:/Users/user/OneDrive/Documents/wordle-allowed-guesses.txt', 'r')
    g = open('C:/Users/user/OneDrive/Documents/wordle-answers-alphabetical.txt', 'r')
    guessesn = f.readlines()
    answersn = g.readlines()
    f.close()
    g.close()
    all_wordsn = guessesn + answersn
    all_wordsn.sort()
    all_words = []
    for word in all_wordsn:
        word = word.replace('\n','')
        all_words.append(word)
    answers = []
    for word in answersn:
        word = word.replace('\n','')
        answers.append(word)
    return all_words, answers

def solve(all_words, answers):
    """solve the Wordle"""
    print("'x' represents a grey square\n'Y' represents a yellow square\n'G' represents a green square\ne.g. 'xxYGx'")
    print("\nTry 'raise'")
    yarray = get_input()
    ylist = []
    xlist = []
    chars = list('raise')
    for i, char in enumerate(chars):
        if int(yarray[i]) == 1:
            ylist.append(char)
        elif int(yarray[i]) == 0:
            xlist.append(char)

    valid_answers = []
    for word1 in answers:
        contains_y = False
        contains_x = False
        for y in ylist:
            if word1.__contains__(y):
                contains_y = True
        for x in xlist:
            if word1.__contains__(x):
                contains_x = True
        if contains_y and not contains_x:
            valid_answers.append(word1) 

    guesses = []
    for word1 in all_words:
        contains_x_or_y = False
        for y in ylist:
            if word1.__contains__(y):
                contains_x_or_y = True
        for x in xlist:
            if word1.__contains__(x):
                contains_x_or_y = True
        if not contains_x_or_y:
            guesses.append(word1) 

    
    result_list = []
    for word1 in guesses:
        elim_count = 0
        chars = list(word1)
        for word2 in valid_answers:
            contains_char = False    
            for char in chars:
                if word2.__contains__(char):
                    contains_char = True
            if not contains_char:
                elim_count += 1
        result_list.append((word1, elim_count))
    result_list.sort(key = lambda x: x[1])
    print(len(result_list))
    print("\nTry '{}'".format(result_list[0][0]))


    #guess2
    yarray = get_input()
    ylist = []
    xlist = []
    chars = list(result_list[0][0])
    for i, char in enumerate(chars):
        if int(yarray[i]) == 1:
            ylist.append(char)
        elif int(yarray[i]) == 0:
            xlist.append(char)

    valid_answers2 = []
    for word1 in valid_answers:
        contains_y = False
        contains_x = False
        for y in ylist:
            if word1.__contains__(y):
                contains_y = True
        for x in xlist:
            if word1.__contains__(x):
                contains_x = True
        if contains_y and not contains_x:
            valid_answers2.append(word1) 

    guesses2 = []
    for word1 in guesses:
        contains_x_or_y = False
        for y in ylist:
            if word1.__contains__(y):
                contains_x_or_y = True
        for x in xlist:
            if word1.__contains__(x):
                contains_x_or_y = True
        if not contains_x_or_y:
            guesses2.append(word1) 

    
    result_list = []
    for word1 in guesses2:
        elim_count = 0
        chars = list(word1)
        for word2 in valid_answers2:
            contains_char = False    
            for char in chars:
                if word2.__contains__(char):
                    contains_char = True
            if not contains_char:
                elim_count += 1
        result_list.append((word1, elim_count))
    result_list.sort(key = lambda x: x[1])
    print(len(result_list))
    print("\nTry '{}'".format(result_list[0][0]))


#guess3
    yarray = get_input()
    ylist = []
    xlist = []
    chars = list(result_list[0][0])
    for i, char in enumerate(chars):
        if int(yarray[i]) == 1:
            ylist.append(char)
        elif int(yarray[i]) == 0:
            xlist.append(char)

    valid_answers3 = []
    for word1 in valid_answers2:
        contains_y = False
        contains_x = False
        for y in ylist:
            if word1.__contains__(y):
                contains_y = True
        for x in xlist:
            if word1.__contains__(x):
                contains_x = True
        if contains_y and not contains_x:
            valid_answers3.append(word1) 

    guesses3 = []
    for word1 in guesses2:
        contains_x_or_y = False
        for y in ylist:
            if word1.__contains__(y):
                contains_x_or_y = True
        for x in xlist:
            if word1.__contains__(x):
                contains_x_or_y = True
        if not contains_x_or_y:
            guesses3.append(word1) 

    
    result_list = []
    for word1 in guesses3:
        elim_count = 0
        chars = list(word1)
        for word2 in valid_answers3:
            contains_char = False    
            for char in chars:
                if word2.__contains__(char):
                    contains_char = True
            if not contains_char:
                elim_count += 1
        result_list.append((word1, elim_count))
    result_list.sort(key = lambda x: x[1])
    print(len(result_list))
    print("\nTry '{}'".format(result_list[0][0]))



    
def get_input():
    """converts user input into usable arrays"""
    userin = input('Input code: ')
    code = list(userin)
    yarray = np.zeros(5)
    for i, c in enumerate(code):
        if c == 'Y':
            yarray[i] = 1
        if c == 'G':
            yarray[i] = 1
    return yarray

def main():
    all_words, answers = read_text()
    solve(all_words, answers)

main()

 #fgfhgf


    print(len(answers))
    g_answers = []
    for i, x in enumerate(code):
        if x == 'G':
            letter = guess[i]
            for answer in answers:
                if answer[i] == letter:
                    g_answers.append(answer)            
    y_answers = []
    for i, x in enumerate(code):              
        if x == 'Y':
            letter = guess[i]
            for answer in answers:
                if answer.__contains__(letter):
                    y_answers.append(answer)
    if len(g_answers) > 0 and len(y_answers) > 0:
        answers = list(set(g_answers) & set(y_answers))
    else:
        answers = g_answers + y_answers
    
    for i, x in enumerate(code):
        if x == 'x':
            letter = guess[i]
            for answer in answers:
                if answer.__contains__(letter):
                    answers.remove(answer)