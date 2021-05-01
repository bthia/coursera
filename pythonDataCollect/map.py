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
print(list(things3))
print(list(things4))


abbrevs = ['usa', 'chn', 'esp', 'jpn', 'sgp', 'rus']
abbrevs_upper = map(lambda value: value.upper(), abbrevs)

print(abbrevs)
print(list(abbrevs_upper))