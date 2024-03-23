#aula1_parte2
#if<condicao>:bloco verdadeir
#python tomar cuidado na identacao
#nao existe operador de imcremento em python

salario = float(input("digite o salario para calculo: "))
base=salario
imposto = 0
if base > 3000:
    imposto = imposto+ ((base-3000)*0.35)
if base < 3000:
    imposto = imposto + ((base-1000)*0.20)

for rodada in range(1,10):
    print(rodada)
for rodada2 in range(1,10,2):
    print (rodada2)
for rodada3 in [1,2,3,4,5,6]:
    print(rodada3)

