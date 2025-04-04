#Feita uma pesquisa de algumas características físicas da população de uma certa região, a
#qual coletaram os seguintes dados referentes a cada habitante para serem analisados:
# sexo (masculino e feminino)
# cor dos olhos (azuis, verdes ou castanhos)
# cor dos cabelos (louros, castanhos, pretos)
# idade
#Programa que determine e escreva: a maior idade dos habitantes; a quantidade de indivíduos do sexo feminino 
#cuja idade está entre 18 e 35, inclusive; quantidade de indivíduos que tenham olhos verdes e cabelos louros

olhos=[]
sexo=[]
cabelo=[]
idade=[]
ind=0
fem=0
qtd=0
resp='S'
maior=0
i=0
while ind >=0 and resp == 'S':
    idade.append(int(input('Informe a idade do individuo: ')))
    sexo.append(input('Informe o sexo do indiviuo (F/M):'))
    cabelo.append(input('Informe a cor do cabelo (louro/preto/castanho): '))
    olhos.append(input('Informe a cor do olhos (azul/castanho/verde)'))
    ind +=1
    for i in range (len(sexo)):
        if sexo[i] == 'F' and (idade[i] >=18 or idade[i] <=35):
           fem+=1
        if cabelo[i] == 'louro' and olhos[i]== 'verde':
           qtd+=1
    resp=input('Deseja continuar? (S/N): ').upper()
    if resp == 'N':
       print ('Inclusão de individuos encerrada.')
       maior=max(idade)   
#Saida
print(f'A maior idade entre os individuos é: {maior}')     
print(f'A quantidade de individuos do sexo F cuja idade está entre 18 e 35: {fem}')
print(f'A quantidade de individuos com olhos verdes e cabelos louros: {qtd}')