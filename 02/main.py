# A, X for Rock
# B, Y for Paper
# C, Z for Scissors

input = open('input.txt', 'r')
rounds = input.readlines()
score = 0

for round in rounds:
    round.split(" ")
    
    if (round[0] == "A" and round[2] == "X") or (round[0] == "B" and round[2] == "Y") or (round[0] == "C" and round[2] == "Z"):
        score += 3
    elif (round[0] == "A" and round[2] == "Z") or (round[0] == "B" and round[2] == "X") or (round[0] == "C" and round[2] == "Y"):
        score += 0
    else:
        score += 6

    if round[2] == 'X':
        score += 1
    elif round[2] == 'Y':
        score += 2
    else: 
        score += 3

print(score)

# part 2
score = 0
for round in rounds:
    round.split(" ")
    if (round[0] == "A" and round[2] == "X") or (round[0] == "C" and round[2] == "Y") or (round[0] == "B" and round[2] == "Z"):
        #scissors
        score += 3
    elif (round[0] == "B" and round[2] == "X") or (round[0] == "A" and round[2] == "Y") or (round[0] == "C" and round[2] == "Z"):
        #rock
        score += 1
    else:
        #papper
        score += 2


    if round[2] == 'X':
        score += 0
    elif round[2] == 'Y':
        score += 3
    else:
        score += 6


print(score)

