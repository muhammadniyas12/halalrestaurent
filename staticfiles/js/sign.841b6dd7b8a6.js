function signupvalidation(){
 email =document.getElementById('email').value
 pswd1 =document.getElementById('pswd1').value
 pswd2 =document.getElementById('pswd2').value
 if  (email==""|| pswd1==""|| pswd2==""){
     document.getElementById('message').innerHTML="please enter email and passwords"
     return false
 }else{
    return true
 }
    


}