def make_tree(elements):

	elements = list(elements)
	probs = {}
	for codepair in elements:
		for symbol in codepair:
			if symbol in probs:
				probs[symbol] = probs[symbol]+1
			else:
				probs[symbol] = 1

	num_sym = float(sum(probs.values()))

	for key in probs:
		probs[key] = float(probs[key])/num_sym

	codewords = dict.fromkeys(probs.keys(),'')

	syms_ord = sorted(list(probs.keys()))

	while len(probs) > 1:
		key1 = syms_ord[-1]
		key2 = syms_ord[-2]
		del syms_ord[-2:]

		nsym = str(key2) + ' ' + str(key1)
		probs[nsym] = probs.pop(key1)+probs.pop(key2)
		syms_ord.append(nsym)

	tree = syms_ord[0].split(' ')
	
	while len(tree) > 1:
		codewords[tree[0]] = codewords[tree[0]] + '1'
		del tree[0]

		for sym in tree:
			codewords[sym] = codewords[sym] +'0'

	codeword_string =""

	for key in codewords:
		codeword_string = codeword_string + key+":"+codewords[key]+"="

	return codeword_string[:-1]

def encode(tree, string):
	tree = list(tree.split('='))
	codewords = {}
	encoded = ""

	for codepair in tree:
		cp = codepair.split(':')
		codewords[cp[0]] = cp[1]

	for char in string:
		encoded = encoded + codewords[char.split(':')[0]]

	return encoded

def decode(tree, string):
	tree = list(tree.split('='))
	codewords = {}

	for codepair in tree:
		cp = codepair.split(':')
		codewords[cp[0]] = cp[1]

	m=[]

	for i in range(0,len(string)-1):
		print len(string)
		if string[i] == '1':
			codeword = string[:i]
			string = string[i+1:]
			m.append(codeword)


	plaintext = ""

	for codeword in m:
		plaintext = plaintext + codewords[codeword]

	print plaintext

if __name__=="__main__":
	s = 'aaalsfkjasdlfisdjngfowerfngewoifjewlofnjeroignerligjwi'
	t = make_tree(s)
	decode(t,encode(t,s))
	
