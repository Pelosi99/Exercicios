v0 = float(input("Velocidade inicial do carro (em m/s): "))
a = float(input("Aceleração (em m/s²): "))
t = float(input("Tempo (em segundos): "))
v = v0+(a*t)
vf = v*3.6
print("A velocidade em km/h é:",vf,"KM/H")

if vf<=40:
    print("Veículo muito lento.")

if 40<vf<=60:
    print("Velocidade permitida.")

if 60<vf<=80:
    print("Velocidade de cruzeiro.")

if 80<vf<=120:
    print("Veículo rápido.")

else:
    print("Veículo muito rápido!")

input("Pressione ENTER para sair.")