/* Authors: Loic Boileau */

#include <DynamixelWorkbench.h>

#if defined(__OPENCM904__)
  #define DEVICE_NAME "3" //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
#elif defined(__OPENCR__)
  #define DEVICE_NAME ""
#endif   

#define BAUDRATE        57600
#define DXL_ID1         2
#define DXL_ID2         3
#define DXL_ID3         1

#define LENGTH_MESSAGE  4

uint8_t dxl_id1 = DXL_ID1;
uint8_t dxl_id2 = DXL_ID2;
uint8_t dxl_id3 = DXL_ID3;

int theta1 = 0;
int theta2 = 0;
int theta3 = 0;

uint8_t maxPosMotor1 = 2000;
uint8_t maxPosMotor2 = 2000;
uint8_t maxPosMotor3 = 1750;

uint8_t minPosMotor1 = 1000;
uint8_t minPosMotor2 = 1000;
uint8_t minPosMotor3 = 750;

DynamixelWorkbench dxl_wb;

String readString = "";

void setup() 
{  
  Serial.begin(57600);
  // while(!Serial); // Wait for Opening Serial Monitor

  Serial.println('Reset of the Open CR');

  const char *log;
  bool result = false;
  
  uint16_t model_number_id1 = 0;
  uint16_t model_number_id2 = 0;
  uint16_t model_number_id3 = 0;

  float decalage_id1 = 0;

  result = dxl_wb.init(DEVICE_NAME, BAUDRATE, &log);
  if (result == false)
  {
    Serial.println(log);
    Serial.println("Failed to init");
  }
  else
  {
    Serial.print("Succeeded to init : ");
    Serial.println(BAUDRATE);  
  }

  result = dxl_wb.ping(dxl_id1, &model_number_id1, &log)&& dxl_wb.ping(dxl_id2, &model_number_id2, &log) && dxl_wb.ping(dxl_id3, &model_number_id3, &log) ;
  if (result == false)
  {
    Serial.println(log);
    Serial.println("Failed to ping");
  }
  else
  {
    Serial.println("Succeeded to ping");
    Serial.print("id motor1 : ");
    Serial.print(dxl_id1);
    Serial.print(" model_number : ");
    Serial.println(model_number_id1);
    Serial.print("id motor2 : ");
    Serial.print(dxl_id2);
    Serial.print(" model_number : ");
    Serial.println(model_number_id2);
    Serial.print("id motor3 : ");
    Serial.print(dxl_id3);
    Serial.print(" model_number : ");
    Serial.println(model_number_id3);
  }

  result = dxl_wb.jointMode(dxl_id1, 0, 0, &log) && dxl_wb.jointMode(dxl_id2, 0, 0, &log) && dxl_wb.jointMode(dxl_id3, 0, 0, &log);
  if (result == false)
  {
    Serial.println(log);
    Serial.println("Failed to change joint mode");
  }
  else
  {
    Serial.println("Succeed to change joint mode");
    Serial.println("Dynamixel is moving...");

    for (int count = 0; count < 1; count++)
    {
      dxl_wb.goalPosition(dxl_id1, (int32_t)1000);
      dxl_wb.goalPosition(dxl_id2, (int32_t)1000);
      dxl_wb.goalPosition(dxl_id3, (int32_t)750);
      delay(3000);

      dxl_wb.goalPosition(dxl_id1, (int32_t)2000);
      dxl_wb.goalPosition(dxl_id2, (int32_t)2000);
      dxl_wb.goalPosition(dxl_id3, (int32_t)1750);
      delay(3000);
    }
  }
  
}

void loop() 
{

  
  if (Serial.available() > 0){
    delay(4000);

    byte bytesBuffer[LENGTH_MESSAGE];
    int i = 0;
    while (Serial.available()) {
      delay(10);  
      if (Serial.available() >0) {
        byte Byte = Serial.read();  //gets one byte from serial buffer
        bytesBuffer[i++] = Byte; //makes the string readString
        Serial.println(bytesBuffer[i]);
      }  
    }
    
    //Prendre le premier octet et le décaller de 8 bits.
    int n1 = int((unsigned char)(bytesBuffer[1]) << 8 | (unsigned char)(bytesBuffer[0])); 
    int n2 = int((unsigned char)(bytesBuffer[3]) << 8 | (unsigned char)(bytesBuffer[2]));
    Serial.println(n1);
    Serial.println(n2);

    checkMaxPosMotors();

    /*
    int32_t message = Serial.readBytes(2);
    Serial.print(message);
    Serial.print(":(BIN) ");
    Serial.println(message,BIN);

    
    dxl_wb.goalPosition(dxl_id1, (int32_t)1000);
    dxl_wb.goalPosition(dxl_id2, (int32_t)1000);
    dxl_wb.goalPosition(dxl_id3, (int32_t)750);
    delay(3000);

    dxl_wb.goalPosition(dxl_id1, (int32_t)2000);
    dxl_wb.goalPosition(dxl_id2, (int32_t)2000);
    dxl_wb.goalPosition(dxl_id3, (int32_t)1750);
    delay(3000);*/
  }
}

void readData()
{
  
}

void checkMaxPosMotors()
{
  if (theta1 > maxPosMotor1){
    theta1 = maxPosMotor1;
  }
  else if (theta1 < minPosMotor1){
    theta1 = minPosMotor1;
  }
  if (theta2 > maxPosMotor2){
    theta2 = 2200;
  }
  else if (theta2 < minPosMotor2){
    theta1 = minPosMotor1;
  }
  if (theta3 > maxPosMotor3){
    theta3 = 2200;
  }
  else if (theta3 < minPosMotor3){
    theta1 = minPosMotor1;
  }
}
