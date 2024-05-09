# n1 = int ( input ('Digite um valor: '))
# n2 = int ( input ('Digite outro valor: '))
# print (n1+n2)

# int para numeros inteiros
# usando format ao invés de vírgula ou "+"

n1 = int ( input ('Digite um valor:'))
n2 = int ( input ('Digite outro valor:'))
s = n1 + n2
print ('a soma vale {}'.format(s))

# Mostrando todos os valores da operação usando virgula

print ('a soma entre', n1, 'e', n2, 'vale', s)

# Mostrando todos os valores da operação usando .format

print ('A soma entre {} e {} vale {}'.format(n1, n2, s))

# mesmo código utilizando "float" para números flutuantes, ex: 1.0

n3 = float (input ('Digite um número:'))
n4 = float (input ('Digite outro número:'))
v = n3 + n4
print ('A soma entre {} e {} vale {}'.format(n3, n4, v))
