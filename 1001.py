userinput = list(str(input()))
i = 0
done = False
for char in userinput:
    try:
        int(char)
        if done == False:
            userinput[i-1] = 'X'
            done = True
    except:
        done = False
    i += 1

while userinput.count(' ') > 0:
    userinput.remove(' ')

outputstr = ''.join(userinput)
outputlist = outputstr.split('X')
if outputlist[len(outputlist)-1] == '':
    outputlist.pop(len(outputlist)-1)
for item in outputlist:
    print("{0:.4f}".format(float(item)**(.5)))