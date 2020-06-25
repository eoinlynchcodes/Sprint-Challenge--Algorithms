'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    search = 'th'
    n1 = len(word)
    n2 = len(search)

    if (n1 == 0 or n1 < n2):
        return 0

    if (word[0: n2] == search):
        return count_th(word[1:]) + 1

    return count_th(word[n2 - 1:])