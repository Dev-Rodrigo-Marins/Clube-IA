import requests
from PIL import Image
from io import BytesIO

# Link da imagem no servidor
url = 'http://192.168.0.106/camera' // Coloque aqui o ip da sua esp32.

# Faz uma requisição HTTP para obter a imagem
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Lê os bytes da imagem
    image_bytes = BytesIO(response.content)

    # Abre a imagem usando a biblioteca PIL
    image = Image.open(image_bytes)

    # Salva a imagem no seu computador
    image.save('/home/rodrigo/Arduino/codigo_correto_live_esp_ov76701/Imagens/imagem_salva.jpg') // Coloque aqui o caminho do seu computador onde deseja salvar
    print('Imagem salva com sucesso!')
else:
    print(f'Erro na requisição HTTP. Código de status: {response.status_code}')
