import PyPDF2

def brute_force_pdf(pdf_path, wordlist_path):
    try:
        # Abrindo o arquivo PDF
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Verifica se o PDF está protegido
            if not pdf_reader.is_encrypted:
                print("O arquivo PDF não está protegido por senha.")
                return

            # Lendo a wordlist
            with open(wordlist_path, 'r', encoding='utf-8') as wordlist:
                for line in wordlist:
                    # Removendo espaços extras
                    password = line.strip()
                    try:
                        # Tentativa de desbloquear o PDF
                        pdf_reader.decrypt(password)
                        # Verifica se o PDF foi desbloqueado
                        if pdf_reader.pages:
                            print(f"Senha encontrada: {password}")
                            return
                    except:
                        pass
                print("Nenhuma senha da wordlist conseguiu desbloquear o PDF.")
    except FileNotFoundError:
        print("Arquivo PDF ou wordlist não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Caminho do arquivo PDF e da wordlist
pdf_path = "G:\Meu Drive\python\SuaContaClaro_Jan-2025.pdf"  # Substitua pelo caminho do arquivo PDF
wordlist_path = "G:\Meu Drive\python\wordlist_5_digitos.txt"  # Substitua pelo caminho da wordlist

# Chamada da função
brute_force_pdf(pdf_path, wordlist_path)
