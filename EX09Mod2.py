print("-="*20)
print("Analisador de Triângulos")
print("-="*20)
r1 = float(input("Valor do primeiro segmento: "))
r2 = float(input("Valor do segundo segmento: "))
r3 = float(input("Valor do terceiro segmento: "))
if(r1<r2+r3) and (r2<r1+r3) and (r3<r1+r2):
    print("Os segmentos podem formar um triângulo!")
else:
    print("Os segmentos não podem formar um triângulo!")
input("Aperte ENTER para fechar.")