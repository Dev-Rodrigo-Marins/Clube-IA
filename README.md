# PROJETO DE LIXEIRA INTELIGENTE COM IA

## Voce vai precisar dos seguintes componentes

- 01 - PLaca ESP32  💻
- 01 - Camera OV7670 📸
- 20 - Cabos jumpers femea x femea 🔌
- 01 - Fonte de alimentação para placa ESP32
- 01 - Cabo de transmissão de dados USB x Micro USB 🔌
- 01 - Instalar o software IDE Arduino e as bibliotecas necessarias 👨‍💻

## Tutorial passo a passo

**1 - PASSO INSTALAR O DRIVER DA PLACA ESP32 CONFORME O CHIP CONVERSOR USB**💻   
Os chips conversores podem ser **CP210X** ou **CH340G**   abaixo temos o link com mais detalhes para identificar 
o chip conversor da sua placa.

<img src="src/imagens/conversor_usb_esp32.png" alt="Minha Figura">

- [LINK ROBOCORE](https://www.robocore.net/tutoriais/instalando-driver-do-nodemcu?gad_source=1&gclid=CjwKCAiA1-6sBhAoEiwArqlGPoSBKq6nlbg5s1_0agZqCzmkurMGCsVrqhLdadiycJBM9h4euCjFcxoCx_YQAvD_BwE)

os drives podem ser baixados diretamente pelos links abaixo 

**Modelo CP210X**  
- [Windows](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CP210x_Windows_Drivers.zip)  
- [Mac OSX](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CP210x_Mac_OSX_VCP_Driver.zip)  
- [Linux](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CP210x_Linux_2.6.x_VCP_Driver_Source.zip)

**Modelo CH340G**  
- [Windows](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CH341SER_WINDOWS.zip)  
- [Mac OSX](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CH341SER_MAC.ZIP)  
- [Linux](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CH341SER_LINUX.ZIP)




**2 - PASSO CONECTAR A SUA PLACA ESP32 AO COMPUTADOR E EXECUTAR O PROGRAMA BLINK**( faz o LED piscar )💻👨‍💻🔌  
Este passo serve para testar se a interface de programação reconhece a placa com o driver instalado,  testar a transmissao de dados 
via cabo usb para placa, e testar a alimentação e funcionamento basico da placa a ser utilizada!

OBS: Caso tenha total certeza do funcionamento da placa e do cabo de transmissao de dados esta etapa pode ser ignorada ( não recomendavel ).



**3 - PASSO INSTALAR O PROGRAMA IDE ARDUINO**👨‍💻  
O programa pode ser baixado diretamente do site oficial clicando no link abaixo    
- [IDE_Arduino](https://www.arduino.cc/en/software)



**4 - PASSO INSTALAR AS BIBLIOTECAS NA IDE ARDUINO**👨‍💻  
siga o tutorial no site abaixo para instalar as bibliotecas necessarias para a IDE Arduino reconhecere corretamente sua placa ESP   
- [DOIT ESP32 DEVKIT v1](https://lobodarobotica.com/blog/como-instalar-esp32-ide-arduino/)  



**5 - PASSO INSTALAR AS BIBLIOTECAS NA IDE ARDUINO** 👨‍💻
- Adafruit GFX (Adafruit_GFX.h) 
- Adafruit ST7735 (Adafruit_ST7735.h)



 **6 - PASSO CONECTAR A PLACA ESP32 A CAMERA OV7670**💻👨‍💻🔌
 - Inserir imagem do diagrama de conexao ESP32 + OV7670
<img src="src/imagens/diagramacao.png" alt="Minha Figura">


  **7 - PASSO INSERIR SSID E SENHA DA REDE WIFI PARA CONEXÃO VIA HTTP COM A CAMERA NO CODIGO**💻👨‍💻🔌  
  Modificar o arquivo ESP_L2S_Camera.ino nas linhas 34 e 35   incluindo o SSID ( nome da rede WIFI) e a senha dentro do codigo.  
<img src="src/imagens/nswifi.png" alt="Minha Figura">
  
Após realizado esse procedimento, o codigo deve ser compilado e enviado a placa esp32... na interface do IDE ARDUINO
quando aparecer a mensagem Conecting... ( enquanto estiver carregando os pontinhos, pressione o botão BOOT na placa)  
isso vai permitir que o codigo seja gravado na placa corretamente!  

- Inserir a imagem da gravação do codigo na ESP32 pelo IDE Arduino ( Conecting )

Será necessario configurar a saida em 11520 Pounds na interface do Ide Arduino para conseguir visualizar o IP da placa
para realizar a conexão com a camera via http, acessando o link no seu navegador padrao http://xxx.xxx.xxx.xxx/camera  
conforme as imagens na sequencia.  

- Inserir imagem da configuração dos pounds na IDE Arduino
- Inserir imagem da mensagem do IP da camera na serial ploter
- Inserir imagem do acesso a camera via navegador pelo link.

**8 - PASSO escrever o codigo em python para acessar o link e salvar a imagem da camera em uma pasta especifica**💻👨‍💻🔌
**9 - PASSO criar um modelo de machine learning para identificar o tipo de lixo seco, organico,papel,metal**💻👨‍💻🔌
**10 - PASSO escrever o codigo para que o modelo de ML pegue a imagem da camera e a classifique**💻👨‍💻🔌
**11 - PASSO escrever o codigo de retorno do ML para a ESP32, sinalizando a classificação do lixo obtida**💻👨‍💻🔌  

