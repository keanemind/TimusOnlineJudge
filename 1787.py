line1 = input()
line2 = input()
input1 = [int(string) for string in line1.split(" ")]
input2 = [int(string) for string in line2.split(" ")]
totalcars = 0
for num in input2:
    totalcars += num
if (totalcars - (input1[0]*input1[1])) > 0: #there are not enough cars to cause a traffic jam
    print(totalcars - (input1[0]*input1[1])) 
else:
    print(0)
