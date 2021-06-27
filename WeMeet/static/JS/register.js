const input_input_picture = document.querySelector('.input_input_picture')


input_input_picture.addEventListener("change", function(){
    const file = this.files[0];
    if(file){
      const reader = new FileReader();
  
      reader.addEventListener("load", function(){
        console.log(this);
        
        document.querySelector('.propicadd').setAttribute("src", this.result);
        document.querySelector('.resetpropicbtn').style.display ='block';
      });
  
      reader.readAsDataURL(file);
    }else{
  
    }
  });

function resetbtm(){
    document.querySelector('.propicadd').src ="/static/IMAGE/LOGO/PropicSchool.svg"
    document.querySelector('.resetpropicbtn').style.display ='none';
  
  }
function resetpropicbtnbtn() {
    document.querySelector('.propicadd').src ="/static/IMAGE/LOGO/PropicSchool.svg"
    document.querySelector('.resetpropicbtn').style.display ='none';

}
