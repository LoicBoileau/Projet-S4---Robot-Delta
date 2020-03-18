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

#define LENGTH_MESSAGE  8
#define DECA_MOT3       200

uint8_t dxl_id1 = DXL_ID1;
uint8_t dxl_id2 = DXL_ID2;
uint8_t dxl_id3 = DXL_ID3;

int32_t theta1 = 0;
int32_t theta2 = 0;
int32_t theta3 = 0;

int32_t msgArg1 = 0;
int32_t msgArg2 = 0;
int32_t msgArg3 = 0;

int cmdNb = 0;

uint32_t maxPosMotor1 = 2500;
uint32_t maxPosMotor2 = 2500;
uint32_t maxPosMotor3 = 2500;

uint32_t minPosMotor1 = 1000;
uint32_t minPosMotor2 = 1000;
uint32_t minPosMotor3 = 800; //valeur des autres moteurs - DECA_MOT3(200)

DynamixelWorkbench dxl_wb;

bool commandReceived = false;

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
      dxl_wb.goalPosition(dxl_id3, (int32_t)800);
      delay(3000);

      dxl_wb.goalPosition(dxl_id1, (int32_t)2000);
      dxl_wb.goalPosition(dxl_id2, (int32_t)2000);
      dxl_wb.goalPosition(dxl_id3, (int32_t)1800);
      delay(3000);
    }
  }
  
}

void loop() 
{

  if (Serial.available() > 0){
    cmdNb = readData(); //read the available data and return the first short received as the command number

    if ( cmdNb >= 2 ) //make sure the angle received are in a good range and command is for moving motors
      Serial.write((byte)cmdNb);  //write the command Number to confirmed you have received it
      theta1 = msgArg1;
      theta2 = msgArg2;
      theta3 = msgArg3;
      commandReceived = true;
      delay(10);
    }
    else if( cmdNb == 1 ){ //if the command is for something else then dont activate the motors
      Serial.write((byte)cmdNb);
      delay(10);
    }
  
  if (commandReceived){
    checkMaxPosMotors();
        
    dxl_wb.goalPosition(dxl_id1, (int32_t)theta1);
    dxl_wb.goalPosition(dxl_id2, (int32_t)theta2);
    dxl_wb.goalPosition(dxl_id3, (int32_t)theta3-DECA_MOT3);
    
    commandReceived = false;
  }
}

int readData()
{
  byte bytesBuffer[LENGTH_MESSAGE];
  int i = 0;
  while (Serial.available()) {
    delay(10);  
    if (Serial.available() >0) {
      byte Byte = Serial.read();  //gets one byte from serial buffer
      bytesBuffer[i++] = Byte; //makes the string readString
      //Serial.println(bytesBuffer[i]);
    }  
  }
  //Prendre le premier octet et le décaller de 8 bits.
  int commandNb = int((unsigned char)(bytesBuffer[1]) << 8 | (unsigned char)(bytesBuffer[0]));
  
  msgArg1 = int((unsigned char)(bytesBuffer[3]) << 8 | (unsigned char)(bytesBuffer[2])); 
  msgArg2 = int((unsigned char)(bytesBuffer[5]) << 8 | (unsigned char)(bytesBuffer[4]));
  msgArg3 = int((unsigned char)(bytesBuffer[7]) << 8 | (unsigned char)(bytesBuffer[6]));

  return (commandNb);
}

bool checkMaxPosMotors()
{
  bool motorCommandInRange = true;
  if (theta1 > maxPosMotor1){
    theta1 = maxPosMotor1;
    motorCommandInRange = false;
  }
  else if (theta1 < minPosMotor1){
    theta1 = minPosMotor1;
    motorCommandInRange = false;
  }
  if (theta2 > maxPosMotor2){
    theta2 = maxPosMotor2;
    motorCommandInRange = false;
  }
  else if (theta2 < minPosMotor2){
    theta2 = minPosMotor2;
    motorCommandInRange = false;
  }
  if (theta3 > maxPosMotor3){
    theta3 = maxPosMotor3;
    motorCommandInRange = false;
  }
  else if (theta3 < minPosMotor3){
    theta3 = minPosMotor3;
    motorCommandInRange = false;
  }
  return (motorCommandInRange);
}
