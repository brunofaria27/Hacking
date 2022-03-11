import socket # Biblioteca feita para nosso SO fazer alguma execucao na rede

# Criando objeto socket que vai utilizar do protocolo TCP IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# Conectar ao host em determinada porta alem de enviar os dados
client.connect(("bancocn.com", 80))
client.send(b"hello world") # b = converte tudo para bytes

# Armazenar os dados recebidos 
resposta = client.recv(1024) # Passar como argumento a quantidade de bytes a receber

print(resposta.decode()) # .decode() -> transforma o conteudo byte em String
