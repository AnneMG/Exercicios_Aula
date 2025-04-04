#Programa que pergunte quanto um funcionário recebe por hora e o número de
#horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11%
#para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto,Quanto pagou ao IRRF,quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.

#Entrada
nome=input('Informe o nome do funcionário: ')
hora=float(input(f'Informe a quantidade de horas trabalhadas: '))
val_hora=float(input(f'Informe o valor da hora trabalhada: '))

#Processamento
sal_bru= hora * val_hora
inss= (sal_bru*8)/100
irpf=(sal_bru*11)/100
sind=(sal_bru*5)/100
saliq= sal_bru - inss - irpf - sind

#Saida
print (f'O funcionario {nome} recebeu um salario liquido de: {saliq:.2f}')
