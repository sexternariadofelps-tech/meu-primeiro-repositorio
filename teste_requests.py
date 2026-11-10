import requests

resposta = requests.get("https://api.github.com/users/torvalds")

if resposta.status_code == 200:
    print("Busca bem sucedida")
    dados = resposta.json()
    print(f'Nome: {dados["name"]}\n{dados["name"]} tem {dados["public_repos"]} repositórios públicos')

elif resposta.status_code == 404:
    print ("Usuário não encontrado")
else:
    print(resposta.status_code)



# print(resposta.status_code)