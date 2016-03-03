import sys

string = sys.argv[1]
words = string.split(" ")
for i in range (0,len(words)):
	print((words[i])[1:] + "-" + (words[i])[0] + "ay"),