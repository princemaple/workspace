def quadra(a,b,c):
	delta=b**2-4*a*c
	root1,root2=(-b+delta**0.5)/(2*a),(-b-delta**0.5)/(2*a)
	if delta>0:
		return root1,root2
	elif delta==0:
		return root1
	else:
		return "No real answers!"

def main():
	while True:
		query=raw_input("a b c->")
		if not query:break
		a,b,c=[float(i) for i in query.split()]
		# print a,b,c
		print "#"*40+"\n"
		roots=quadra(a,b,c)
		print roots
		print
		print "#"*40
	return

main()
