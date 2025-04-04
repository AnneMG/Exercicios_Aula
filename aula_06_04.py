#Crie um programa que:
#1- Peça ao usuário para digitar dez números inteiros e os armazene em uma lista.
#2- Exiba a lista completa.
#3- Exiba o maior e o menor número da lista.
#4- Exiba a soma e a média de todos os números.

lista=[]
for i in range (10):
    lista.append(int(input('Informe a seguir 10 numeros a serem incluidos na lista:')))
maior=max(lista)
menor=min(lista)
soma=sum(lista)
media= (soma/len(lista))
print(f'os numeros informados foram: {lista}')
print(f'O menor numero informados foi: {menor}')
print(f'O maior numero informados foi: {maior}')
