// Определение пинов
const int sensorPin = A0; // Пин считывания данных с датчика
const int ledPin = 13;     // Пин светодиода (для индикации)

void setup() {
  // Настройка монитора последовательного порта
  Serial.begin(9600);
  
  // Настройка пина для светодиода
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Считывание значения с датчика
  int sensorValue = analogRead(sensorPin);
  
  // Проверка значения на влажность
  if (sensorValue > 500) {
    digitalWrite(ledPin, HIGH); // Включение светодиода
    Serial.println("Вода обнаружена!"); // Вывод сообщения
  } else {
    digitalWrite(ledPin, LOW); // Выключение светодиода
    Serial.println("Вода не обнаружена."); // Вывод сообщения
  }
  
  // Задержка между измерениями
  delay(1000);
}
