function togglelight() {
    document.body.setAttribute('data-md-color-scheme','default');
    document.body.setAttribute('data-md-color-primary', 'teal');
    document.getElementsByTagName('meta')["theme-color"].content = "#009485";
    //document.querySelector("aside").style.backgroundColor='#009485';
    localStorage.setItem('themepref','default');
    localStorage.setItem('primary','white');
}
function toggledark() {
    document.body.setAttribute('data-md-color-scheme', 'slate');
    document.body.setAttribute('data-md-color-primary', 'yellow');
    document.getElementsByTagName('meta')["theme-color"].content = "#ffec3d";
    //document.querySelector("aside").style.backgroundColor='#ffec3d';
    localStorage.setItem('themepref', 'slate');
    localStorage.setItem('primary','black');
}
function switchTheme(e) {
    if (e.target.checked) {
        toggledark();
    }
    else {
        togglelight();
    }
}
var toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
toggleSwitch.addEventListener('change', switchTheme, false);


function loadthemepreference() {
    var preference = localStorage.getItem('themepref');
    if (preference == null) {
        localStorage.setItem('themepref', 'default');
        //document.querySelector("aside").style.backgroundColor='#009485';
        document.body.setAttribute('data-md-color-scheme', "default");
        document.body.setAttribute('data-md-color-primary', 'teal');
        document.getElementsByTagName('meta')["theme-color"].content = "#009485";
        
    }
    else {
        if(preference === "slate"){
            toggleSwitch.checked = true;
            //document.querySelector("aside").style.backgroundColor='#ffec3d';
            document.body.setAttribute('data-md-color-scheme', preference);
            document.body.setAttribute('data-md-color-primary', 'yellow');
            document.getElementsByTagName('meta')["theme-color"].content = "#ffec3d";
            
        }
    }
}

