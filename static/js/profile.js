let edit = document.getElementsByClassName('edit')[0];
let editMain = document.getElementsByClassName('edit-main');
let all = document.getElementsByClassName('all')[0];
let password = document.getElementsByClassName('password')[0];

let changeAll = document.getElementsByClassName('change-all')[0];
let changePassword = document.getElementsByClassName('change-password')[0];

function show(open, close){
    let showTag = document.getElementsByClassName(open)[0];
    let closeTag = document.getElementsByClassName(close)[0];

    edit.style.display = 'flex'
    closeTag.style.display = 'none';
    showTag.style.display = 'flex';
}
function close(){
    edit.style.display = 'none';
}

document.addEventListener('click', function(tags){
    if(tags.composedPath().includes(editMain[0]) == false && tags.composedPath().includes(editMain[1]) == false && tags.composedPath().includes(changeAll) == false && tags.composedPath().includes(changePassword) == false){
        close();        
    }
})