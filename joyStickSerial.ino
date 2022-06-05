// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

int maxVal=1700;

int left_x = 0;
int left_y = 0;
int left_z = 0;

int right_x = 0;
int right_y = 0;
int right_z = 0;

// the loop routine runs over and over again forever:
void loop() 
{
  readAxisData();
  printAxis();
}


void readAxis(int pin, int mid, int jitter, int z_band, int &prevReading)
{
   int currentReading =  analogRead(pin);
   
   currentReading = currentReading - mid;
   
   // limit jitter
   if (currentReading < prevReading - jitter || currentReading > prevReading + jitter)
   {
      prevReading = currentReading;
   }
   // z-banding
   if ((prevReading > 0  && prevReading < z_band) || (prevReading < 0 && prevReading > -z_band))
   {
      prevReading  = 0;
   }
   
   if(prevReading > maxVal)
   {
      prevReading=maxVal;
   }

   if(prevReading < -maxVal)
   {
      prevReading = -maxVal;
   }
   delay(6); 
}

void readAxisData()
{
   readAxis(34, 1860,10,200,left_x);
   readAxis(35, 1776,10,200,left_y);
   readAxis(32, 1855,10,200,left_z);   
   
   readAxis(33, 1801,10,200,right_x);
   readAxis(25, 1900,10,200,right_y);
   readAxis(26, 1860,10,200,right_z);
   /*
   // get real values to find mid point and jitter values for each axis
   leftt_x =  analogRead(34);
   left_y =  analogRead(35);
   left_z =  analogRead(32);
 
   right_x =  analogRead(33);
   right_y =  analogRead(25);

   
   right_z =  analogRead(26);
   */
    
}

void printAxis()
{
  Serial.print(left_x);
  Serial.print(" ");
  Serial.print(left_y);
  Serial.print(" ");
  Serial.print(left_z);
  Serial.print(" ");
  Serial.print(right_x);
  Serial.print(" ");
  Serial.print(right_y);
  Serial.print(" ");
  Serial.println(right_z);
}
