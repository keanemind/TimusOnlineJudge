monsters = ("few", "several", "pack", "lots", "horde", "throng", "swarm", "zounds", "legion")
counts = (5, 10, 20, 50, 100, 250, 500, 1000)
monstercount = int(input())
# for i in range(len(counts)):
#     if monstercount < counts[i]:
#         print(monsters[i-1])
#         break
#     if i == (len(counts) - 1):
#         print(monsters[i])
#         break

for tup in enumerate(counts):
    if monstercount < counts[tup[0]]:
        print(monsters[tup[0]])
        break
    if tup[0] == (len(counts) - 1):
        print(monsters[len(monsters) - 1])
        break