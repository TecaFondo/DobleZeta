const formulario = document.getElementById('formulario');

/*function sendEmail() {
    Email.send({
        SecureToken: "<your generated token>",
        To: 'carlosvkohle',
        From: "sender@example.com",
        Subject: "Test Email",
        Body: "<html><h2>Header</h2><strong>Bold text</strong><br></br><em>Italic</em></html>"
    }).then(
        message => alert("mail sent successfully")
    );
}*/


formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    var email = document.getElementById("EntradaMail").value;
    var mensaje = document.getElementById("infoBox").value;
    const regx = /^([a-zA-Z0-9\._]+)@([a-zA-Z0-9])+.([a-z]+)(.[a-z]+)?$/
    const regex = /^([a-zA-Z0-9\._])?$/


    if (regx.test(email)) {
        if (regex.test(mensaje)) {
            alert("Correo enviado")
            sendEmail();
            return true;
        }
    } else {
        alert("Correo Incorrecto")
        return false;
    }
})