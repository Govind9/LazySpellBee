def specialMultiply(n, m):
	#This function makes adjustments for big multiplications. 
	#It is just AWESOME. Wrapping up the answer everytime it crosses the given limit.
	if n > 1000000007:
		n = n % 1000000007
	n = n * m
	n = n % 1000000007
	return n

def possibilities(W):
	#For the given word, this function calculates the total number of possibilities (modulo 1000000007 of course)
	length = len(W)
	if length <= 1:
		return 1
	n = 1
	if W[0] != W[1]:
		n = 2
	if W [length - 1] != W[length - 2]:
		n = n * 2
	for i in range(1, length - 1):
		m = 3
		if W[i] == W[i + 1]:
			m = m - 1
		if W[i] == W[i - 1]:
			m = m - 1
		if W[i - 1] == W[i + 1]:
			m = 2
		if W[i - 1] == W[i + 1] and W[i - 1] == W[i]:
			m = 1
		n = specialMultiply(n, m)
	n = n % 1000000007
	return n

#Open the file for reading input.
f = open("A-large-practice.in", "r")
#Open a file to write answer into it.
O = open("Answer.out", "w")
#Read the number of inputs from the input file.
T = int(f.readline())
#for every word in the input file do the stuff in the loop.
for i in range(1, T + 1):
	#Read the word and store it in W
	W = f.readline()
	#Strip the \n from the back of the word. I know there must be a better way to do this.
	W = W[0:len(W) - 1]
	#Write the answer in the desired format in the output file.
	O.write("Case #" + str(i) + ": " + str(possibilities(W)) + "\n")
#Close everything.
f.close()
O.close()
