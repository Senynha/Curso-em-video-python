#Adicionando caracteres

# nome = input ('Qual seu nome?')
# print ('Prazer em te conhecer {}!'.format(nome))

# nome = input ('Qual seu nome?')
# print ('Prazer em te conhecer {:<20}!'.format(nome))

# nome = input ('Qual seu nome?')
# print ('Prazer em te conhecer {:^20}!'.format(nome))

# nome = input ('Qual seu nome?')
# print ('Prazer em te conhecer {:>20}!'.format(nome))

# nome = input ('Qual seu nome?')
# print ('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int (input ('Digite um valor:'))
n2 = int (input ('Outro valor'))

s = n1 + n2
m = n1 * n2
d =  n1 / n2
di = n1 // n2 
p = n1 ** n2

#Com a função ":"  dentro das chaves de um format, se controla o número de caractéres que vão ser exibidos

print ('A soma é {}, a mutiplicação é {}, e a divisão é {:.3f}'.format(s, m , d))
print ('Divisão inteira {}, e potência {}'.format(di, p))

