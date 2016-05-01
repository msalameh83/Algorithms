__author__ = 'Mohammad'

def word_break_problem(string, dictionary):
    # -1 indicates string between i to j cannot be split
    chart = [[-1]* len(string) for i in range(len(string))]

    # fill up the matrix in bottom up manner
    for span in range(1, len(string)+1):
        for i in range(len(string) - span + 1):
            j = i + span - 1
            # if string between i to j is in dictionary T[i][j] is true
            if string[i:j + 1] in dictionary:
                chart[i][j] = i
                continue
            # find a k between i+1 to j such that T[i][k-1] && T[k][j] are both true
            for k in range(i + 1, j + 1):
                if chart[i][k - 1] != -1 and chart[k][j] != -1:
                    chart[i][j] = k-1
                    break
    for i in chart: print (i)

    # BELOW NOT WORKING
    # create space separate word from string is possible
    words = []
    i = 0
    j = len(string) -1
    while  i < j:
        k = chart[i][j]
        if i == k:
            words.append(string[i:j + 1])
            break
        words.append(string[i:k+1])
        i = k

    print (words)



string = 'iamace'
dictionary = ['i', 'a', 'am', 'ace']
word_break_problem(string, dictionary)
