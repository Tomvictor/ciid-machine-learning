import oscP5.*;
import netP5.*;

int c ;
OscP5 oscP5;

void setup() {
  size(500,500);
  oscP5 = new OscP5(this,12000);
}

void draw(){
  
  if (c==1){
    background(255,0,0);
  }else if(c==2){
    background(0,255,0);
  }else if(c==3){
    background(0,0,255);
  }
}


/* incoming osc message are forwarded to the oscEvent method. */
//this is where we recive data from the wekkinator
void oscEvent(OscMessage msg) {
  if(msg.addrPattern().equals("/wek/outputs")){
  c = (int) msg.get(0).floatValue();
  }

}
