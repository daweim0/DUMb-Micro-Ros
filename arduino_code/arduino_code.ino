#include "ArduinoJsonv6.h"
#include "dummr.h"

// This is an example

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  dummr_init();
  sub_message("/get_string_len/input", "std_msgs/String");
}


void loop() {

  if (dummr_check_for_msg()) {
      String topic = String((const char*) dummr_last_topic["topic"]);

      if (topic.equals("/get_string_len/input")) {
        // use the arduinojson assistant to figure out how big StaticJsonDocument should be - https://arduinojson.org/v6/assistant/
        StaticJsonDocument<256> return_doc;
        return_doc["data"] = dummr_last_message_data["data"]; 
        pub_message("/get_string_len/echo", "std_msgs/String", return_doc);
  
        StaticJsonDocument<64> return_doc2;
        return_doc["data"] = strlen(dummr_last_message_data["data"]); 
        pub_message("/get_string_len/output", "std_msgs/Int32", return_doc); 
      }
  }
  else {
    delay(1);  // probaby a good idea to have some delay here, so the computer doesn't get overwhelmed
  }
   
}



