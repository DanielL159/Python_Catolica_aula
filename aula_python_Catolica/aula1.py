num1= int(input("digite um numero: "))#input so retorna string pra retornar outra coisa tem que converter
num2= int(input("digite outro numero: "))


#formas de imprimir variavel em string
print(str(num1) + " + " + str(num2) + " = " + str(num1+num2));
print ("%d + %d = %d"%(num1 ,num2,num1+num2));#melhor forma pro compilador
print(f"{num1} + {num2} = {num1+num2}")
print("{}+{}={}".format(num1,num2,num1+num2))

print(str(num1) + " + " + str(num2) + " = " + str(num1+num2));
print ("%d + %d = %d"%(num1 ,num2,num1+num2));#melhor forma pro compilador
print(f"{num1} + {num2} = {num1+num2}")
print("{}/{}={:.2f}".format(num1,num2,num1/num2))
