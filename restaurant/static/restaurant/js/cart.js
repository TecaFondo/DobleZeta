var updateBtns = document.getElementsByClassName('editar-carrito')


for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var cod_prod = this.dataset.producto //producto es el nombre del dataset data-producto
        var action = this.dataset.action
        console.log("El codigo es: ", cod_prod, "action: ", action)

        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            console.log('No se encuentra iniciado sesion')
        } else {
            updateUserOrder(cod_prod, action)
        }
    })
}

function updateUserOrder(cod_prod, action) {
    console.log('User is logged in, sending data...')

    var url = '/update_item/'

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'cod_prod': cod_prod, 'action': action })
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })
}