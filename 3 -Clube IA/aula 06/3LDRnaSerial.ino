int ldrPinos[3] = {A1, A2, A3};  // Pinos dos LDRs
int botaoPino = 2;  // Pino do botão
bool estadoBotao = true;  // Estado inicial do botão (começando a leitura com dados de DIA)
int intervalo = 1000;  // Intervalo entre as medidas em milissegundos

void setup() {
  for (int i = 0; i < 3; i++) {
    pinMode(ldrPinos[i], INPUT);
  }
  pinMode(botaoPino, INPUT);
  Serial.begin(9600);
}

void loop() {
  int ldrValores[3];

  for (int i = 0; i < 3; i++) {
    ldrValores[i] = analogRead(ldrPinos[i]);
  }

  int leituraBotao = digitalRead(botaoPino);

  // Verifica se o botão foi pressionado
  if (leituraBotao == HIGH) {
    // Inverte o estado do botão
    estadoBotao = !estadoBotao;
    delay(300);  // Debounce delay
  }

  // Imprime os valores dos LDRs
  for (int i = 0; i < 3; i++) {
   // Serial.print("LDR "); // habilite se você quiser ver texto
   // Serial.print(i+1);
   // Serial.print(": ");
    Serial.print(ldrValores[i]);
    Serial.print(",   ");
  }

  // Imprime o estado atual do botão
  Serial.println(estadoBotao ? "dia" : "noite");

  // Espera pelo intervalo antes da próxima leitura
  delay(intervalo);  
}


