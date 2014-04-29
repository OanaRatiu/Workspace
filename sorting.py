def sorting(initl):
	# i'll use bubble sort (i'm not confusing it again with insertion sort :| )
	# this is slower than merge sort: n^2 complexity, while merge sort has nlogn
	sorted = False
	while not sorted:
		sorted = True
		for index in range(0, len(initl) - 1):
				if int(initl[index]) > int(initl[index + 1]):
					(initl[index + 1], initl[index]) = (initl[index], initl[index + 1])
					sorted = False


def mergeSort(flist):
	# cam ca divide et impera, impart lista pana ajung la un element si dupa ma intorc sa le merge
    if len(flist) > 1:
        mid = len(flist)//2
        left = flist[:mid]
        right = flist[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                flist[k] = left[i]
                i = i + 1
            else:
                flist[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            flist[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            flist[k] = right[j]
            j = j + 1
            k = k + 1

'''flist = [54,26,93,17,77,31,44,55,20]
mergeSort(flist)
print(flist)'''
import random
def scheck():
    l = []
    for i in range (1000):
        l.append(random.randint(0, 1000))
    sorting(l)
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            print False
    print True

scheck()



