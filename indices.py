import os 
os.system("cls")

#   0   1   2   3   4   5   6   7   8   9
lista = [0, 10, 20 ,30 ,40 ,50 ,60 ,70 ,80 , 90]
#   -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# minipulação delistas  pelos indices 
print (lista)
print (lista [4], lista [-6])
# Sintaxe: lista [inicio, fim -1, passo]
print (lista [3:7])
print (lista [-8:-2])
#   0   1   2   3   4   5   6   7   8   9
lista = [0, 10, 20 ,30 ,40 ,50 ,60 ,70 ,80 , 90]
#   -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# Sintaxe: lista [inicio, fim -1, passo]
os.system("cls")
#exibir o primeiro e ultimo elemento
print (lista[0], lista[-1])
print (lista[0:9])
print (lista [:5])
print (lista, lista [:])
print (lista[0:8:3])
nova_lista = lista [0:8:3]
print (nova_lista, lista)
#1 - começo; 2- ate onde ele vai na lista; 3 - de quanto em quanto ele vai

#string - slicing
#   0123456789012345678901234567890123456789012345678901234567890123456789
frase = "Não acredito que isso funciona com string tambem"
print (frase)
print (frase[10])
print (frase[-30])
print (frase [10:20])
print (frase [-20:-10])
#funciona literalmente igual um book code kk (obrigado enigmas)
print (frase[::-1])
#assim ele vai estar pulando de tras pra frente então deixaria a frase invertida 

# NAO ESQUECER QUE VC USA "LEN" PARA CONTAR CARACTERES, SEU ANIMAL

os.system("cls")
lista = [10, 20, 30]
lista [0] = 99
print (lista)
#Aqui a gente ta substituindo essa caceta por 99

texto = "Python"
texto = "J" + texto [1:]
print (texto)
texto = texto[:2] +"X" +texto [3:]
#assim a gente substitui strings (ainda nao entendi direito)
