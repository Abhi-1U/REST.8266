# use case diagram

## Details
Generator: Plant UML  
Theme : default 

## Code

```plantuml
@startuml

title Use Case Diagram

left to right direction
actor "User" as fc
rectangle REST.8266 {
  usecase "Access Hardware" as UC1
  usecase "Read Data" as UC2
  usecase "Change Settings" as UC3
  usecase "Instruct Controller" as UC4
  usecase "Edit Programs" as UC5
  usecase "Access WebREPL" as UC6
}
fc --> UC1
fc --> UC2
fc --> UC3
fc --> UC4
fc --> UC5
fc --> UC6
@enduml
```

## Image

![Use case Diagram](usecase.png)