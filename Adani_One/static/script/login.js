var btn = document.getElementById('btn')

btn.onclick = loginFormValidate

function loginFormValidate(){
    var email = document.getElementById('email').value
    var password = document.getElementById('password').value

    if(email === ""){
        alert('Enter Your Email!!')
        return false
    }
    if(password === ""){
        alert('Enter Your Password!!')
        return false
    }
}   