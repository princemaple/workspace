import os

h="Mode Instruction: file$word.type-mode\n\n"
h+="|->\tb:bracket surround\n|->\tz:zero prefix\n|->\ts:space margin\n|->\tt:type restricted\n\n"
h+="'$' can be used to mark counter position\ne.g. file$th.txt\n"

def smode(c):
	c=" "+c+" "
	return c

def bmode(c):
	c="("+c+")"
	return c

def zmode(n,c):
	l=len(c)
	if l<n:c="0"*(n-l)+c
	return c

def tmode(follow,f):
	l=len(follow)
	files=[name for name in f if name[-l:] == follow]
	return files

def rnall(name="file$",follow="txt",mode="n"):
	files=os.listdir(os.getcwd())
	files.remove("rename.py")
	n=len(str(len(files)))
	count=0
	if "t" in mode: files=tmode(follow,files)
	for each in files:
		count+=1
		c=str(count)
		if mode!="n":
			if "z" in mode: c=zmode(n,c)
			if "b" in mode: c=bmode(c)
			if "s" in mode: c=smode(c)
		if "$" in name:
			fn=name.replace("$","%s")+"."+follow
			fn=fn %c
		else:fn=(name+c).strip()+"."+follow
		os.rename(each,fn)
	return

def main():
	while True:
		os.system("cls")
		print h
		print "#"*25+"\n"
		try:
			command=raw_input("Enter 'general_filename.type'>>").strip()
			if not command:return
			assert command.count("$")<=1, "here's a problem"
			filename,follow=command.split(".")
			if "-" in follow: follow,mode=follow.split("-")
			else:mode="n"
			rnall(filename,follow,mode)
		except AssertionError:
			print "\nThere shouldn't be more than 1 '$'."
			raw_input()
			continue
		except:
			print "\nError occured, please enter general_filename and file type separated by space."
			print "Press Enter to continue [twice to exit]"
			raw_input()
			continue
main()
