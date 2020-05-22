import random as rd
import math
population = []

nPortfolio = 5
nSubset = 5
nDataset = 10

for i in range(nPortfolio):
    tmp = [0 for i in range(nDataset)]
    bit1 = rd.sample(range(0, nDataset-1),nSubset)
    #print(bit1)
    for j in range((nDataset)):
        if j in bit1 :
            tmp[j] = 1
    population.append(tmp)
        
    
print(len(population))

"""
def crossover(population):

    def parent(population):
        parent = rd.sample(population,2)
        return parent

    parents = parent(population)
    newPopulation = [pop for pop in population] #checked by me
    #print(newPopulation)
    
    pCo = 0.5
    parent1,parent2 = parent(population) # Checked by me
    nCo = math.floor(len(population)*pCo)
    
    nPoint = 0.5
    barier =(math.floor(len(population[0])*nPoint))
    # print(parent1)
    if rd.random() > 0.2 :
        offspring1 = parent1[:barier]+parent2[barier:]
        offspring2 = parent2[:barier]+parent1[barier:]
        print(len(newPopulation))
        print(offspring1)
        
        newPopulation += [offspring1] + [offspring2]
        print(len(newPopulation))

    #newPopulation = newPopulation+[parent1]+[parent2]
    return newPopulation
print(len(crossover(population)))
"""

def generateOffspring(population) :
    sizeOfPop = len(population)
    def parent(population=population, sizeOfPop = sizeOfPop):
        #sizeOfPop = len(population[0])
        parent1 = population[rd.randint(0,sizeOfPop-1)]
        parent2 = population[rd.randint(0,sizeOfPop-1)]
        return [parent1,parent2]

    def crossover(parent,pCo = 0.5) :
        randCo = rd.random()
        print(randCo)
        parent1,parent2 = parent
        parent1.sort(reverse=True)
        parent2.sort(reverse=True)
        print(parent1)
        nGen = sum(parent1)
        nPoint = 0.5
        #barier =(math.floor(len(population[0])*nPoint))
        barier = math.floor(nGen*nPoint) 
        end = nGen
        if randCo > pCo :
            offspring1 = parent1[:barier]+parent2[barier:]
            offspring2 = parent2[:barier]+parent1[barier:]
        else :
            offspring1 = parent1[:barier]+parent2[barier:]
            offspring2 = parent2[:barier]+parent1[barier:]

        return [offspring1,offspring2]

   # Flip mutation 
    def mutation(offSpring,pMut = 0.2) :
        randMut = rd.uniform(0,1)
        print(randMut)
        newOffspring = []
        if randMut > pMut :
            for bit in offSpring :
                if bit == 1 :
                    newBit = 1
                else :
                    newBit = 0
                newOffspring.append(newBit)
            offSpring = newOffspring
        return offSpring



    
    # Start Generate
    solution = []
    while(len(solution) < 2*sizeOfPop):
        parents = parent()
        #print(parents)
        offSpring = crossover(parents)
        for x in offSpring :
            solution.append(mutation(x))
    return solution

#print((generateOffspring(population)))

lc = [1,2,3,4,5]
lb = [2,3,4]

z = set(lc) - set(lb)

print(list(z))







    
