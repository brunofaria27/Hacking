# Como a missao e criar portscanner, nao precisamos mandar dados para o servidor, precisamos tentar uma conexao e ver se e>
import socket

# Lista de portas a serem testadas
ports = [21, 22, 80, 443, 445, 3306, 8080, 25]

print(f"Write a port (Ip or Adress): ")
adress_or_ip = input()

for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1) # Tempo em segundos para estabelecer a conexao e mostrar o resultado  
        code = client.connect_ex((str(adress_or_ip), port)) # connect_ex -> retorna um inteiro (retorno da conexao)
                                                            # Retorno: 0 -> Conexao foi estabelecida, diferente de 0 -> Co>
        if code == 0:
                print(f"Connection successful in {port} - OPEN")
        else:
                print(f"Connection unsuccessful in {port} - CLOSED")
