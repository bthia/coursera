print('\n\n ****** List Comprehension ***** \n[<transform expression> for <var name> in seq if <filtration_expression>]')

print('\nExample 1: Double a list of number ************')

print(list(num * 2 for num in [2,4,53,42,423]))

print('\nExample 2: Filter Even number ************')

print(list(num for num in [2,4,53,42,423] if num%2 == 0))


print('\nExample 3: Chain map and filter *************')

things = [2,4,5,6,12,24,245, 234]

print(list(map(lambda value: value * 2, filter(lambda invalue: invalue % 2 == 0, things))))

print(list(v * 2 for v in things if v%2 == 0))