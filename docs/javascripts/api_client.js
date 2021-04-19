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
  $("#toggleledstate").text(response['LED']);
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

