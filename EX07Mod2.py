p = float(input("Digite o seu peso: "))
a = float(input("Digite a sua altura: "))
r = p/(a*a)
print("Sua relação Peso/Altura²:",r)
if(r<20):
    print("Abaixo do peso.")
if(r>=25):
    print("Acima do peso.")
elif(20<=r<25):
    print("Peso ideal.")
input("Pressione ENTER para sair.")
