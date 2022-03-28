function requiered(inputx) {
    if (inputx.value.length == 0) {
        alert("message");
        return false;
    }
    return true;
}
const expresiones = {
    correo: /^\[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/
}