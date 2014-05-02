#!/usr/bin/env python

'''
CPU USAGE 98.9!! JESUS (cu top | grep 1.py am facut)
'''





import random
def writef():
	f = open("nbs.txt", "w")
	for i in range (10000):
		f.write(str(random.randint(0, 10000)) + "\n")

from itertools import islice
def readsort():
	# i really don't like that i have to parse the file twice!!
	with open("nbs.txt", "r") as f:
		global num_lines
		num_lines = sum(1 for line in f)
		f.seek(0)
		for i in range (0, num_lines / 1000):
			lines = list(islice(f, 1000))
			sorting(lines)
			g = open("temp/nb" + str(i) + ".txt", "w+")
			for line in lines:
				g.write("%s" % str(line))
			g.close()
		f.close()


def sorting(myl):
	if len(myl) > 1:
		middle = len(myl)//2
		left = myl[:middle]
		right = myl[middle:]

		sorting(left)
		sorting(right)

		#now i merge left and right, which are sorted
		i = 0	#this is for left
		j = 0 	#this is for right
		k = 0	#this is for myl

		#i need a stop condition, altfel o sa depaseasca indexu lungimea listei
		#o sa fac merge-ul in myl
		#while-ul asta merge numai cand len left e egala cu len right
		while i < len(left) and j < len(right):
			if int(left[i]) < int(right[j]):		#le ia ca string si trebuie sa le convertesc la int, ca altfel compara 21 cu 3 si iasa 3 mai mare
				myl[k] = left[i]
				i = i + 1 			#trec in left la urmatorul element, sa nu il ia pentru comparare inca o data; la right nu e nevoie inca, paote mai sunt elemente mai mici in left
			else:
				myl[k] = right[j]
				j = j + 1
			k = k + 1


		#trebuie sa tratez cazurile in care right sau left au len diferite
		#adica: pot sa fie toate valorile din left < valorile din right sau invers!!
		while i < len(left):
			myl[k] = left[i]
			i = i + 1
			k = k + 1

		while j < len(right):
			myl[k] = right[j]
			j = j + 1
			k = k + 1


def scheck():
	l = []
	for i in range (1000):
		l.append(random.randint(0, 1000))
	sorting(l)
	for i in range(len(l)-1):
		if l[i] > l[i+1]:
			print False
	print True

#scheck()

def sortFinal():
	f = open("nbfin.txt", "w+")
	j = 1
	forsort = []
	files = []
	for i in range (0, num_lines / 1000):
		files.append("temp/nb" + str(i) + ".txt")
	ref_files = [open(filename, "r") for filename in files]

	while j <= num_lines / 10:
		for i in range (0, num_lines / 1000):
			forsort.append(ref_files[i].readline())
		sorting(forsort)
		j = j + 1	

	'''while j <= num_lines / 10:
		for i in range (0, num_lines / 100):
			forsort.append(ref_files[i].readline())
		j = j + 1

	sorting(forsort)'''
		

	for line in forsort:
		f.write("%s" % str(line))
	f.close()

	for filename in ref_files:
		filename.close()
	

def checkFile():
	with open("nbfin.txt", "r") as f:
		inival = f.readline()
		for line in f:
			if int(line) < int(inival):
				print False
		print True
		f.close()


def execute():
	writef()
	readsort()
	sortFinal()
	checkFile()