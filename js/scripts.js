const formulario = document.getElementById('formulario');

function sendEmail(email, mensaje) {
    Email.send({

        Host: "smtp.mailtrap.io",
        Username: "10ef1dc05d2969",
        Password: "25c702958bf97a",
        To: 'carlosvkohler@gmail.com',
        From: email,
        Subject: "Test Email",
        Body: mensaje
    }).then(
        message => alert("Correo enviado")
    );
}


formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    var email = document.getElementById("EntradaMail").value;
    var mensaje = document.getElementById("infoBox").value;
    const regx = /^([a-zA-Z0-9\._]+)@([a-zA-Z0-9])+.([a-z]+)(.[a-z]+)?$/
        /*const regex = /^([a-zA-Z0-9\._])?$/*/


    if (regx.test(email)) {
        console.log("Se aprueba correo")
        if (mensaje != null) {
            console.log("Se aprueba mensaje")
            sendEmail(email, mensaje);
            console.log("Mensaje enviado")
            return true;
        }
    } else {
        alert("Correo Incorrecto")
        return false;
    }
})
myID = document.getElementById("flechita");

var myScrollFunc = function() {
    var y = window.scrollY;
    if (y >= 200) {
        myID.className = "fixed-bottom show"
    } else {
        myID.className = "fixed-bottom hide"
    }
};

window.addEventListener("scroll", myScrollFunc);