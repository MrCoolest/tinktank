
const degree = document.getElementById("Degree_name");
const if_other = document.getElementById("if_others");



// This eventlisner run when user choose Other option in Degree Name
degree.addEventListener('change', (e)=>{
     const degree_other = document.getElementById('degree_other');
     if(e.target.value == 'Others'){
          degree_other.classList.remove("visually-hidden");
          if_other.required = true;
     }
     else if(!degree_other.classList.contains("visually-hidden")){
          degree_other.classList.add("visually-hidden");
          if_other.required = false;
     }
});


// This eventListner give input value to other option
if_other.addEventListener('input', (e)=>{
     const value = e.target.value;
     const other = document.getElementById('option_other');

     other.value = value;
});

window.onscroll = function(){
     document.querySelector('footer').classList.remove('fixed-bottom');
}


