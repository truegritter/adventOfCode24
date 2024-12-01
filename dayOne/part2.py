file = open("day1.txt", "r")

left = []
right = []

for line in file:
    line = line.strip()
    line = line.split("   ")
    left.append(int(line[0]))
    right.append(int(line[1]))

left = sorted(left)
right = sorted(right)

similiarity = 0 

for i in range(len(left)):
    count = 0
    curNum = left[i]
    for j in range(len(right)):
        if curNum == right[j]:
            count += 1
    similiarity += (curNum * count)

print(similiarity)