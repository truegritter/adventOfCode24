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

sum = 0 

for i in range(len(left)):
    sum += abs(left[i] - right[i])

print(sum)