v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
v3 = float(input("Digite o terceiro valor: "))
if(v1>v2>v3 or v1>v3>v2):
    print ("Primeiro numero maior.")
if(v2>v3>v1 or v2>v1>v3):
    print ("Segundo numero maior.")

if(v3>v2>v1 or v3>v1>v2 ):
    print ("Terceiro numero maior.")

input ("Aperte ENTER para sair.")
