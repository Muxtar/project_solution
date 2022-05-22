let divFormLogin = document.getElementsByClassName('login')[0];
let divFormSign = document.getElementsByClassName('sign')[0];

let divLogin = document.getElementsByClassName('login-title')[0];
let divSign = document.getElementsByClassName('sign-title')[0];

function change(param){
    if(param.innerText == 'Log in'){
        divFormSign.style.display = 'none';
        divFormLogin.style.display = 'block';

        divSign.style.boxShadow = 'none';
        divSign.style.clipPath = 'none';
        divLogin.style.backgroundImage = 'none'

        divSign.style.backgroundImage = 'linear-gradient(to left, rgb(245, 245, 245), white)';
        divLogin.style.boxShadow = '0 0 5px rgba(0,0,0,0.75)';
        divLogin.style.clipPath = 'inset(0px -15px 0px 0px)';
    }

    else{
        divFormSign.style.display = 'block';
        divFormLogin.style.display = 'none';

       divSign.style.backgroundImage = 'none'
       divSign.style.boxShadow = '0 0 5px rgba(0,0,0,0.75)';
       divSign.style.clipPath = 'inset(0px 0px 0px -15px)'

       divLogin.style.boxShadow = 'none';
       divLogin.style.clipPath = 'none';
       divLogin.style.backgroundImage = 'linear-gradient(to right, rgb(245, 245, 245), white)'

    }
}

function borderBottom(param){
    param.parentNode.style.borderBottom = '2px solid red' 
}
function removeBottom(param){
    param.parentNode.style.borderBottom = '2px solid rgb(220, 220, 220)'
}