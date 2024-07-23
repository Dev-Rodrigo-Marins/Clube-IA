import requests
from PIL import Image
from io import BytesIO

print("A imagem foi enviada ESP32!")
# Adicione aqui o código que você deseja executar


# Link da imagem no servidor
url = 'http://192.168.0.104/camera'

try:
    # Faz uma requisição HTTP para obter a imagem
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Imprime o cabeçalho de conteúdo
        content_type = response.headers.get('content-type', '')
        print(f'Content-Type: {content_type}')
        
        # Verifica se o conteúdo retornado é uma imagem
        if 'image' in content_type:
            # Lê os bytes da imagem
            image_bytes = BytesIO(response.content)

            # Abre a imagem usando a biblioteca PIL
            image = Image.open(image_bytes)

            # Salva a imagem no seu computador
            image.save('/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/Imagens/imagem_salva.jpg') 
            print('Imagem salva com sucesso! No diretorio Imagens')
        else:
            # Imprime o conteúdo retornado para análise
            print('O conteúdo retornado não é uma imagem.')
            print(response.text)  # Isso imprime o conteúdo da resposta como texto
    else:
        print(f'Erro na requisição HTTP. Código de status: {response.status_code}')
except Exception as e:
    print(f'Erro ao processar a imagem: {e}')

