s = str(input("Informe o gênero [M/F]: ")).strip().upper() [0]
p = float(input("Digite seu peso: "))
a = float(input("Digite sua altura: "))
massa = p/(a*a)
if s=="M":
   print("Sua relação peso/altura²:",massa)
   if massa < 20:
        print("Abaixo do Peso.")
   elif 20 <= massa <25:
        print("Peso ideal.")
   else:
        print("Acima do peso.") 
else:
    print("Sua relação peso/altura²:",massa)
    if massa < 19:
        print("Abaixo do Peso.")
    elif 19 <= massa <24:
        print("Peso ideal.")
    else:
        print("Acima do peso.")
input("Aperte ENTER para sair.")        