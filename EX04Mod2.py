a = float(input("Digite o Valor da base: "))
b = float(input("Digite o Valor da altura: "))
r = a*b
if(r>100):
    print("A área é:",r,("m²"))
    print("Terreno Grande")
else:
    print("A área é",r,("m²"))
input("Pressione ENTER para sair.")