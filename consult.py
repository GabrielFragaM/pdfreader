import requests

# URL da sua API Flask
url = 'http://localhost:5000/parse-pdf'

# Caminho para o arquivo PDF que você deseja enviar
file_path = 'caminho/para/arquivo.pdf'

# Preparar os arquivos para o envio
files = {'file': open(file_path, 'rb')}

# Fazer a requisição POST com o arquivo
response = requests.post(url, files=files)

# Fechar o arquivo
files['file'].close()

# Verificar a resposta
if response.status_code == 200:
    if len(str(response.json())) > 5:
        print('sucesso')
else:
    print("Erro ao fazer a requisição:", response.status_code)
