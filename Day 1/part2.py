with open("./data.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

increments = 0
for i in range(0, len(lines)-3, 1):
    A = [lines[i],lines[i+1], lines[i+2]]
    B = [lines[i+1], lines[i+2], lines[i+3]]

    if sum(B) > sum(A):
        increments += 1

print(increments)