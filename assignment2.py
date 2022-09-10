#solving a+8b-3c+d+4e-2f=54 equation using  Genetic Algorithm
import random
from prettytable import PrettyTable
random.seed(100)

#selection function selects the top 4 chromosomes which are closer to solution
def selection(population, fit_chromosomes, generation):              
    fitnessscore=[]
    selection_table=PrettyTable(["Population","Fitness"]) 
    for chromosome in population:
        individual_fitness=100-abs(54-(chromosome[0]+8*chromosome[1]-3*chromosome[2]+chromosome[3]+4*chromosome[4]-2*chromosome[5]))
        fitnessscore.append(individual_fitness)
        selection_table.add_row([chromosome,individual_fitness])
    print("=============>Selection Table<==============")
    print(selection_table)
    total_fitness=sum(fitnessscore)
    average_fitness=total_fitness/len(fitnessscore)
    score_card=list(zip(fitnessscore,population))
    score_card.sort(reverse=True)
    print('Total fitness: ', total_fitness)
    print('Average fitness: ', average_fitness)
    print('Max : ',score_card[0][0])
    for individual in score_card:
        if individual[0]==100:
            if individual[1] not in fit_chromosomes:
                fit_chromosomes.append(individual[1][::])
    
    score_card=score_card[:4]
    score, population=zip(*score_card)
    print()
    return list(population)
'''
cross-over function creates offspings
by taking random parents from selected population and
mix there values for creating offsprings
'''
def crossover(population):                                               
    random.shuffle(population)
    fatherchromosome=population[:2]
    motherchromosome=population[2:]
    children=[]
    crossover_table=PrettyTable(['Father Chromosome',"Mother Cromosome","Cross Over Point","Offsping"])
    noOfChilds=-1
    for i in range(len(fatherchromosome)):
        crossoversite=random.randint(1,5)
        fatherfragments=[fatherchromosome[i][:crossoversite],fatherchromosome[i][crossoversite:]]
        motherfragments=[motherchromosome[i][:crossoversite],motherchromosome[i][crossoversite:]]
        firstchild=fatherfragments[0]+motherfragments[1]
        children.append(firstchild)
        secondchild=motherfragments[0]+fatherfragments[1]
        children.append(secondchild)
        noOfChilds+=2
        crossover_table.add_row([fatherchromosome[i],motherchromosome[i],crossoversite,children[noOfChilds-1]])
        crossover_table.add_row([fatherchromosome[i],motherchromosome[i],crossoversite,children[noOfChilds]])
    print("=============>Crossover Table<==============")
    print(crossover_table)
    print()
    return children

'''
Randomly mutates the population
by replacing randomly selected number with a random number in chromosome
'''
def mutation(population):
    mutatedchromosomes=[]
    mutation_table=PrettyTable(["Before Mutation","Mutation Position","After Mutation"])
    for chromosome in population:
        mutation_site=random.randint(0,5)
        chro=chromosome[::]
        chromosome[mutation_site]=random.randint(1,9)
        mutatedchromosomes.append(chromosome)
        mutation_table.add_row([chro,mutation_site,chromosome])
    print("=============>Mutation Table<==============")
    print(mutation_table)
    print()
    print("*"*110)
    return mutatedchromosomes

def solveEquation(generations):
    population=[[random.randint(1,9) for i in range(6)] for j in range(6)]
    fit_chromosomes=[]
    for generation in range(generations):
        generation+=1
        print('----------------------------------------Generation: {}--------------------------------------------------'.format(generation))
        population=selection(population, fit_chromosomes, generation)
        crossover_children=crossover(population)
        population=population[::]+crossover_children[::]
        mutated_population=mutation(population)
        population=population[::]+mutated_population[::]
        #random.shuffle(population)

    return fit_chromosomes

solution=solveEquation(500)
print('-----------Solution-----------')
print(solution)
print(len(solution))
