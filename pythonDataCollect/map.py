def triple(value):
	return 3 * value

def triplestuff(a_list):
	new_list = map(triple, a_list)
	return new_list

def quadruplestuff(a_list):
	new_list = map(lambda value: 4 * value, a_list)
	return new_list

things = [3, 6, 9]
things3 = triplestuff(things)
things4 = quadruplestuff(things)
print(things)
print(*things3)
print(*things4)