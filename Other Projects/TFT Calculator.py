import math
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

#Numpy Settings
np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:0.2f}'.format})

#Matplotlib Settings
plt.style.use('dark_background')
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

# TFT Data
#Shop odds at specific levels
array_of_level_odds = np.array([(100, 0, 0, 0, 0), (100, 0, 0, 0, 0), (75, 25, 0, 0, 0), (55, 30, 15, 0, 0), (45, 33, 20, 2, 0), (25, 40, 30, 5, 0), (19, 30, 35, 15, 1), (16, 20, 35, 25, 4), (9, 15, 30, 30, 16), (5, 10, 20, 40, 25), (1, 2, 12, 50, 35)])

#No. of unique champion in particular tier, no. of same copy champion per tier, total number of champion per tier
array_of_champion_pool = np.array([(13, 13, 13, 12, 8) , (29, 22, 18, 12, 10), (377, 286, 234, 144, 80)])

try:
    level = int(input('Level: '))
    if level < 1 or level > 11:
        print('You can\'t reach that level m8')
    champion_tier = int(input('Tier of desired champion: '))
    if champion_tier < 0 or champion_tier > 5:
        print('There\'s only tier 1 to tier 5')
    same_champion_bought = int(input('Number of copies of desired champion bought in the game: '))
    if champion_tier == 1 and same_champion_bought > 29:
        print('There\'s only 29 of your desired tier 1 champions in the pool')
    elif champion_tier == 2 and same_champion_bought > 22:
        print('There\'s only 22 of your desired tier 2 champions in the pool')
    elif champion_tier == 3 and same_champion_bought > 18:
        print('There\'s only 18 of your desired tier 3 champions in the pool')
    elif champion_tier == 4 and same_champion_bought > 12:
        print('There\'s only 12 of your desired tier 4 champions in the pool')
    elif champion_tier == 5 and same_champion_bought > 10:
        print('There\'s only 10 of your desired tier 5 champions in the pool')
    same_champion_tier_bought = int(input('Number of champions bought in same tier: '))
    gold_rolled = int(input('Amount of Gold Spent: '))
    number_of_rolls = gold_rolled/2
    expected_number_of_slots = math.floor(number_of_rolls * (array_of_level_odds[level - 1, champion_tier - 1]/100) * 5)
    if gold_rolled % 2 != 0:
        print('You can only spend an even amount of money')
except ValueError:
    print('That\'s not a number')


#Calculations
level_odds = array_of_level_odds[level-1, champion_tier-1]

final_pool_size = array_of_champion_pool[2, champion_tier - 1] - same_champion_bought - same_champion_tier_bought

number_of_desired_champion = array_of_champion_pool[1, champion_tier - 1] - same_champion_bought

list_of_probability_of_hitting = []

x = 0

while x != 9:
    probability_of_hitting = (sp.stats.hypergeom.sf(x, final_pool_size, number_of_desired_champion, expected_number_of_slots) * 100)
    if probability_of_hitting < 1:
        pass 
    else:
        list_of_probability_of_hitting.append(probability_of_hitting)
    x += 1

array_of_probabilities_of_hitting = np.array(list_of_probability_of_hitting)

array_for_champions = np.arange(1, len(list_of_probability_of_hitting) + 1, 1)


#Plotting of Bar Graph
fig, ax = plt.subplots()
ax.bar(array_for_champions, array_of_probabilities_of_hitting)
ax.set_title(f'Odds Shop Calculator for Tier {champion_tier} Unit at Level {level} with {gold_rolled} Gold Rolled')
ax.set_xlabel('Number of Champions')
ax.set_ylabel('Probability')
ax.set_xticks(array_for_champions)
ax.bar_label(ax.containers[0])
plt.tight_layout()
plt.show()

fig.savefig('Odds Shop Calculator.png')