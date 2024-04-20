// How It Works section JS start From here 
const step_option = document.getElementsByClassName("Domestic_departure_option")

let class_option_name = null

const step_content = document.getElementsByClassName("Domestic_departure")

for(let i = 0; i < 4; i++){
    step_content[i].style.display = "none"
    step_content[0].style.display = "flex"
    step_option[0].style.fontWeight = "600"

    step_option[i].onclick = function step_script(e){
        
        class_option_name = e.target.classList[1]
        console.log(step_content[i].classList[1]);

        for(let j = 0; j < 4; j++){
            step_content[j].style.display = "none"
            step_option[j].style.fontWeight = "400"
        }

        step_option[i].style.fontWeight = "600"
        
        if(class_option_name == step_content[i].classList[1])
        {
            step_content[i].style.display = "flex"
        }
    }
    
}

// How IT Works Section JS Ends Here