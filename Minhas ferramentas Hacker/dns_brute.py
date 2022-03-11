import dns.resolver # Modulo de consultas DNS

res = dns.resolver.Resolver() # Objeto capaz de fazer as consultas DNS

# Abrir arquivos com subdominios
arquivo = open("/home/kali/Desktop/BancoCN/wordlist.txt", "r")
subdominios = arquivo.read().splitlines() # Ler o arquivo e dar um slip nas linhas

# Pegar alvo do usuario
print(f"Write a port (Adress): ")
alvo = input()

for subdominio in subdominios:
        # Tratamento de erro do alvo
        sub_alvo = subdominio + '.' + alvo
        try:
                result = res.resolve(str(sub_alvo), "A")
                for ip in result:
                        print(f'{sub_alvo} -> {ip}')
        except:
                print(f'{sub_alvo} -> Error')
                pass # Ignore Error
