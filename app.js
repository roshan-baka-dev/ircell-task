

function register(params) {
    location.href="login.html"  
}


function redirect(params) {
    location.href="index.html"    
}
function redirect_northamerica(params) {
    location.href="north-america.html"    
}
function redirect_southamerica(params) {
    location.href="south-america.html"    
}
function redirect_asia(params) {
    location.href="asia.html"    
}
function redirect_europe(params) {
    location.href="europe.html"    
}
function redirect_australia(params) {
    location.href="australia.html"    
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