list1 = ['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
list2 = ['X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K']


def checker(x, y, z):
    if x == 1:
        if len(y) > 9 or len(z) > 4:
            print('PLEASE ENSURE INFO IS CORRECT')
        else:
            if y[0] == 'T' and z[0] == '2' and z[1] == '0':
                if y[1] == z[2] and y[2] == z[3]:
                    d = int(y[1]) * 2 + int(y[2]) * 7 + int(y[3]) * 6 + int(y[4]) * 5 + int(y[5]) * 4 + int(y[6]) * 3 +\
                        int(y[7]) * 2 + 4
                    e = d % 11
                    if y[8] == list1[e]:
                        print('THIS IS A VALID IC')
                    else:
                        print('PLEASE ENSURE THAT INFO IS CORRECT')
                else:
                    print('PLEASE ENSURE THAT INFO IS CORRECT')
            elif y[0] == 'S' and z[0] == '1' and z[1] == '9':
                if int(z[2]) < 7:
                    print('PLEASE ENSURE INFO IS CORRECT')
                else:
                    if y[1] == z[2] and y[2] == z[3]:
                        f = int(y[1])*2 + int(y[2])*7 + int(y[3])*6 + int(y[4])*5 + int(y[5])*4 + int(y[6]*3) +\
                        int(y[7])*2
                        g = int(f % 11)
                        if int(y[8]) == list1[g]:
                            print('THIS IS A VALID IC')
                        else:
                            print('PLEASE ENSURE THAT INFO IS CORRECT')
                    else:
                        print('PLEASE ENSURE THAT THIS INFO IS CORRECT')
            else:
                print('PLEASE ENSURE INFO IS CORRECT')
    elif x == 2:
        if len(y) > 9 or len(z) > 4:
            print('PLEASE ENSURE INFO IS CORRECT')
        else:
            if y[0] == 'G' and z[0] == '2' and z[1] == '0':
                if y[1] == z[2] and y[2] == z[3]:
                    h = int(y[1]) * 2 + int(y[2]) * 7 + int(y[3]) * 6 + int(y[4]) * 5 + int(y[5]) * 4 + int(y[6]) * 3 +\
                        int(y[7]) * 2 + 4
                    i = h % 11
                    if y[8] == list2[i]:
                        print('THIS IS A VALID IC')
                    else:
                        print('PLEASE ENSURE THAT INFO IS CORRECT')
                else:
                    print('PLEASE ENSURE THAT INFO IS CORRECT')
            elif y[0] == 'F' and z[0] == '1' and z[1] == '9':
                    if int(z[2]) < 7:
                        print('PLEASE ENSURE INFO IS CORRECT')
                    else:
                        if y[1] == z[2] and y[2] == z[3]:
                            j = int(y[1]) * 2 + int(y[2]) * 7 + int(y[3]) * 6 + int(y[4]) * 5 + int(y[5]) * 4 + \
                                int(y[6] * 3) + int(y[7]) * 2
                            k = int(j % 11)
                            if int(y[8]) == list1[k]:
                                print('THIS IS A VALID IC')
                            else:
                                print('PLEASE ENSURE THAT INFO IS CORRECT')
                        else:
                            print('PLEASE ENSURE THAT INFO IS CORRECT')
    else:
        print('PLEASE ENSURE INFO IS CORRECT')



# if singaporean key 1 if foreigner key 2 for a
# b is NRIC and c is Year of Birth

a = 1
b = 'T0200508A'
c = '2002'


checker(a, b, c)

#REVIEW
# Things to improve
#1 Code might be able to be shorter
#2 Can pinpoint the error and list them instead of simply saying ensure info is correct
#3 Can try to ensure int and strings are a bit neater

