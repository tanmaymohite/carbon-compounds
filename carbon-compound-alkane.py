print('-----------------------------------')
print('             Alkane')
print('-----------------------------------')

n = input('Enter the numbers of carbon atoms: ')
n = int(n)
c = n*2+2
name = ''
print('-----------------------------------')

if n == 1:
    name = 'Methane'
elif n == 2:
    name = 'Ethane'
elif n == 3:
    name = 'Propane'
elif n == 4:
    name = 'Butane'
elif n == 5:
    name = 'Pentane'
elif n == 6:
    name = 'Hexane'
elif n == 7:
    name = 'Heptane'
elif n == 8:
    name = 'Octane'
elif n == 9:
    name = 'Nonane'
elif n == 10:
    name = 'Decane'
else:
    name = 'non-standard '

print('Name:- ' + name)
print('Molecular formula:- '+'C'+str(n)+'H'+str(c))
print('-----------------------------------')
