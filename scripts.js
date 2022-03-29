const formulario = document.getElementById('formulario');

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    var email = document.getElementById("EntradaMail").value;
    var mensaje = document.getElementById("infoBox").value;
    const regx = /^([a-zA-Z0-9\._]+)@([a-zA-Z0-9])+.([a-z]+)(.[a-z]+)?$/
    const regex = /^([a-zA-Z0-9\._])?$/


    if (regx.test(email)) {
        if (regex.test(mensaje)) {
            alert("Correo enviado")
            return true;
        }
    } else {
        alert("Correo Incorrecto")
        return false;
    }
})