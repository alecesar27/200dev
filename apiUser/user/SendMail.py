import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_mail(emails,body): 
      
      host = 'smtp.gmail.com'
      
      port = '587'
      
      login = 'joao@gmail.com' #mude a sua senha aqui
      
      senha = 'nemwdfdsfmfvetjvnxfbj'  #mude a sua senha aqui

      server = smtplib.SMTP(host,port)
      
      server.ehlo()
      server.starttls()
      server.login(login,senha)
      
      '''
      Para gerar senha de app na conta do google
      https://myaccount.google.com/apppasswords?utm_source=google-account&utm_medium=myaccountsecurity&utm_campaign=tsv-settings&rapt=AEjHL4OwgomkYdEWF8XsTd3X6QZa_OnUqdlOqDervC1DECQDv9-EF1OgKBz0uZ9LVk-fIcHO4aXXbG1IYJab0KNTusSMaHCo1pjTl9tAxm5X_diosVHrc44
      '''
      corpo = body
                
      
      email_msg = MIMEMultipart()
      
      email_msg['From'] =  'joao@gmail.com' #Quem está mandando o email
      
      email_msg['To'] = emails #Substitui um email fixo pelo vindo na função.
      
      email_msg['Subject'] = 'Ative you account!'                                      
                            

                              
      email_msg.attach(MIMEText(corpo,'plain'))

      
      #caminho_arquivo = '/home/acesar/Área de Trabalho/CURSO PYTHON/MOD 27 Integração com E-mail/Enviar e-mail pelo Gmail - smtplib/Enviar e-mail pelo Gmail - smtplib/Marketing.xlsx'
      
      
      
      server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
      
      server.quit()