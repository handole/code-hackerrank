import sys

S = input()

try:
	print(int(S))
except:
	print("Bad String")
	sys.exit(0)
	