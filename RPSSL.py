import numpy as np

str2int = {'Rock': 0, 'Paper' : 1, 'Scissors': 2, 'Spock': 3, 'Lizard': 4}
int2str = {str2int[x]: x for x in str2int.keys()}
exod = [[0, -1, 1, 1, -1], [1, 0, -1, -1, 1], [1, -1, 0, -1, 1], [-1, 1, 1, 0, -1], [1, -1, -1, 1, 0]]

input = input()
int_input = str2int[input]
rand = int(np.random.randint(low=0, high=5, size=1)[0])

print("Your choice is ", input)
print("Computer choosed ", int2str[rand])

if exod[int_input][rand] == -1:
    print("You lose!")
elif exod[int_input][rand] == 0:
    print("Draw!")
elif exod[int_input][rand] == 1:
    print("You won!")