# PROJETO DE LIXEIRA INTELIGENTE COM IA

## Voce vai precisar dos seguintes componentes

- 01 - PLaca ESP32  
- 01 - Camera OV7670
- 20 - Cabos jumpers femea x femea
- 01 - Fonte de alimentação para placa ESP32
- 01 - Cabo de transmissão de dados USB x Micro USB
- 01 - Instalar o software IDE Arduino e as bibliotecas necessarias

## Tutorial passo a passo

**1 - PASSO INSTALAR O DRIVER DA PLACA ESP32 CONFORME O CHIP CONVERSOR USB**   
Os chips conversores podem ser **CP210X** ou **CH340G** abaixo temos a imagem e o link com mais detalhes para identificar 
o chip conversor da sua placa.

- Inserir imagem dos chips dos conversores USB

[LINK ROBOCORE](https://www.robocore.net/tutoriais/instalando-driver-do-nodemcu?gad_source=1&gclid=CjwKCAiA1-6sBhAoEiwArqlGPoSBKq6nlbg5s1_0agZqCzmkurMGCsVrqhLdadiycJBM9h4euCjFcxoCx_YQAvD_BwE)

os drives podem ser baixados diretamente pelos links abaixo 

**Modelo CP210X**  
[Windows](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CP210x_Windows_Drivers.zip)  
[Mac OSX](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CP210x_Mac_OSX_VCP_Driver.zip)  
[Linux](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CP210x_Linux_2.6.x_VCP_Driver_Source.zip)

**Modelo CH340G**  
[Windows](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CH341SER_WINDOWS.zip)  
[Mac OSX](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CH341SER_MAC.ZIP)  
[Linux](https://s3-sa-east-1.amazonaws.com/robocore-tutoriais/163/CH341SER_LINUX.ZIP)


**2 - PASSO CONECTAR A SUA PLACA ESP32 AO COMPUTADOR E EXECUTAR O PROGRAMA BLINK ( faz o LED piscar )**  
Este passo serve para testar se a interface de programação reconhece a placa com o driver instalado,  testar a transmissao de dados 
via cabo usb para placa, e testar a alimentação e funcionamento basico da placa a ser utilizada!

OBS: Caso tenha total certeza do funcionamento da placa e do cabo de transmissao de dados esta etapa pode ser ignorada ( não recomendavel ).

**3 - PASSO INSTALAR O PROGRAMA IDE ARDUINO**
O programa pode ser baixado diretamente do site oficial clicando no link abaixo  
[IDE_Arduino](https://www.arduino.cc/en/software)
