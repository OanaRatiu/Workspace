#!/usr/bin/env python

import random
def write_file_random():
	f = open("nbs.txt", "w")
	for i in range (10000):
		f.write(str(random.randint(0, 10000)) + "\n")


from itertools import islice
def sort_in_subfiles():
	with open("nbs.txt", "r") as f:
		global num_lines
		num_lines = sum(1 for line in f)
		f.seek(0)
		for i in range (0, num_lines / 1000):
			lines = list(islice(f, 1000))
			sort_a_list(lines)
			g = open("temp/nb" + str(i) + ".txt", "w+")
			for line in lines:
				g.write("%s" % str(line))
			g.close()
		f.close()


def sort_a_list(myl):
	if len(myl) > 1:
		middle = len(myl)//2
		left = myl[:middle]
		right = myl[middle:]

		sort_a_list(left)
		sort_a_list(right)

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


def minimum_in_list(my_list):
	min = 10001
	for i in range (len(my_list)):
		if int(my_list[i]) < min and my_list[i] != 10001:
				min = int(my_list[i])
				index = i
	return (min, index)

import os
def sort_subfiles_into_final_file():
	f = open("nbfin.txt", "w+")
	j = 1
	forsort = []
	files = []
	for i in range (0, num_lines / 1000):
		files.append("temp/nb" + str(i) + ".txt")
	ref_files = [open(filename, "r") for filename in files]

	min = 10001
	for i in range (0, num_lines / 1000):
		forsort.append(ref_files[i].readline())
	ok = 0
	while ok < num_lines / 1000:
		min = 10001
		for i in range (num_lines / 1000):
			if int(forsort[i]) < min and forsort[i] != 10001:
				min = int(forsort[i])
				j = i
		f.write("%s\n" %str(min))
		if ref_files[j].tell() != os.fstat(ref_files[j].fileno()).st_size :
			forsort[j] = ref_files[j].readline()
		else:
			forsort[j] = 10001	
			ok = ok + 1
		
		


	

	for filename in ref_files:
		filename.close()
	

def check_final_file():
	with open("nbfin.txt", "r") as f:
		inival = f.readline()
		for line in f:
			if int(line) < int(inival):
				print False
		print True
		f.close()


def execute():
	write_file_random()
	sort_in_subfiles()
	sort_subfiles_into_final_file()
	check_final_file

execute()