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

	#get each symbol probability
	for key in probs:
		probs[key] = float(probs[key])/num_sym

	codewords = dict.fromkeys(probs.keys(),'')

	#probably not the most efficient way to do this
	syms_ord = sorted(list(probs.keys()))

	#almost certainly not the most efficient way to do this
	while len(probs) > 1:
		key1 = syms_ord[-1]
		key2 = syms_ord[-2]
		del syms_ord[-2:]

		nsym = str(key2) + ' ' + str(key1)
		probs[nsym] = probs.pop(key1)+probs.pop(key2)
		syms_ord.append(nsym)

	tree = list(set(syms_ord[0].split(' ')))

	for i in range(0, len(tree)):
		if not tree[i]: tree[i] = " "

	while len(tree) > 1:
		codewords[tree[0]] = codewords[tree[0]] + '1'
		del tree[0]

		for sym in tree:
			codewords[sym] = codewords[sym] +'0'

	codeword_string =""

	for key in codewords:
		codeword_string = codeword_string + key+"~"+codewords[key]+"@"

	return codeword_string[:-1]

def encode(tree, string):
	tree = list(tree.split('@'))
	codewords = {}
	encoded = ""

	for codepair in tree:
		cp = codepair.split('~')
		if len(cp)==2:
			codewords[cp[0]] = cp[1]
		else:
			codewords[''] = cp[0]

	for char in string:
		encoded = encoded + codewords[char]

	return encoded

def decode(tree, string):

	tree = tree.split('@')
	codewords = {}
	b = ""
	plaintext = ""

	for codepair in tree:
		cp = codepair.split('~')
		if len(cp)==2:
			codewords[cp[1]] = cp[0]
		else:
			codewords[''] = cp[0]

	for i in range(0, len(string)):
		b = b + string[i]
		if b in codewords:
			plaintext = plaintext + codewords[b]
			b = ""

	return plaintext

if __name__=="__main__":
	s = 'Hello, my name is Blackbird. I like cake.cccccccccccccccccccccccccc'
	t = make_tree(s)
	print decode(t,encode(t,s))
	
