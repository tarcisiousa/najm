"""from zeep import Client

url = "https://pje.tjmt.jus.br/pje/intercomunicacao?wsdl"
client = Client(url)

# Listar todos os métodos disponíveis no serviço
for service in client.wsdl.services.values():
    for port in service.ports.values():
        operations = port.binding._operations
        for operation in operations:
            print(operation)

url = "https://pje.tjmt.jus.br/pje/ConsultaPJe?wsdl"
client = Client(url)

# Faz a chamada ao método consultarProcessoReferencia
response = client.service.consultarProcesso("0600361-77.2024.6.05.0066")
print(response)"""

from zeep import Client

url = "https://pje.tjmt.jus.br/pje/ConsultaPJe?wsdl"
client = Client(url)

# Número de processo a ser consultado
numeros_processos = [
    "8000742-91.2023.8.05.0251",  # Exemplar que você usou
   # Insira outros números conhecidos
]

for numero_processo in numeros_processos:
    try:
        response = client.service.consultarProcessoReferencia(numero_processo)
        print(f"Resultado para {numero_processo}: {response}")
    except Exception as e:
        print(f"Ocorreu um erro para {numero_processo}: {e}")


from zeep import Client

url = "https://pje.tjmt.jus.br/pje/intercomunicacao?wsdl"
client = Client(url)

# Defina o número do processo, a senha do consultante e o id do consultante
numeros_processos = ["8000742-91.2023.8.05.0251"]
senha_consultante = "gustavo123"
id_consultante = "052.246.84-544"  # ID fornecido pelo tribunal ou pelo sistema

for numero_processo in numeros_processos:
    try:
        # Usando um dicionário para fornecer os parâmetros corretos
        response = client.service.consultarProcesso(
            numeroProcesso=numero_processo,
            senhaConsultante=senha_consultante,
            idConsultante=id_consultante
        )
        print(f"Resultado para {numero_processo}: {response}")
    except Exception as e:
        print(f"Ocorreu um erro para {numero_processo}: {e}")


import requests
from bs4 import BeautifulSoup

url = "https://pje.tjba.jus.br/"
params = {
    "numero_processo": "8000742-91.2023.8.05.0251"
}

response = requests.get(url, params=params)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar e exibir informações relevantes
situacao = soup.find('div', class_='situacao-processo').text
print(situacao)

#"txtConsultaContextoExpedientes"