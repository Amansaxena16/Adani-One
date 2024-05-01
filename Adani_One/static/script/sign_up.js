// Sign Up Page script for validation of data
var btn = document.getElementById('btn')

btn.onclick = validateForm

function validateForm(event){
    // event.preventDefault()
    var name = document.getElementById('name').value
    var email = document.getElementById('email').value
    var contact = document.getElementById('contact').value
    var password = document.getElementById('password').value
    var repassword = document.getElementById('repassword').value

    
    if(name === ""){
        alert('Enter Your Name!!')
        return false
    }
    var specialCharacter = /[!@#$%^&*(),.?":{}|<>0123456789]/;
    
    if(specialCharacter.test(name)){
        alert('Name should not have any Special Character or Number!!')
        return false
    }
    if(name.length > 50){
        alert('Too Long Name!!')
        return false
    }
    if(email === ""){
        alert('Enter Your Email')
        return false
    }
    if(email.length > 80){
        alert('Email is too Big')
    }
    if(contact === ""){
        alert('Enter your Contact Details')
        return false
    }
    if(contact.length != 10){
        alert('Phone must have 10 Numbers Only')
        return false
    }
    if(password === ""){
        alert('Enter Your Password')
        return false
    }
    if(repassword === ""){
        alert('Re-Enter Your Password')
        return false
    }
    if(password != repassword){
        alert('Password Does not Match')
        return false
    }

    

}

