const btnadmin = document.querySelector(".btnadmin")
const btnschool = document.querySelector(".btnschool")
const btnstudent = document.querySelector(".btnstudent")

const buttonNameAdmin = document.querySelector(".buttonNameAdmin")
const buttonNameSchool = document.querySelector(".buttonNameSchool")
const buttonNameStudent = document.querySelector(".buttonNameStudent")

const error_auth = document.querySelector(".error_auth")

function btnadminbtnEnter(){
    buttonNameAdmin.innerHTML='.Admin.'
}
function btnschoolnbtnEnter(){
    buttonNameSchool.innerHTML='.School.'
}
function btnstudentbtnEnter(){
    buttonNameStudent.innerHTML='.Student.'
}
function btnadminbtnout(){
    buttonNameAdmin.innerHTML=''
}
function btnschoolnbtnout(){
    buttonNameSchool.innerHTML=''
}
function btnstudentbtnout(){
    buttonNameStudent.innerHTML=''
}

//================================AuthError Method for ajax================================//

function btnadminbtn(){
    error_auth.innerHTML="Admin Login is not Authenticated"

    setTimeout(function(){ error_auth.innerHTML='' }, 2000);
}
function btnschoolnbtn(){
    error_auth.innerHTML="School Login is not Authenticated"

    setTimeout(function(){ error_auth.innerHTML='' }, 2000);
}
function btnstudentbtn(){
    error_auth.innerHTML="Student Login is not Authenticated"

    setTimeout(function(){ error_auth.innerHTML='' }, 2000);
}