import requests
from PIL import Image
from io import BytesIO
import subprocess
import os
import shutil
from datetime import datetime

# Link da imagem no servidor
url = 'http://192.168.0.103/camera' # Inserir o IP da ESP32 que aparece no serail monitor no 192.168.0.103
image_path = '/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/Imagens/imagem.jpg'

try:
    # Faz uma requisição HTTP para obter a imagem
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Imprime o cabeçalho de conteúdo
        content_type = response.headers.get('content-type', '')
        print('Ola eu sou Octos estou iniciando a detecção da imagem!')
        print("Aguarde por gentileza...\n")
        
        print(f'Imagem formato: {content_type}')
        
        # Verifica se o conteúdo retornado é uma imagem
        if 'image' in content_type:
            # Lê os bytes da imagem
            image_bytes = BytesIO(response.content)

            # Abre a imagem usando a biblioteca PIL
            image = Image.open(image_bytes)

            # Salva a imagem no seu computador
            image.save(image_path) 
            print('Imagem registrada com sucesso!')

            # Executa a detecção usando YOLO
            print("Executando a detecção com YOLO...")
            yolo_command = [
               'python3', '/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/darknet/detect.py',  # Script YOLO para detecção
            ]
           
        else:
            print('O conteúdo retornado não é uma imagem.')

    else:
        print("Obrigado pela preferencia")
except Exception as e:
    print(f'Erro ao processar a imagem: {e}')

