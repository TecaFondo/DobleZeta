const formulario = document.getElementById('formulario');

$("#mensajeError1").hide();

//Funcion encargada de enviar correo a smtp
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

//Se verifica el correo ingresado
function IsEmail(email) {
    var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (!regex.test(email)) {
        return false;
    } else {
        return true;
    }
}

function initMap() {
    var coord = { lat: -33.4003076, lng: -70.5570257 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 16,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });

    var request = {
        placeId: 'ChIJff405eHPYpYR-3wCBkWbGEQ'
    };
    var service = new google.maps.places.PlacesService(map); // map se usa igual que para poner el mapa

    service.getDetails(request, function(place, status) {
        if (status == google.maps.places.PlacesServiceStatus.OK) {
            console.log(place.reviews); //esto imprime en la consola las reviews 
        }
    });
};

//Se encarga de cargar elementos al menu de comidas
$("menu.html").ready(function() {
    fetch("https://raw.githubusercontent.com/TecaFondo/DobleZeta/main/json/menu.JSON")
        .then(Response => Response.json())
        .then(data => {

            $.each(data.pizzas, (function(i, item) {
                $("#pizzaP").append('<div class="platillo">' + item.foto + item.nombre + item.descripcion + '<div class="precio">' + item.precio + '</div>' + '</div>');
            }));

            $.each(data.sandwiches, (function(i, item) {
                $("#sandwichP").append('<div class="platillo">' + item.foto + item.nombre + item.descripcion + '<div class="precio">' + item.precio + '</div>' + '</div>');
            }));
            $.each(data.cafeteria, (function(i, item) {
                $("#cafeteriaP").append('<div class="platillo">' + item.foto + item.nombre + item.descripcion + '<div class="precio">' + item.precio + '</div>' + '</div>');
            }));
            $.each(data.plato, (function(i, item) {
                $("#platoP").append('<div class="platillo">' + item.foto + item.nombre + item.descripcion + '<div class="precio">' + item.precio + '</div>' + '</div>');
            }));
            $.each(data.bebidas, (function(i, item) {
                $("#bebidaP").append('<div class="platillo">' + item.foto + item.nombre + item.descripcion + '<div class="precio">' + item.precio + '</div>' + '</div>');
            }));

        })
});


//validadores de inicio de sesion
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

//validador de creacion de usuarios
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

//validacion de correo de recuperacion
$("#mensajeErrorMail").hide()
$("#recuperar").click(function() {
    if (IsEmail($("#recupEmail").val())) {
        $("#mensajeErrorMail").hide();
    } else {
        $("#mensajeErrorMail").show();
    }
})

//se encarga de validar correo, obtener info de textfield y enviar correo.
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

//encargado de controlar flechita BTT.
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