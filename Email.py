import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print('Enviar email com Gmail' )
user = input("Conta do gmail: ")
password = getpass.getpass("Senha: ")

#Para o cabeçalho do email
remetente = input("From, exemplo: administrador <admin@gmail.com>: ")
destinatario = input("To, exemplo: amigo <amigo@mail.com>: ")
assunto = input("Subject, Assunto da mensagem: ")
mensagem = input("Mensagem HTML: ")

#Host e porta SMTP do Gmail
gmail = smtplib.SMTP('smtp.gmail.com', 587)

#protocolo de criptografia de dados utilizado pelo gmail
gmail.starttls()

#Credenciais
gmail.login(user, password)

#mostra a depuração da operação de remessa 1=true
gmail.set_debuglevel(1)

header = MIMEMultipart()
header['Subject'] = assunto
header['From'] = remetente
header['To'] = destinatario

mensagem = MIMEText(mensagem, 'html') #Content-type:text/html
header.attach(mensagem)

#Enviar email
gmail.sendmail(remetente, destinatario, header.as_string())

#Encerrar a conexão SMTP
gmail.quit()