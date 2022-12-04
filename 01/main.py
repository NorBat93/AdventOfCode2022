

input = open('input.txt', 'r')
lines = input.readlines()

elvesCalories = []
temp = 0
for line in lines:
    if line.strip() != '':
        temp += int(line)
    else:
        elvesCalories.append(temp)
        temp = 0

print(max(elvesCalories))

# Part 2

topElves = 0
for x in range(3):
    topElves += max(elvesCalories)
    elvesCalories.remove(max(elvesCalories))

print(topElves)
