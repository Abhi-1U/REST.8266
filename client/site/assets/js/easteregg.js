var day=function(){
    today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1;
    var yyyy = today.getFullYear();
    if (dd == 1 & mm ==1 & yyyy ==2021){
        return true
    }
    else return false
}
if(! day()){
    document.querySelector("aside").style.visibility="hidden";
    var div=document.querySelector("aside");
    while(div.firstChild) { 
        div.removeChild(div.firstChild); 
    }
}
