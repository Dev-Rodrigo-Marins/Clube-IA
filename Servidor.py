from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/button_pressed', methods=['POST'])
def button_pressed():
    # Executa o script Python quando o botão é pressionado
    try:
        subprocess.run(['python3', 'seu_script.py'], check=True)
        return 'Script executado com sucesso!', 200
    except subprocess.CalledProcessError:
        return 'Erro ao executar o script', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Escuta em todas as interfaces na porta 5000
