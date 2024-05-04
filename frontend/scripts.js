// scripts.js

// Función para enviar los datos del formulario
function submitForm(event) {
    event.preventDefault(); // Evita que el formulario se envíe de forma predeterminada

    // Obtiene los valores de los campos del formulario
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Crea una URL con los datos del formulario
    const urlParams = new URLSearchParams({
        name: name,
        email: email,
        message: message
    });

    // Redirige a results.html con los datos del formulario en la URL
    window.location.href = 'results.html?' + urlParams.toString();
}

// Agrega un listener al evento submit del formulario
document.getElementById('data-form').addEventListener('submit', submitForm);
