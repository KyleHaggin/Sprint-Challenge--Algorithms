'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"***
occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_helper(word, occurences, index):
    if index >= (len(word)-1):
        return occurences
    if word[index]+word[index+1] == 'th':
        occurences += 1
    index += 1
    return count_helper(word, occurences, index)


def count_th(word):

    # Initialize the index and holder variables
    index = 0
    occurences = 0
    occurences = count_helper(word, occurences, index)

    return occurences
