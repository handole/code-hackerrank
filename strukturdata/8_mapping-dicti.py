# def add(x, y):
# 	return x + y

# add(2, 5)
# print(add)

# def multiply(x):
# 	return x * 2

# map(multiply, [1, 2, 3, 4, 5])
# print(map)

# user = {'sam': '08978647', 'lido': '087876556', 'juju': '089746756'}
# print(type(user))
# print(user.keys())
# print(user.values())

# for us in user:
# 	print(us, user[us])

# user = {}
# n = int(input('jumlah list : '))

# user = dict(input().split() for k in range(n))

# for i in range(n):
# 	name = input()
# 	if name in user:
# 		print("%s=%s" % (name, user[name]))
# 	else:
# 		print("not found")

dict = {k:v for k, v in (input().split() for i in range(int(input())))}

while True:
	queryName = input()
	if queryName in dict:
		print('{}={}'.format(queryName, dict[queryName]))
	else:
		print("Not found")

# n = int(input())
# phonebook = {}

# for i in range(n):
# 	name, phonenum = input().strip().split(' ')
# 	phonebook[name] = phonenum

# while True:
# 	try:
# 		lookupname = input()
# 		if lookupname in phonebook:
# 			print('{}={}'.format(lookupname, phonebook[lookupname]))
# 		else:
# 			print('Not found')

# 	except:
# 		break

# n = int(input())
# user = dict(input().split() for k in range(n))
# for i in range(n):
#     name = input()
#     try:
#         print(name+'='+d[name])
#     except KeyError:
#         print('Not found')



	# print("%s=%s" % (us, user[us]))
	# if user[us]:
	# 	print("Not found")
	# if user[us]:
	# 	print("%s=%s" % (us, user[us]))
	# else:
	# 	print("Not found")

# 	if user[us]:
# 		print("%s=%s" % (us, user[us]))
# 	else:
# 		print("Not found.")


# if user.keys():
# 	for us in sorted(user):
# 		print("%s=%s" % (us, user[us]))
# else:
# 	print("Not found.")





# for k, v in user.items():


	# if us == user.keys():
	# 	print(us,'=',user[us])
	# else:
	# 	print('Not found')

# print(type(user))
# print(user.keys())
# print(user.values())
# print(str(user)
# print(user.keys(), '=', user.values())



# user = dict(input().split() for x in range(n))
# print(user)

# print(type(user))
# for us in user:
# 	print()

# n = int(input())
# user = input(n, user{})

# for us in user:
# 	if us == n:
# 		print('')



# phonebook = {}

# n = int(input())

# phonebook = dict(input().split() for book in range(n))

# for book in sorted(phonebook):
#     print("%s=%s" % (book, phonebook[book]))
#     if phonebook[book]:
#         print("Not found")
#     if phonebook[book]:
#         print("%s=%s" % (book, phonebook[book]))
#     else:
#         print("Not found.")

# if phonebook.keys():
#     for book in sorted(phonebook):
#         print("%s=%s" % (book, phonebook[book]))
# else:
#     print("Not found")