for i in range (1, 101):
	if (((i % 3) == 0) & ((i % 5) == 0)):
		print("fizzbuzz")
	elif (i % 3) == 0:
		print("fizz")
	elif (i % 5) == 0:
		print("buzz")
	else:
		print(i)

for j in range (1, 101):
	if (((j % 3) == 0) | ((j % 5) == 0)):
		if (((j % 3) == 0) & ((j % 5) == 0)):
			print("fizzbuzz")
		else:
			if ((j % 3) == 0):
				print("fizz")
			else:
				print("buzz")
	else:
		print(j)

for k in range (1, 101): print("fizzbuzz" if (((k % 3) == 0) & ((k % 5) == 0)) else ("fizz" if ((k % 3) == 0) else "buzz") if (((k % 3) == 0) | ((k % 5) == 0)) else k)