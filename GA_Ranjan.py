# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 21:45:56 2021

@author: ranjan
https://pythonhealthcare.org/2018/10/01/94-genetic-algorithms-a-simple-genetic-algorithm/
"""
import numpy as np
import random
def Initial_population(individuals, chromosome_length):
    # Set up an initial array of all zeros
    population = np.zeros((individuals, chromosome_length))
    # Loop through each row (individual)
    for i in range(individuals):
        # Choose a random number of ones to create
        ones = random.randint(0, chromosome_length)
        # Change the required number of zeros to ones
        population[i, 0:ones] = 1
        # Sfuffle row
        np.random.shuffle(population[i])
    return population

def Calculate_fitness(population):
    fitness_scores=22-np.sum(population,axis=1) #1/(np.sum(population,axis=1)+0.0005)
    return fitness_scores


def Parent_selection(population, scores):
    # Get population size
    population_size = len(scores)
    # Pick individuals for tournament
    fighter_1 = random.randint(0, population_size-1)
    fighter_2 = random.randint(0, population_size-1)
    # Get fitness score for each
    fighter_1_fitness = scores[fighter_1]
    fighter_2_fitness = scores[fighter_2]
    # Identify undividual with highest fitness
    # Fighter 1 will win if score are equal
    if fighter_1_fitness >= fighter_2_fitness:
        winner = fighter_1
    else:
        winner = fighter_2
    # Return the chromsome of the winner
    return population[winner, :]

def Crossover_operation(parent_1, parent_2):
    # Get length of chromosome
    chromosome_length = len(parent_1)
    # Pick crossover point, avoding ends of chromsome
    crossover_point = random.randint(1,chromosome_length-1)
    # Create children. np.hstack joins two arrays
    child_1 = np.hstack((parent_1[0:crossover_point], parent_2[crossover_point:]))
    child_2 = np.hstack((parent_2[0:crossover_point], parent_1[crossover_point:]))
    # Return children
    return child_1, child_2

def Mutation_operation(population, mutation_probability):
    # Apply random mutation
    random_mutation_array = np.random.random(size=(population.shape))
    random_mutation_boolean = random_mutation_array <= mutation_probability
    population[random_mutation_boolean] = np.logical_not(population[random_mutation_boolean])
    # Return mutation population
    return population

print("---------------------------------------------------------")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
print("Random Initial Population")
population_matrix=Initial_population(5,10)   # (10, 22)   10 samples, 22 channels
print(population_matrix)
print("Score of the population")
score_matrix=Calculate_fitness(population_matrix)
print(score_matrix)
parent_1 = Parent_selection(population_matrix, score_matrix)
parent_2 = Parent_selection(population_matrix, score_matrix)
print("Selected parents for crossover")
print(parent_1)
print(parent_2)
print("New children after crossover")
child_1, child_2=Crossover_operation(parent_1, parent_2)
print(child_1)
print(child_2)
print("Child Population after mutation")
childpopulation = np.stack((child_1, child_2))
mutation_probability=0.85
afterMutation=Mutation_operation(childpopulation, mutation_probability)
print(afterMutation)
print("---------------------------------------------------------")
print("---------------------------------------------------------")
print("---------------------------------------------------------")



