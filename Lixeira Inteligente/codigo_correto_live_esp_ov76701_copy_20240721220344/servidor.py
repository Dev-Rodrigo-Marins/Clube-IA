from flask import Flask, request
import subprocess
import logging
import os

app = Flask(__name__)

# Configurar o nível de log
logging.basicConfig(level=logging.ERROR)

# Diretório base (onde está o servidor.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/button_pressed', methods=['POST'])
def button_pressed():
    try:
        # 🔹 Script de captura de frame (já está no mesmo diretório)
        captura_script = os.path.join(BASE_DIR, "captura_frame.py")

        # 🔹 Caminhos para o Darknet e arquivos de configuração
        darknet_dir = os.path.join(BASE_DIR, "darknet")
        detect_script = os.path.join(darknet_dir, "detect.py")
        weights_file = os.path.join(darknet_dir, "digo-8000.weigths")
        config_file = os.path.join(darknet_dir, "digo.cfg")
        data_file = os.path.join(darknet_dir, "digo.data")

        # 🔹 Caminhos de entrada e saída
        input_image = os.path.join(BASE_DIR, "Imagens", "imagem.jpg")
        output_dir = os.path.join(BASE_DIR, "imagemsaida")

        # Executar o script de captura
        subprocess.run(['python3', captura_script], check=True)

        # Executar o detector
        subprocess.run([
            'python3', detect_script,
            '--weights', weights_file,
            '--config', config_file,
            '--data', data_file,
            '--input', input_image,
            '--output', output_dir
        ], check=True)

        return 'Script executado com sucesso-serv!', 200
    except subprocess.CalledProcessError:
        return 'Erro ao executar o script-serv', 500

if __name__ == '__main__':
    # Rodar em todas as interfaces, porta 5000
    app.run(host='0.0.0.0', port=5000, debug=False)
