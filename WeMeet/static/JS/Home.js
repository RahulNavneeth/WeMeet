const btnadmin = document.querySelector(".btnadmin")
const btnschool = document.querySelector(".btnschool")
const btnstudent = document.querySelector(".btnstudent")

const buttonNameAdmin = document.querySelector(".buttonNameAdmin")
const buttonNameSchool = document.querySelector(".buttonNameSchool")
const buttonNameStudent = document.querySelector(".buttonNameStudent")


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

setTimeout(function() {
    document.querySelector(".error_auth").style.display='none'
}, 5000);

function forgetPassword(){
    document.querySelector(".studentInfo").style.display='none'
    document.querySelector(".schoolInfo").style.display='none'
    document.querySelector(".forgetPassBg").style.display='flex'



}


function maill(){
    document.querySelector("#mail").style.display='none'
    document.querySelector("#code").style.display='flex'


}