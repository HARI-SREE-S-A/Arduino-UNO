#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <printf.h>



#if defined(__AVR_ATmega328P__) || defined(__AVR_ATmega328PB__) ||defined(__AVR_ATmega2560__) || defined(__AVR_ATmega1280__)
#define CSN 10
#define CE  9
#elif defined(ESP32)
#define CSN 5
#define CE  4
#else
#error "Make Config you're self"
#endif

#define Debug_mode false

/*Create a unique pipe out. The receiver has to
  wear the same unique code*/
const uint64_t pipeIn = 0x662266; //IMPORTANT: The same as in the receiver!!!
/*//////////////////////////////////////////////////////*/

/*Create the data struct we will send
  The sizeof this struct should not exceed 32 bytes
  This gives us up to 32 8 bits channals */
RF24 radio(CE, CSN); // select  CSN and CE  pins


/*//////////////////////////////////////////////////////*/
//Create a struct to send over NRF24
struct MyData {
  byte test;
};
MyData data;
/*//////////////////////////////////////////////////////*/

//This function will only set the value to  0 if the connection is lost...
void resetData()
{
  data.test = 0;
}

