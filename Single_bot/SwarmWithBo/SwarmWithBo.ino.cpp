#include <ESP8266WiFi.h>

char command;
const char* ssid = "khadgisujan";       // Replace with your local Wi-Fi network name
const char* password = "CLB279EF91";     // Replace with your local Wi-Fi password
const char* server_ip = "192.168.1.84";  // Replace with your laptop's IP address
const int server_port = 5000;            // Choose a port number

WiFiClient client;

#define IN_1 5   //D1       // L298N in1 motors Right           
#define IN_2 4   //D2       // L298N in2 motors Right          
#define IN_3 0   //D3        // L298N in3 motors Left          
#define IN_4 12  //D6         // L298N in4 motors Left 
#define ena1 13  //D7
#define ena2 15  //D8

void setup() {
  delay(2000);
  Serial.begin(115200);
  pinMode(IN_1, OUTPUT);
  pinMode(IN_2, OUTPUT);
  pinMode(IN_3, OUTPUT);
  pinMode(IN_4, OUTPUT); 
  digitalWrite(IN_1, LOW);
  digitalWrite(IN_2, LOW);
  digitalWrite(IN_3, LOW);
  digitalWrite(IN_4, LOW);
  analogWrite(ena1, 80);  // Reduced PWM value for turning
  analogWrite(ena2, 80);  // Reduced PWM value for turning

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  Serial.println("Connecting to server...");
  while (!client.connect(server_ip, server_port)) {
    Serial.println("Connection failed. Retrying...");
    delay(1000);
  }
  Serial.println("Connected to server");
}

void loop() {
  while (client.available() > 0) {
    command = client.read();
    Serial.print(command);
  }
  delay(500);
  if (command == 'F' || command == 'f') {
    goAhead();
    Serial.println("Moving Forward");
  } 
  else if (command == 'B' || command == 'b') {
    goBack();
    Serial.println("Moving Backward");
  }
  else if (command == 'L' || command == 'l') {
    goLeft();
    Serial.println("Moving Left");
  }
  else if (command == 'R' || command == 'r') {
    goRight(); 
    Serial.println("Moving Right");
  }
  else if (command == 'S' || command == 's') {
    stopRobot();
    Serial.println("STOP!");
  }
}

void goLeft() {
  digitalWrite(IN_1, LOW);
  digitalWrite(IN_2, HIGH);
  digitalWrite(IN_3, LOW);
  digitalWrite(IN_4, HIGH);
}

void goRight() {
  digitalWrite(IN_1, HIGH);
  digitalWrite(IN_2, LOW);
  digitalWrite(IN_3, HIGH);
  digitalWrite(IN_4, LOW);
}

void goBack() {
  digitalWrite(IN_1, LOW);
  digitalWrite(IN_2, HIGH);
  digitalWrite(IN_3, HIGH);
  digitalWrite(IN_4, LOW);
}

void goAhead() {
  digitalWrite(IN_1, HIGH);
  digitalWrite(IN_2, LOW);
  digitalWrite(IN_3, LOW);
  digitalWrite(IN_4, HIGH);
}

void stopRobot() {
  digitalWrite(IN_1, HIGH);
  digitalWrite(IN_2, HIGH);
  digitalWrite(IN_3, HIGH);
  digitalWrite(IN_4, HIGH);
}
