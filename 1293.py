inputs = input().split(" ")
numsonly = []
for tup in enumerate(inputs):
    if tup[1] != '':
        try:
            numsonly.append(int(tup[1]))
        except:
            None

print(numsonly[0]*numsonly[1]*numsonly[2]*2)
