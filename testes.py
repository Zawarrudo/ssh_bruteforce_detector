
linha = ("Nov 19 10:23:45 server sshd[1234]: Failed password for root from 203.0.113.5 port 52814 ssh2".split())

evento = {
    "Retorno": linha[5],
    "IP": linha[10],
    "porta": linha[12],
    "user": linha[8],
    "hora": linha[2]
}
  
print(f"na hora de: {evento["hora"]} um {evento["Retorno"]} foi gerado a partir do user {evento["user"]} ")
