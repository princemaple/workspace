from itertools import permutations as per
import re

operators=per(['+','+','+','-','-','-','*','*','*','/','/','/'],3)
operatorset=set([])
while True:
	try:operatorset.add(operators.next())
	except:break

def call(numset):
	def calc(ar):
		operations=[
			"%f %%s %f %%s %f %%s %f" %(ar[0],ar[1],ar[2],ar[3]),
			"(%f %%s %f) %%s %f %%s %f" %(ar[0],ar[1],ar[2],ar[3]),
			"%f %%s (%f %%s %f) %%s %f" %(ar[0],ar[1],ar[2],ar[3]),
			# "%f %%s %f %%s (%f %%s %f)" %(ar[0],ar[1],ar[2],ar[3]),
			"(%f %%s %f %%s %f) %%s %f" %(ar[0],ar[1],ar[2],ar[3]),
			# "%f %%s (%f %%s %f %%s %f)" %(ar[0],ar[1],ar[2],ar[3]),
			"((%f %%s %f) %%s %f) %%s %f" %(ar[0],ar[1],ar[2],ar[3]),
			"(%f %%s (%f %%s %f)) %%s %f" %(ar[0],ar[1],ar[2],ar[3]),
			# "%f %%s ((%f %%s %f) %%s %f)" %(ar[0],ar[1],ar[2],ar[3]),
			# "%f %%s (%f %%s (%f %%s %f))" %(ar[0],ar[1],ar[2],ar[3]),
			"(%f %%s %f) %%s (%f %%s %f)" %(ar[0],ar[1],ar[2],ar[3])
		]
		results=set([])
		for op in operations:
			for sign in operatorset:
				eq=op %(sign[0],sign[1],sign[2])
				try:
					if eval(eq)==24:
						results.add(re.sub(".0+","",eq))
				except:pass
		for result in results:print result
		return
	
	generator=per(numset)
	while True:
		try:calc(generator.next())
		except:break

def main():
	print "Hi!\n"
	while True:
		q=raw_input("enter number set as '1,2,3,4'>>")
		if not q:break
		try:
			q=q.strip().split(',')
			if any(not x.isdigit() for x in q):
				print "\n## I'm expecting to see NUMBERs. ##\n"
				continue
			if len(q)!=4:
				print "\n## Please enter exactly 4 numbers, separated by comma sign ##\n"
				continue
		except:
			print "\n## You've entered a wrong query that I am not expecting to see ##\n"
			continue
		q=[float(i) for i in q]
		if any(x>=10 for x in q):
			print "\n## Please enter numbers within 1-9 ##\n"
			continue
		call(q)
		print "\n"+"#"*50+"\n"
main()