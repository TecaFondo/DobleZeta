const formulario = document.getElementById('formulario');

$("#mensajeError1").hide();

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

function IsEmail(email) {
    var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (!regex.test(email)) {
        return false;
    } else {
        return true;
    }
}
$("#mensajeError").hide();
$("#mensajeErrorPass").hide();
$("#loginBTN").click(function() {
    var correo = $("#correo").val();
    if (IsEmail(correo) && correo != "") {
        if ($("#pass").val() != "") {
            $("#mensajeError").hide();
            alert("inicio sesion exitoso");
        } else {
            $("#mensajeError").show();
        }
    } else {
        $("#mensajeError").show();
    }
});
$("#crearUsr").click(function() {
    var correo = $("#newcorreo").val();

    if (IsEmail(correo) && correo != "") {
        $("mensajeError1").hide();
        if (($("#clave1").val() != "")) {
            if (($("#clave2").val()) == ($("#clave1").val())) {
                $("#mensajeError1").hide();
                $("#mensajeErrorPass").hide();
                alert("Nuevo usuario creado");
            } else {
                $("#mensajeErrorPass").show();

            }
        }
    } else {
        $("mensajeError1").show();
    }
})

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    var email = document.getElementById("EntradaMail").value;
    var mensaje = document.getElementById("infoBox").value;

    if (IsEmail(email)) {
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
});


myID = document.getElementById("flechitaMenu");
var myScrollFunc = function() {
    var y = window.scrollY;
    if (y >= 200) {
        myID.className = "fixed-bottom show"
    } else {
        myID.className = "fixed-bottom hide"
    }
};

window.addEventListener("scroll", myScrollFunc);