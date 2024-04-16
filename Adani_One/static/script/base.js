// Navbar Js start from here 
const hamburger = document.getElementsByClassName("nav_hamburger")[0]

hamburger.addEventListener("click", myScript);

function myScript(){
    const content = document.getElementsByClassName("nav_content")[0]
    if(content.style.display === "block"){
        content.style.display = "none"
    }   
    else{
        content.style.display = "block" 
    }
}
// Navbar Js end here 

// Footer js start from here 

const footer_dropdown = document.getElementsByClassName("fa-chevron-circle-down")
for(let i = 0;i < 5; i++){
    footer_dropdown[i].addEventListener("click", footerDrodownScript)
}


function footerDrodownScript(){
    const footer_content = document.getElementsByClassName("col_content")
    for(let i = 0; i < 5; i++){
        if(footer_content[i].style.display === "none"){
            footer_content[i].style.display = "block"
        }
        else{
            footer_content[i].style.display = "none"
        }
    }
}
// Footer Js end here 



