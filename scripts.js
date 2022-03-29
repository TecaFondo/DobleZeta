const formulario = document.getElementById('formulario');

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    var email = document.getElementById("EntradaMail").value;
    const regx = /^([a-zA-Z0-9\._]+)@([a-zA-Z0-9])+.([a-z]+)(.[a-z]+)?$/

    if (regx.test(email)) {
        alert("Correo enviado")
        return true;
    } else {
        alert("Ingrese un correo valido")
        return false;
    }
})