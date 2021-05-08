var Host_IP = "http://192.168.43.97"; 

// LED status
$(".ledstatus").click(function(){
  var settings = {
  "url": Host_IP+"/led/status",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
   $("#ledstats").text(response['LED']);
  console.log(response);
});
});
// LED toggle
$(".toggleled").click(function(){
 var settings = {
  "url": Host_IP+"/led/config",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "data": {
    "led": $("#togglevalue").val()
  }
};

$.ajax(settings).done(function (response) {
  $("#toggledledstate").text(response['LED']);
  console.log(response);
});
});

// CPU status
$(".cpustatus").click(function(){
 var settings = {
  "url": Host_IP+"/cpu/status",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#cpustats").text(response['freq']);
  console.log(response);
});
});

// CPU toggle
$(".togglecpu").click(function(){
var settings = {
  "url": Host_IP+"/cpu/config?freq="+$("#cputogglevalue").val(),
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
$("#toggledcpustate").text(response['freq']);
  console.log(response);
});
});

// Stack status
$(".stackstatus").click(function(){
var settings = {
  "url": Host_IP+"/stack/status",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#stackallocated").text(response['used']);
  $("#stackfree").text(response['free']);
  console.log(response);
});
});
// Heap status
$(".heapstatus").click(function(){
var settings = {
  "url": Host_IP+"/heap/status",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#heapallocated").text(response['allocated']);
  $("#heapfree").text(response['free']);
  console.log(response);
});
});

// Garbage Collector
$(".garbage").click(function(){
var settings = {
  "url": Host_IP+"/garbage/collect",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#gc").text(response['OK_GC_1']);
  console.log(response);
});
});


// Clock time
$(".clock").click(function(){
var settings = {
  "url": Host_IP+"/clock/time",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#timezone").text(response['TimeZone']);
  $("#dayname").text(response['WeekDay']);
  $("#dayom").text(response['Day Of Month']);
  $("#month").text(response['Month']);
  $("#year").text(response['Year']);
  $("#timehour").text(response['Hour']);
  $("#timeminute").text(response['Minute']);
  $("#timesecond").text(response['Second']);
  $("#dayyear").text(response['Year-Day']);
  console.log(response);
});
});

// clock ntpsync
$(".ntpsync").click(function(){
var settings = {
  "url": Host_IP+"/clock/ntpsync",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#timezone").text(response['TimeZone']);
  $("#dayname").text(response['WeekDay']);
  $("#dayom").text(response['Day Of Month']);
  $("#month").text(response['Month']);
  $("#year").text(response['Year']);
  $("#timehour").text(response['Hour']);
  $("#timeminute").text(response['Minute']);
  $("#timesecond").text(response['Second']);
  $("#dayyear").text(response['Year-Day']);
  console.log(response);
});
});

// Device details
$(".devicedetails").click(function(){
var settings = {
  "url": Host_IP+"/device/uid",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#uid").text(response['Unique ID']);
  console.log(response);
});
var settings = {
  "url": Host_IP+"/device/hardware",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#board").text(response['Board']);
  $("#arch").text(response['Arch']);
  $("#rom").text(response['External-ROM']);
  $("#ram").text(response['RAM']);
  $("#firmware").text(response['Firmware']);
  
  console.log(response);
});
var settings = {
  "url": "http://192.168.43.97/device/software",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
   $("#nodename").text(response['nodename']);
  $("#release").text(response['release']);
  $("#version").text(response['version']);
  $("#machine").text(response['machine']);
  $("#sysname").text(response['sysname']);
  console.log(response);
});
});

// Device Reset
$(".reset").click(function(){
var settings = {
  "url": Host_IP+"/device/reset",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "data": {
    "reset": "True"
  }
};

$.ajax(settings).done(function (response) {
  
  console.log(response);
});
});

// Device Reset
$(".webrepl").click(function(){
var settings = {
  "url": Host_IP+"/device/webrepl?repl=True",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
});

// Network IFconfig
$(".ifconfig").click(function(){
var settings = {
  "url": Host_IP+"/network/ifconfig",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#ipaddr").text(response['IP']);
  $("#mask").text(response['Mask']);
  $("#gateway").text(response['Gateway']);
  $("#dns").text(response['DNS']);
  console.log(response);
});
});

// Network status
$(".netstat").click(function(){
var settings = {
  "url": Host_IP+"/network/status",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#activity").text(response['active']);
  $("#protocol").text(response['HW_protocol']);
  $("#status").text(response['status']);
  $("#strength").text(response['strength']);
  $("#connected").text(response['connected']);
  console.log(response);
});
});
// Network rssi
$(".rssibutton").click(function(){
var settings = {
  "url": Host_IP+"/network/rssi",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#rssi").text(response['rssi']);
  console.log(response);
});
});


// GPIO read ADC
$(".readadc").click(function(){
var settings = {
  "url": Host_IP+"/gpio/readadc",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#adc").text(response['adc-level']);
  console.log(response);
});
});

// GPIO read PWM
$(".readadc").click(function(){
var settings = {
  "url": Host_IP+"/gpio/readadc",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#adc").text(response['adc-level']);
  console.log(response);
});
});

// File System CWD
$(".cwd").click(function(){
var settings = {
  "url": Host_IP+"/fsys/getcwd",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  $("#getcwd").text(response['cwd']);
  console.log(response);
});
});

// File System LS
$(".ls").click(function(){
var settings = {
  "url": Host_IP+"/fsys/ls",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "data": {
    "path": $("#lspath").val()
  }
};

$.ajax(settings).done(function (response) {
  $("#pathlist").text(response[$("#lspath").val()]);
  console.log(response);
});
});

// File System CHDIR
$(".chdir").click(function(){
var settings = {
  "url": Host_IP+"/fsys/chdir",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "data": {
    "path": $("#chpath").val()
  }
};

$.ajax(settings).done(function (response) {
  $("#chdir").text(response['OK_FS_3']);
  console.log(response);
});
});
