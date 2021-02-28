# activity diagram

## Details
Generator: Plant UML  
Theme : default 

## Code

```plantuml
@startuml

title ESP8266 Activity Diagram 


start
:boot process ;
: configure boot.py;
while (Connected to WiFi)  is (No)
  :Try Again;
endwhile (yes)

while (Execute Main.py) is (yes)
    : handle requests;
endwhile (no)
:interrupt handler/REPL/WebREPL;
while (Power Connected) is (yes)
    :keep running;
endwhile (no)
stop

@enduml
```

## Image

![Activity Diagram](activity.png)