// function readfiles(files) {
//   for (var i = 0; i < files.length; i++) {

//     reader = new FileReader();
//     reader.onload = function(event) {
//       document.querySelector('.postuploadtext').innerHTML = '';
//       document.querySelector('.uploadBtn').style.display = 'block';
//       document.querySelector('#uploadedfile').style.width='410px';
//       document.querySelector('#uploadedfile').style.height='490px';
//       document.getElementById('uploadedfile').src = event.target.result;

//      document.querySelector('.none').className='uploadImageDisplay';
//     document.querySelector('#uploadedfileDescrition').style.display = 'block';
      
//     }
//     reader.readAsDataURL(files[i]);
    
//   }
// }
// var holder = document.getElementById('dropContainer');
// holder.ondragover = function () {document.querySelector('#uploadedfile').style.width='0';document.querySelector('#uploadedfile').style.height='0';document.querySelector('#uploadedfile').src = ''; document.querySelector('.postuploadtext').innerHTML = 'DROP TO UPLOAD';this.className = 'postuploadHover';document.querySelector('.uploadBtn').style.display = 'none'; return false; };
// holder.ondragend = function () { this.className = 'postupload'; return false; };
// holder.ondragleave = function () { this.className = 'postupload'; return false; };
// // holder.ondrop = function (e) {
// //   this.className = 'postupload';
// //   e.preventDefault();
// //   document.querySelector('.postuploadtext').innerHTML = '';
// //   document.querySelector('.uploadBtn').style.display = 'block';

// //   document.querySelector('#fileInput').files =e.dataTransfer.files;
// //   console.log(e.dataTransfer.files)
// //   readfiles(e.dataTransfer.files);
// // }
// document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
//   const dropZoneElement = inputElement.closest(".postupload");

//   // dropZoneElement.addEventListener("click", (e) => {
//   //   inputElement.click();
//   // });
//   dropZoneElement.addEventListener("drop", (e) => {
//   e.preventDefault();

//   if (e.dataTransfer.files.length) {
//   // this.className = 'postupload';


//     inputElement.files = e.dataTransfer.files;
//     readfiles(e.dataTransfer.files);
//   }

//   holder.className="postupload";
// });
// });
// BigWhen21 -- github

function ShowBatch(){
    document.querySelector('.batchstud').style.width='100%';
    document.querySelector('.batchstud').style.height='23rem'
}