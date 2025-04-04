#programa para uma loja de tintas, que solicite o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em 
#latas de 18 litros, que custam R$ 130,00.Informe ao usuário a quantidade de latas de tinta a 
#serem compradas e o valor a ser pago.

tam=int(input('Informe o tamanho em metros quadrados da area a ser pintada: '))
#Processamento
latas = (tam/3)
valor= latas * 130
#Saida
print(f'O tamanho do imovel informado é de {tam:.2f}') 
print(f'A quantidade de latas a ser utilizada para pintura são {latas:.2f} totalizando em R${valor: ,.2f} reais')