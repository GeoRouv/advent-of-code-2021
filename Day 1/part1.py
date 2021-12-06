with open("./data.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

increments = 0
decrements = 0
for i in range(0,len(lines)-1):
    if(lines[i+1] > lines[i]):
        increments += 1
    
    if(lines[i+1] < lines[i]):
        decrements += 1

print(increments)
print(decrements)