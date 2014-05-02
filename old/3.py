'''from re import compile
l=compile("([\w,.'\x92]*\w)").findall(open(raw_input('Input file: '),'r').read().lower())
f=open(raw_input('Output file: '),'w')
for word in set(l):
    print>>f, word, '\t', l.count(word)
f.close()'''

class Word(object):
	"""docstring for word"""
	def __init__(self, myw):
		self.uniq = 0
		self.myw = myw


''' merge sort are nlogn complexitate, mai mica decat alealalte'''
def sorting(myl):
	if len(myl) > 1:
		lm = len(myl)
		middle = len(myl)//2
		left = myl[:middle]
		right = myl[middle:]

		sorting(left)
		sorting(right)

		'''print "**********************"
		for word in left:
			print word.myw + " " + str(word.uniq)
		print "\n"
		for word in right:
			print word.myw + " " + str(word.uniq)
		print "----------------------" '''


		i = 0	#this is for left
		j = 0 	#this is for right
		k = 0	#this is for myl

		while i < len(left) and j < len(right):
			if k > 0:
				if left[i].myw == myl[k-1]:
					i = i + 1 
					myl[k-1].uniq = 1
					continue
				if right[j].myw == myl[k-1]:
					j = j + 1
					myl[k-1].uniq = 1
					continue
			if left[i].myw == right[j].myw:										#daca primul din left si primu din right sunt ==, il pun numa pe left si il ignor pe right	
				myl[k].myw = left[i].myw
				myl[k].uniq = 1
				k = k + 1
				j = j + 1
				i = i + 1
			else:
				if left[i].myw < right[j].myw:
					myl[k] = left[i]
					i = i + 1
					k = k + 1 			
				elif left[i].myw > right[j].myw:
					myl[k] = right[j]
					j = j + 1
					k = k + 1

			'''if (left[i-1].myw == myl[k-1].myw) or (i < len(left)-1 and left[i+1].myw == left[i].myw):
				i = i+i
			if (right[j-1].myw == myl[k-1].myw) or (j < len(right)-1 and right[j+1].myw == right[j].myw):
				j = j+1
				
			
			if i < len(left)-1 and left[i].myw == left[i+1].myw:				#daca is 2 egale in left, il skip pe unu
				left[i+1].uniq = 1
				i = i + 1
			if j < len(right)-1 and right[j].myw == right[j+1].myw:			#daca is 2 egale din right, il skip pe unu
				right[j+1].uniq = 1
				j = j + 1'''
		

		while i < len(left):
			#if (left[i].myw == myl[k-1].myw) or (i < len(left)-1 and left[i].myw == left[i+1].myw):
			if (left[i].myw == myl[k-1].myw):
				i = i+i
				myl[k-1].uniq = 1
			else:
				myl[k] = left[i]
				i = i + 1
				k = k + 1

		while j < len(right):
			#if (right[j].myw == myl[k-1].myw) or (j < len(right)-1 and right[j].myw == right[j+1].myw):
			if (right[j].myw == myl[k-1].myw):
				j = j+1
				myl[k-1].uniq = 1
			else:
				myl[k] = right[j]
				j = j + 1
				k = k + 1

		print "//////////////////BEFORE////////////////////"		
		for word in myl:
			print word.myw + " " + str(word.uniq)
		print "//////////////////////////////////////"
		
		if k < lm:
			for p in range(lm-k):
				myl.pop()

		print "//////////////////AFTER////////////////////"		
		for word in myl:
			print word.myw + " " + str(word.uniq)
		print "//////////////////////////////////////"

		'''print str(k)+ " " + str(lm)
			for p in range (k, lm):
				print myl[p].myw + " " + str(myl[p].uniq)
				myl.pop(p)'''

l = []
w1 = Word("aa")
w2 = Word("fgh")
w3 = Word("ca")
w4 = Word("aa")
w5 = Word("chf")
w6 = Word("fgh")
w7 = Word("aa")
w8 = Word("b")
w9 = Word("b")
l.append(w1)
l.append(w2)
l.append(w3)
l.append(w4)
l.append(w5)
l.append(w6)
l.append(w7)
l.append(w8)
l.append(w9)
sorting(l)
for word in l:
	print word.myw + " " + str(word.uniq)

def check():
	with open("word", "r") as f:
		delimiters = ['\n',' ', ',', '.', '?', '!', ':', '"', "*", "="]
		lines = f.readlines()
		for line in lines:
			for delimiter in delimiters:
			    new_words = []
			    for word in lines:
			        new_words += word.split(delimiter)
			    lines = new_words
		print new_words




#check()

def checkf():
	with open('word','r') as f:
		delimiters = ['\n',' ', ',', '.', '?', '!', ':', '"']
		#lines = f.readlines()
		lines = []
		lines.append("am fost, dfsadfsa dasda!! dsaf, das.!!\n dsadfas fasfda")
		lines.append("dasdasfsa gfdf")
		for delimiter in delimiters:
		    new_words = []
		    for word in lines:
		        new_words += word.split(delimiter)
		    lines = new_words
		print new_words

#checkf()
