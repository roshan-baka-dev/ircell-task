

function register(params) {
    // location.href="login.html"  
    //you have been successfully registered
    //lets redirect to the page where it shows congrats
    location.href="register"  
}

function success(params) {
    // location.href="login.html"  
    //you have been successfully registered
    //lets redirect to the page where it shows congrats
    location.href="success"  
}

function redirect(params) {
    // location.href="index.html"    
    location.href="index"    
}
function redirect_northamerica(params) {
    // location.href="north-america.html"    
    location.href="north_america"  
}
function redirect_southamerica(params) {
    // location.href="south-america.html"
    location.href="south_america"    
}
function redirect_asia(params) {
    // location.href="asia.html"
    location.href="asia"    
}
function redirect_europe(params) {
    // location.href="europe.html"
    location.href="europe"    
}
function redirect_australia(params) {
    // location.href="australia.html"
    location.href="australia"    
}


//this wouldn't allow to go back
// function register(params) {
//     location.replace("https://www.twitter.com/1roshanekka")
// }


// console.log("ok")
const options=document.querySelectorAll(".navbar div");
console.log(options)
options.forEach((element)=>{
    element.addEventListener('click',(e)=>{
        
        for(let i=0;i<options.length;i++){
            options[i].className="";
        }

        element.className+="active";
        // console.log(element.className)
    },false)
})

// function changeColor(e){
//     if(e.type=='ontouchstart')
// }