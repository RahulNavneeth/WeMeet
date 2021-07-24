const input_picture = document.querySelector('.input_picture')

input_picture.addEventListener("change", function(){
    const file = this.files[0];
    if(file){
      const reader = new FileReader();
  
      reader.addEventListener("load", function(){
        console.log(this);
        
        input_picture.style.background='url('+this.result+')';
        input_picture.style.backgroundSize = "contain";
        input_picture.style.backgroundRepeat = "round";

      });
  
      reader.readAsDataURL(file);
    }else{
  
    }
  });