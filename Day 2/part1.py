with open("./data.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# lines = ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]

directions = {"depth": 0, "position": 0}

for line in lines:
    move = line.split()

    if(move[0] == "forward"): directions["position"] += int(move[1])
    if(move[0] == "down"): directions["depth"] += int(move[1])
    if(move[0] == "up"): directions["depth"] -= int(move[1])

print(directions["depth"]*directions["position"])