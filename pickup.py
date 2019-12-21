from argparse import ArgumentParser
import sys,getopt
import random
def getfilename(num):
	name=""
	if num == '1':
		name="cheesy.txt"
	elif num=='2':
		name="dirty.txt"
	elif num=='3':
		name="funny.txt"
	elif num=='4':
		name="sweet.txt"
	elif num=='5':
		name="newyear.txt"
	elif num=='6':
		name="tinder.txt"
	else:
		print("use a number between 1-6")
	return name

count=len(sys.argv)

if count==1:
	print(" 1 = cheesy\n"
         " 2 = dirty\n"
         " 3 = funny\n"
         " 4 = sweet\n"
         " 5 = newyear")

else:
	 	
	filename= getfilename(sys.argv[1])
	lines = open(filename).read().splitlines()
	i = 1
	while i < 6:
		print(random.choice(lines))
		print("\n")
		i += 1
	




