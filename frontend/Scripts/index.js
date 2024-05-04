// scripts.js

// Función para enviar los datos del formulario
function submitForm(event) {
    event.preventDefault(); // Evita que el formulario se envíe de forma predeterminada

    // Obtiene los valores de los campos del formulario
    const name = document.getElementById('name').value;
    const departureCity = document.getElementById('departureCity').value;
    const departureDate = document.getElementById('departureDate').value;
    const arrivalCity = document.getElementById('arrivalCity').value;
    const arrivalDate = document.getElementById('arrivalDate').value;
    const selectSport = document.getElementById('selectSport').value;

    // Crea una URL con los datos del formulario
    const urlParams = new URLSearchParams({
        name: name,
        departureCity: departureCity,
        departureDate: departureDate,
        arrivalCity: arrivalCity,
        arrivalDate: arrivalDate,
        selectSport: selectSport
    });

    const url = "https://hackupc.weonpollo.xyz/user/?" + urlParams.toString();
    fetch(url, {
        method: 'post',
        body: '',
        mode: 'cors',
        headers: new Headers()
    }).then(response => response.text()).then(text => window.location.href = 'results.html?id=' + text);
}

// Agrega un listener al evento submit del formulario
document.getElementById('data-form').addEventListener('submit', submitForm);
