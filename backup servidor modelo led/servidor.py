from flask import Flask, request
import subprocess
import logging

app = Flask(__name__)

# Configurar o nível de log
logging.basicConfig(level=logging.ERROR)

@app.route('/button_pressed', methods=['POST'])
def button_pressed():
    try:
        subprocess.run(['python3', 'captura_frame.py'], check=True)
        subprocess.run([
            'python3', '/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/darknet/detect.py', 
            '--weights', '/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/darknet/digo-8000.weigths', 
            '--config', '/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/darknet/digo.cfg', 
            '--data', '/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/darknet/digo.data', 
            '--input', '/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/Imagens/imagem.jpg',
            '--output', '/home/rodrigo/Arduino/Octos/codigo_correto_live_esp_ov76701_copy_20240721220344/imagemsaida/'
        ], check=True)
        return 'Script executado com sucesso-serv!', 200
    except subprocess.CalledProcessError:
        return 'Erro ao executar o script-serv', 500

if __name__ == '__main__':
    app.run(debug=False) 
    app.run(host='0.0.0.0', port=5000)
     
