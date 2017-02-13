monsters = ("few", "several", "pack", "lots", "horde", "throng", "swarm", "zounds", "legion")
counts = (1, 5, 10, 20, 50, 100, 250, 500, 1000)
monstercount = int(input())
for i in range(len(counts)):
    if monstercount < counts[i]:
        print(monsters[i-1])
        break
    if i == (len(counts) - 1):
        print(monsters[i])
        break

