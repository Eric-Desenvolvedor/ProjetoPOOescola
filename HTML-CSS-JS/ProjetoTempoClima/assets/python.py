# Exemplo de como buscar dados meteorológicos (Python)
import requests

API_KEY = "140d9dc32dc811ca20b1f094778220aa" # Substitua com sua chave real
LATITUDE = -23.5505  # Ex: Latitude de São Paulo
LONGITUDE = -46.6333 # Ex: Longitude de São Paulo
URL = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"

# Realiza a requisição HTTP GET
response = requests.get(URL)

# Processa a resposta (que geralmente é em JSON)
if response.status_code == 200:
    data = response.json()
    temperatura = data["main"]["temp"]
    descricao = data["weather"][0]["description"]
    print(f"Temperatura: {temperatura}°C, Condições: {descricao}")
else:
    print("Erro ao buscar os dados da API")