#include "OV7670.h"
#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library
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
const int TFT_DC = 2;
const int TFT_CS = 5;

#define ssid1        "VempraUno_5764"  // Nome da rede Wifi
#define password1    "18801705" // Senha da rede Wifi

const char* serverUrl = "http://192.168.0.105:5000/button_pressed";  // Substitua <SEU_IP_LOCAL> pelo IP do seu computador
const int buttonPin = 5;  // Ajuste o pino conforme sua configuração para colocar o pino de start(touch)

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS,  TFT_DC, 0/*no reset*/);
OV7670 *camera;

WiFiMulti wifiMulti;
WiFiServer server(80);

unsigned char bmpHeader[BMP::headerSize];

void serve()
{
  WiFiClient client = server.available();
  if (client) 
  {
    //Serial.println("New Client.");
    String currentLine = "";
    while (client.connected()) 
    {
      if (client.available()) 
      {
        char c = client.read();
        //Serial.write(c);
        if (c == '\n') 
        {
          if (currentLine.length() == 0) 
          {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println();
            client.print(
             "<style>body{margin: 0}\nimg{height: 50%; width: auto}</style>"
             "<img id='a' src='/camera' onload='this.style.display=\"initial\"; var b = document.getElementById(\"b\"); b.style.display=\"none\"; b.src=\"camera?\"+Date.now(); '>"
             "<img id='b' style='display: none' src='/camera' onload='this.style.display=\"initial\"; var a = document.getElementById(\"a\"); a.style.display=\"none\"; a.src=\"camera?\"+Date.now(); '>");
            

            
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
        
        if(currentLine.endsWith("GET /camera"))
        {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:image/bmp");
            client.println();
            
            client.write(bmpHeader, BMP::headerSize);
            client.write(camera->frame, camera->xres * camera->yres * 2);
        }
      }
    }
    // close the connection:
    client.stop();
    //Serial.println("Client Disconnected.");
  }  
}

void setup() 
{
    delay(5000);
    Serial.begin(115200);
   wifiMulti.addAP(ssid1, password1);
 
  if(wifiMulti.run() == WL_CONNECTED) {
     Serial.println(WiFi.localIP());
     }
  
  camera = new OV7670(OV7670::Mode::QQVGA_RGB565, SIOD, SIOC, VSYNC, HREF, XCLK, PCLK, D0, D1, D2, D3, D4, D5, D6, D7);
  BMP::construct16BitHeader(bmpHeader, camera->xres, camera->yres);
  
  tft.initR(INITR_BLACKTAB);
  tft.fillScreen(0);
  server.begin();

  pinMode(buttonPin, INPUT_PULLUP);  // Configura o pino do botão como entrada com resistor pull-up

}

void displayY8(unsigned char * frame, int xres, int yres)
{
  tft.setAddrWindow(0, 0, yres - 1, xres - 1);
  int i = 0;
  for(int x = 0; x < xres; x++)
    for(int y = 0; y < yres; y++)
    {
      i = y * xres + x;
      unsigned char c = frame[i];
      unsigned short r = c >> 3;
      unsigned short g = c >> 2;
      unsigned short b = c >> 3;
      tft.pushColor(r << 11 | g << 5 | b);
    }  
}

void displayRGB565(unsigned char * frame, int xres, int yres)
{
  tft.setAddrWindow(0, 0, yres - 1, xres - 1);
  int i = 0;
  for(int x = 0; x < xres; x++)
    for(int y = 0; y < yres; y++)
    {
      i = (y * xres + x) << 1;
      tft.pushColor((frame[i] | (frame[i+1] << 8)));
    }  
}
  
void loop()
{
  camera->oneFrame();
  serve();
  displayRGB565(camera->frame, camera->xres, camera->yres);


  if (digitalRead(buttonPin) == LOW) {  // Verifica se o botão foi pressionado
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    
    int httpResponseCode = http.POST("button=pressed");
    
    if (httpResponseCode > 0) {
      Serial.println("Requisição POST enviada");
    } else {
      Serial.println("Erro ao enviar requisição");
    }
    
    http.end();
    
    delay(1000);  // Debounce para evitar múltiplas requisições
  }
}
