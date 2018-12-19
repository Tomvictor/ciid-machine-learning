import oscP5.*;
import netP5.*;

float c ;
float new_c ;
OscP5 oscP5;

void setup() {
  size(500,500);
  oscP5 = new OscP5(this,12000);
}

void draw(){
  
    background(255,0,c*500);
    //ellipse(56, 46, 55, 55);
}


/* incoming osc message are forwarded to the oscEvent method. */
//this is where we recive data from the wekkinator
void oscEvent(OscMessage msg) {
  if(msg.addrPattern().equals("/wek/outputs")){
  c = msg.get(0).floatValue();
  }

}
