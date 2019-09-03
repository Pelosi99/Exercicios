base = float(input("Digite o Valor da Base: "))
altura = float(input("Digite o Valor da Altura: "))
a = base*altura
if(a>100):
    print("A área total é:",a,("m²"))
    print("Terreno Grande")
else:
    print("A área total é:",a,("m²"))
    print("Terreno Pequeno")
input("Pressione ENTER para sair.")