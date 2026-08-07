import os 
os.system("cls")
#metodos de strings 
nome = "jão luiz rivia al gaib drumon santos hornet tunico de oliveira tozzi"
print (nome.upper()) # todos as letras em maiusculo
print (nome.lower()) # todas as letras em minusculo
print (nome.title) #todas as primeiras letras em maiusculo
print (nome.capitalize()) # primeira letra em maiusculo

os.system("cls")
nome = "    jão gizz    "
print ('|' + nome + '|', len(nome), 'caracteres') 

novo = nome.strip()#Elimina os espaços das extremidades
print ('|' + novo + '|', len(novo), 'caracteres')

novo = nome.rstrip() #tira todos os espaços do final
print('|' + novo  + "|", len (novo), 'caracteres')

novo = nome.lstrip() #tira todos os espaços do começo
print('|' + novo  + "|", len (novo), 'caracteres')

os.system ("cls")
frase = "Aprendendo a manipular strings"
new1 = frase.replace ('e', 'E')
print (new1)
new2 = frase.replace ('manipular', '********')
print (new2)
new3 = frase.replace ('n','N',2)
print (new3)

os.system("cls")
texto = "O split() divide a string para uma lista pelo argumento passado"
print (texto)
print (texto.split (), len (texto.split()), "partes")
print (texto.split('p'), len (texto.split ('p')),"partes")
print (texto.split('uma'), len(texto.split('uma')), "partes")

os.system("cls")
linguagens = ["python", "c", "java", "javascript"]
print (linguagens)
print ("|".join (linguagens))

os.system("cls")
texto = "programação em python"
print (texto.find ("em"))
print (texto.find ("gra"))
#ele mostra a posição em que a palavra procurada se encontra (contando os caracteres do 0 igual toda a lista)

print(texto.find ("CU"))
#se não tiver ele exibe -1

os.system ("cls")
texto = "programação em python em um computador"
print (texto.count('o')) #ele vai contar quantos vezes tem o elemento pedido que aqui foi 0

os.system("cls")
texto = "Python"
print ((texto.startswith ("cs"))) #ele vai mostrar FALSE pq nao tem "cs" no texto
print ((texto.startswith ("Py"))) #Ele vai mostrar Tru pq tem no texto
print ((texto.startswith ("py"))) #False pq não tem no texto

texto2 = "relatorio.pdf"
print(texto2.endswith(".docx")) #vai exibir false (pelo mesmo motivo mas agora no final)
print (texto2.endswith(".pdf")) #true ne... eu nao preciso explicar eu acho...
#NOMENCLATURA RESOLVE TUDO, AMEM

os.system("cls")
texto = "1234"
print (texto.isdigit())
texto = "-1234"
print (texto.isdigit())

