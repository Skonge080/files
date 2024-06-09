const int trigPin = 9;
const int echoPin = 10;

void setup() {
  // Инициализация последовательного соединения для вывода данных в монитор порта
  Serial.begin(9600);
  
  // Инициализация пинов
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Переменные для измерения времени
  long duration;
  int distance;
  
  // Посылаем ультразвуковой импульс
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Считываем время возврата импульса
  duration = pulseIn(echoPin, HIGH);
  
  // Рассчитываем расстояние в сантиметрах
  distance = duration * 0.034 / 2;
  
  // Выводим данные в монитор порта
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  // Задержка перед следующим измерением
  delay(500);
}
