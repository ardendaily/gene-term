#!/usr/bin/python
import random
from time import sleep

generation = []
mutaterate = 80
breedrate = 50
scorepercentile = 5 #top five percent best 

class Organism:

	def __init__(self, genes=None):
		if not genes:
			self.genes = []
			for num in range(0, 25):
				self.genes.append(0)
		else:
			self.genes = genes

def mutate( organism ):
	#genes sequence linearly
	newgenes = []

	for gene in organism.genes:
		if random.randint(0,100) < mutaterate:
			newgene = gene + 1
			# print "mutation!"
		else:
			newgene = gene
		newgenes.append(newgene)

	return Organism(genes=newgenes)

def breed( organism1, organism2):
	#six of one, half-dozen of the other
	sixofone = organism1.genes[:12]
	halfdozen = organism2.genes[12:]

	newgenes = sixofone.extend(halfdozen)

	if random.randint(0,100) < breedrate:
		# print "breeding successful!"
		return Organism(genes=newgenes)
	else:
		return organism1

def score(organism):
	#best score is highest value in least space
	#i.e., one X is better than 22 As 
	score = 0
	for x in organism.genes:
		score += x 
	return score 

def numtoletter( num ):
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	index = num % len(letters)
	return letters[index]

def locate(user_string="", x=0, y=0):
	x = str(x)
	y = str(y)
	# Plot the user_string at the starting at position HORIZ, VERT...
	print("\033["+x+";"+y+"H"+user_string)



if __name__ == "__main__":
	for number in range(0,25):
		generation.append( Organism() )

	for o in range(0, 50): 
		print("\n")

	while True:

		for o in range(0, len(generation)):
			for g in range(0, len(generation[o].genes)):
				locate( 
					user_string=numtoletter(generation[o].genes[g]),
					x = o,
					y = g
				)

			locate( user_string="     ", x=o, y=30)

			locate( user_string=str(score(generation[o])),
				x = o, 
				y = 30)
			
		locate( user_string="ctrl+c to exit", x = 30, y = 0)

		nextgeneration = list(generation)
		scoresort = []



'''
I REALIZE THAT THE FOLLOWING IS INSANE

basically i'm just sorting the mutations based on their 
score and weighing the likeliness of selection
in favor of the high performers,
but i am very tired right now
and cannot think of a better way to do this.

thanks.

'''
		for o in generation:
			scoresort.append([score(o), o])
		scoresort.sort(key=lambda tup: tup[0])
		scoresort = list(scoresort[0:scorepercentile])
		best = []

		while len(best) < len(generation):
			#better performers get better selection
			for num in range(0,10):
				best.append(scoresort[0][1])
			for num in range(0, 5):
				best.append(scoresort[1][1])
				best.append(scoresort[2][1])
			for num in range(0, 2):
				best.append(scoresort[3][1])
				best.append(scoresort[4][1])
			best.append(scoresort[4][1])


		for o in range(0, len(nextgeneration)):
			nextgeneration[o] = mutate(nextgeneration[o])
			nextgeneration[o] = breed(
				nextgeneration[o], 
				random.choice(best)
				)

		generation = nextgeneration

		sleep(0.08)