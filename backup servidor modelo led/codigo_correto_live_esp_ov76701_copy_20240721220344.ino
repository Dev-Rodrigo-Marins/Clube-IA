#include "OV7670.h"
#include <WiFi.h>
#include <WiFiMulti.h>
#include <WiFiClient.h>
#include "BMP.h"
#include <HTTPClient.h>

const int SIOD = 21; //SDA
const int SIOC = 22; //SCL
const int VSYNC = 34;
const int HREF = 35;
const int XCLK = 32;
const int PCLK = 33;
const int D0 = 27;
const int D1 = 25;
const int D2 = 26;
const int D3 = 15;
const int D4 = 14;
const int D5 = 13;
const int D6 = 12;
const int D7 = 4;

const int ledAzul = 23;
const int ledVerde = 2;
const int ledAmarelo = 18;
const int ledVermelho = 19;

const char* serverUrl = "http://192.168.0.105:5000/button_pressed";  // Substitua <SEU_IP_LOCAL> pelo IP do seu computador
const int buttonPin = 5;  // Ajuste o pino conforme sua configuração para colocar o pino de start(touch)

#define ssid1        "VempraUno_5764"  // Nome da rede Wifi
#define password1    "18801705" // Senha da rede Wifi

OV7670 *camera;

WiFiMulti wifiMulti;
WiFiServer server(80);

unsigned char bmpHeader[BMP::headerSize];

void serve()
{
    WiFiClient client = server.available();
    if (client) 
    {
        String currentLine = "";
        while (client.connected()) 
        {
            if (client.available()) 
            {
                char c = client.read();
                if (c == '\n') 
                {
                    if (currentLine.length() == 0) 
                    {
                        client.println("HTTP/1.1 200 OK");
                        client.println("Content-type:text/html");
                        client.println();
                        break;
                    } 
                    else 
                    {
                        currentLine = "";
                    }
                } 
                else if (c != '\r') 
                {
                    currentLine += c;
                }

                                // Checagem da requisição de câmera
                if (currentLine.endsWith("GET /camera"))
                {
                    client.println("HTTP/1.1 200 OK");
                    client.println("Content-type:image/bmp");
                    client.println();
                    
                    client.write(bmpHeader, BMP::headerSize);
                    client.write(camera->frame, camera->xres * camera->yres * 2);
                }  

                // Checagem das requisições de LEDs
                if (currentLine.endsWith("GET /ledAzul")) 
                {
                    client.println();
                    client.println("<html><body><h1>LED Azul ligado!</h1></body></html>");
                    digitalWrite(ledAzul, HIGH);
                    delay(1000); // Liga o LED por 1 segundo
                    digitalWrite(ledAzul, LOW);
                } 
                else if (currentLine.endsWith("GET /ledAmarelo")) 
                {
                    client.println();
                    client.println("<html><body><h1>LED Amarelo ligado!</h1></body></html>");
                    digitalWrite(ledAmarelo, HIGH);
                    delay(1000); // Liga o LED por 1 segundo
                    digitalWrite(ledAmarelo, LOW);
                } 
                else if (currentLine.endsWith("GET /ledVerde")) 
                {
                    client.println();
                    client.println("<html><body><h1>LED Verde ligado!</h1></body></html>");
                    digitalWrite(ledVerde, HIGH);
                    delay(1000); // Liga o LED por 1 segundo
                    digitalWrite(ledVerde, LOW);
                } 
                else if (currentLine.endsWith("GET /ledVermelho")) 
                {
                    client.println();
                    client.println("<html><body><h1>LED Vermelho ligado!</h1></body></html>");
                    digitalWrite(ledVermelho, HIGH);
                    delay(1000); // Liga o LED por 1 segundo
                    digitalWrite(ledVermelho, LOW);
                }
                else if (currentLine.endsWith("GET /panic")) 
                {
                    client.println();
                    client.println("<html><body><h1>LED Vermelho ligado!</h1></body></html>");
                    digitalWrite(ledVermelho, HIGH);
                    delay(500);
                    digitalWrite(ledVermelho, LOW);
                    digitalWrite(ledAmarelo, HIGH);
                    delay(500);
                    digitalWrite(ledAmarelo, LOW);
                    digitalWrite(ledAzul, HIGH);
                    delay(500);
                    digitalWrite(ledAzul, LOW);
                    digitalWrite(ledVerde, HIGH);
                    delay(500);
                    digitalWrite(ledVerde, LOW);
                    delay(500); // Liga o LED por 1 segundo
                    
                    
                   
                    
                }                
            }
        }

        client.stop();
    }  
}

void setup() 
{
    // Configuração dos LEDs como saída
    pinMode(ledAzul, OUTPUT);
    pinMode(ledAmarelo, OUTPUT);
    pinMode(ledVerde, OUTPUT);
    pinMode(ledVermelho, OUTPUT);

    digitalWrite(ledAzul, LOW);
    digitalWrite(ledAmarelo, LOW);
    digitalWrite(ledVerde, LOW);
    digitalWrite(ledVermelho, LOW);

    delay(1000);
    Serial.begin(115200);
    wifiMulti.addAP(ssid1, password1);

    if (wifiMulti.run() == WL_CONNECTED) {
        Serial.println(WiFi.localIP());
    }
  
    camera = new OV7670(OV7670::Mode::QQVGA_RGB565, SIOD, SIOC, VSYNC, HREF, XCLK, PCLK, D0, D1, D2, D3, D4, D5, D6, D7);
    BMP::construct16BitHeader(bmpHeader, camera->xres, camera->yres);
  
    server.begin();
    pinMode(buttonPin, INPUT_PULLUP);  // Configura o pino do botão como entrada com resistor pull-up
}

void loop()
{
    camera->oneFrame();
    serve();

    if (digitalRead(buttonPin) == LOW) {  // Verifica se o botão foi pressionado
        HTTPClient http;
        http.begin(serverUrl);
        http.addHeader("Content-Type", "application/x-www-form-urlencoded");
        
        int httpResponseCode = http.POST("button=pressed");
        
            if (httpResponseCode == 200) {
                Serial.printf("Requisição POST enviada. Código de resposta: %d\n", httpResponseCode);
                String response = http.getString();  // Captura a resposta do servidor
                Serial.println("Resposta do servidor: " + response);
            } else {
                Serial.printf("Erro ao enviar requisição. Código de erro: %d\n", httpResponseCode);
            }
            
            http.end();
        
        http.end();
        
        delay(1000);  // Debounce para evitar múltiplas requisições
    }
}
