import sys
from collections import deque

class Solutions:
	queue = []
	stack = []

	def pushChar(self, itemstack):
		return self.stack.append(itemstack)

	def enqueueChar(self, itemqueue):
		return self.queue.append(itemqueue)

	def popChar(self):
		return self.stack.pop()

	def dequeueChar(self):
		return self.queue.pop(0)

	# def size(self):
	# 	return len(self.queue), len(self.stack)

	# def is_empty(self):
	# 	return self.size() == 0

# read the string s
s = input()

# create the Solutions class objects
obj = Solutions()

l = len(s)
# push / enqueue all the characters of string s to stack
for i in range(l):
	obj.pushChar(s[i])
	obj.enqueueChar(s[i])

isPalindrome = True
'''
__init__ (konstruktor) 
pop the pop character from stack
dequeue the first character from queue
compare both the characters
'''

for i in range(l // 2):
	if obj.popChar() != obj.dequeueChar():
		isPalindrome = False
		break

# finally print whether string s is palindrome or not
if isPalindrome:
	print("The word, "+s+", is a palindrome.")
else:
	print("The word, "+s+", is not a palindrome.")
