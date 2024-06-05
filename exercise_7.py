import random
import matplotlib.pyplot as plt



def monte_carlo_simulation(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        sum_counts[dice_one + dice_two] += 1

    probabilities = {value: count / num_rolls for value,
                     count in sum_counts.items()}

    return probabilities


def plot_probabilities(probabilities):
    
    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel('The sum of the numbers on the dice.')
    plt.ylabel('Probability')
    plt.title('The probability of the sum of the numbers on two dice.')


    for i, prob in enumerate(probabilities.values()):
        plt.text(list(probabilities.keys())[i], prob, f"{prob*100:.2f}%", ha='center')

    plt.show()


for veracity in [100, 1000, 10000, 100000]:
    
    # Simulation and calculation of probabilities
    probabilities = monte_carlo_simulation(veracity)
    plot_probabilities(probabilities)