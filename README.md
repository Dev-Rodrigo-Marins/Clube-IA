# PROJETO DE LIXEIRA INTELIGENTE COM IA

## Voce vai precisar dos seguintes componentes

- 01 - PLaca ESP32  💻
- 01 - Camera OV7670 📸
- 20 - Cabos jumpers femea x femea 🔌
- 01 - Fonte de alimentação para placa ESP32
- 01 - Cabo de transmissão de dados USB x Micro USB 🔌
- 01 - Instalar o software IDE Arduino e as bibliotecas necessarias 👨‍💻
- 01 - Instalar o python 3.09 ou superior 👨‍💻
- 01 - Instalar as bibliotecas pyhton REQUESTS, IMAGE, BytesIO 👨‍💻

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
- USAR A BIBLIOTECA CONTROLADORA DE PLACA ESP32 DA EXPRESSIF NA VERSAO 2.0.17... versões superiores tiveram alterações nas modulos e quebram a aplicação atual.




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

<img src="src/imagens/DualtechTalk.png" alt="Minha Figura">
<img src="src/imagens/DualtechTalk2.png" alt="Minha Figura">

imagens retiradas do canal - [Dual_Tech_talk](https://www.youtube.com/@duotechtalk)

Será necessario configurar a saida em 115200 Pounds na interface do monitor serial no Ide Arduino para conseguir visualizar o IP da placa
para realizar a conexão com a camera via http, acessando o link no seu navegador padrao http://ip.da.sua.esp32/camera  
conforme as imagens na sequencia. (isso evita que voce tenha dor de cabeça com a porta serial).  



@@**8 - PASSO Atenção será necessario ajustar o codigo captura_frame.py**@@💻👨‍💻🔌  
- Ajuste o ip da esp32 no codigo do arquivo captura_frame.py.
- Ajuste o caminho onde o frame capturado vai ser salvo ( ajustando conforme o caminho no seu SO).

<img src="src/imagens/Capturapyframe.png" alt="Minha Figura">
  

  
```diff
@@**9 - PASSO baixar imagens para o dataset conforme o tipo de lixo seco, organico,papel,metal**@@💻👨‍💻🔌
- Baixar imagens com a biblioteca do bing usando python.
- Usar o LabelImg para realizar a classificação manual da imagem para pré-treinamento dos dados com YOLO. 
- Utilize bibliotecas populares de aprendizado de máquina, como TensorFlow ou PyTorch, para criar e treinar seu modelo.
```

```diff
@@**10 - PASSO escrever o codigo para que o modelo de ML pegue a imagem da camera e a classifique**@@💻👨‍💻🔌  
- Integre o modelo treinado com o código Python para que ele possa receber imagens da câmera e fornecer classificações.
- Teste o modelo com diferentes tipos de lixo para garantir sua precisão.
```

```diff
@@**11 - PASSO escrever o codigo de retorno do ML para a ESP32, sinalizando a classificação do lixo obtida**@@💻👨‍💻🔌  
- Configure uma comunicação entre o código Python e a ESP32 para enviar a classificação de volta.  
- Pode ser útil usar um formato de mensagem simples, como JSON, para transmitir as informações.
- Poder ser possivel criar 4 links https para cada tipo de saida de lixo. e uma para uma saida não identificada! 
```

```diff
@@**12 - PASSO como tratar as imagens que o modelo não conseguir identificar*@@💻👨‍💻🔌  
- Salvar numa pasta no computador onde estara rodando o modelo... e notificar o adm para retreino do modelo quando atingir 100 arquivos.  
- validar salvar em banco pode tornar lento... capacidade do processador livree ???.
```
