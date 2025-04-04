#3- O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que
#leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem
#como a média delas.
temp=[]
val=1
resp = 'N'
while val >= 1 and resp == 'N': 
    temp.append(int(input('Informe as temperaturas que deseja incluir para calculo: ')))
    resp=input('Informe se deseja parar (S/N): ').upper()
    val +=1
    if resp == 'S':
        print('Inclusão de temperaturas encerrada.')        
menor= min(temp)
maior= max(temp)
media= sum(temp)/len(temp)
#Saida
print(f'A maior temperatura encontrada foi:{maior}')
print(f'A menor temperatura encontrada foi:{menor}')
print(f'A média de temperatura foi:{media}')
        