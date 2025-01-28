def gerar_wordlist_5_digitos(output_file):
    try:
        with open(output_file, 'w') as file:
            for numero in range(100000):  # De 0 a 99999
                file.write(f"{numero:05}\n")  # Formata o número para ter 5 dígitos, com zeros à esquerda
        print(f"Wordlist gerada com sucesso em: {output_file}")
    except Exception as e:
        print(f"Ocorreu um erro ao gerar a wordlist: {e}")

# Nome do arquivo para salvar a wordlist
nome_arquivo = "wordlist_5_digitos.txt"

# Chama a função para gerar a wordlist
gerar_wordlist_5_digitos(nome_arquivo)