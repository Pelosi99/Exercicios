from os import system

print('Cadastro de Contatos\n')

contatos=[]

while(True):
    system('cls')
    print('1 - Inserir Contato')
    print('2 - Atualizar Contato')
    print('3 - Excluir Contato')
    print('4 - Listar Contatos')
    print('5 - Sair')

    op = int(input('Digite a opção escolhida: '))

    while( (op<1) or (op>5) ):
        print('Opção inválida!')
        op = int(input('Digite a opção escolhida: '))

    if (op == 1):
        nome = input('Digite o nome do Contato: ')
        contatos.append(nome)
        print('Cadastro realizado com sucesso!')
        input()

    elif (op == 2):
        nomeant = input('Digite o nome do Contato que deseja alterar: ')
        contatos.remove(nomeant)
        nomenov = input('Digite o novo nome do contato: ')
        contatos.append(nomenov)
        print('Contato alterado com sucesso!')
        input()
    elif (op == 3):
        
        for i in range(0, len(contatos), 1):
            print(contatos[i])
        
        nome = input('Digite o nome do contato que deseja excluir: ')
        contatos.remove (nome)
        print('Contato Excluido com sucesso!')
        input()
    
    elif (op == 4):
        
        for c in contatos:
            print(c)
        input()
    else:
        break