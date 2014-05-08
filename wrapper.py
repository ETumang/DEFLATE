import huffman as huff
import LempelZiv as lz
import time

windowlen = 100

def encode(text):

	Lziv = open('Lziv_'+file,'w')
	#text = lz.prep_text(file)

	t1 = time.clock()
	lztext = lz.encode(text,windowlen)
	Lziv.write(lztext)
	Lziv.close()
	t2 = time.clock()

	lztext = lz.prep_text('Lziv_'+file)
	t3 = time.clock()
	tree = huff.make_tree(lztext)
	t4 = time.clock()

	h = open('huff_'+file,'w')
	t5 = time.clock()
	htext = huff.encode(tree,lztext)
	#h.write(tree)
	h.write(htext)
	t6 = time.clock()
	h.close

	return [t2-t1,t4-t3,t6-t5],tree

def decode(file, tree):
	f= open('huff_'+file,'r')
	text = f.read()
	f.close
	print lz.decode(huff.decode(tree, text))

if __name__ == "__main__":
	file = raw_input("File to be encoded?")
	text = lz.prep_text(file)
	start= time.clock()
	times, tree=encode(text)
	print times
	end = time.clock()
	print end-start
	decode(file,str(tree))