import subprocess
import requests
import re  # Para expressões regulares
import os
import shutil
from datetime import datetime
predictions_path = '/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/imagemsaida/'


# Comando que será executado
command = [
    "/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/darknet/darknet",  # Caminho completo para o executável
    "detector",
    "test",
    "/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/darknet/digo.data",
    "/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/darknet/digo.cfg",
    "/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/darknet/digo_8000.weights",
    "/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/Imagens/imagem.jpg",
    "/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/imagemsaida/"
]

# Executando o comando
try:
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode()
    print("Resultados do Yolo:")
    
    # Usando expressão regular para encontrar a classe e a confiança
    match = re.search(r'(\w+): (\d+)%', output)
    if match:
        classe_detectada = match.group(1)
        confianca = int(match.group(2))

        # Exibir a classe e a confiança
        print(f"Classe detectada: {classe_detectada}, Confiança: {confianca}%")

        # Enviar dados para a ESP32 se a confiança for maior que um limite
        if confianca > 10 and classe_detectada =='papel':  # Ajuste o limite conforme necessário
            ip_esp32 = "http://192.168.0.104/ledAzul"# Ajuste conforme sua lógica
            requests.get(ip_esp32)
            #print("Resposta da ESP32:", response.text)
        elif confianca >10 and classe_detectada =='plastico':
            ip_esp32 = "http://192.168.0.104/ledVermelho"
            requests.get(ip_esp32)
        elif confianca > 10 and classe_detectada == 'metal': 
            ip_esp32 = "http://192.168.0.104/ledAmarelo"
            requests.get(ip_esp32)
        elif confianca > 10 and classe_detectada == 'organico':
            ip_esp32 = "http://192.168.0.104/ledVerde"
            requests.get(ip_esp32)
        else:
            print("Confiança insuficiente para enviar comando para a ESP32.")
    else:
        print("Classe não detectada.")
        ip_esp32 = "http://192.168.0.104/panic"
        requests.get(ip_esp32)
        
        # Gerar um timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        new_filename = f'predictions_{timestamp}.jpg'
        source_file = '/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/predictions.jpg'
        destination_file = os.path.join(predictions_path, new_filename)

        # Mover e renomear o arquivo
        shutil.move(source_file, destination_file)
        print(f'Arquivo movido e renomeado para: {destination_file}')

except subprocess.CalledProcessError as e:
    print("Erro ao executar o comando:\n", e.stderr.decode())
