function loginvalidation (){
    email=document.getElementById('email').value
    password=document.getElementById('pswd').value
    if (email==""|| password==""){
        document.getElementById("message").innerHTML='please enter email  and password'
        return false
    }else{
        return true
    }
}