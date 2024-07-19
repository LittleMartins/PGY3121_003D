// Variable que mantiene el estado visible del carrito
var carritoVisible = false;

// Esperamos a que todos los elementos de la página carguen para ejecutar el script
document.addEventListener('DOMContentLoaded', function() {
    // Agregamos funcionalidad a los botones eliminar del carrito
    var botonesEliminarItem = document.getElementsByClassName('btn-eliminar');
    for (var i = 0; i < botonesEliminarItem.length; i++) {
        var button = botonesEliminarItem[i];
        button.addEventListener('click', eliminarItemCarrito);
    }

    // Agregamos funcionalidad al botón sumar cantidad
    var botonesSumarCantidad = document.getElementsByClassName('sumar-cantidad');
    for (var i = 0; i < botonesSumarCantidad.length; i++) {
        var button = botonesSumarCantidad[i];
        button.addEventListener('click', sumarCantidad);
    }

    // Agregamos funcionalidad al botón restar cantidad
    var botonesRestarCantidad = document.getElementsByClassName('restar-cantidad');
    for (var i = 0; i < botonesRestarCantidad.length; i++) {
        var button = botonesRestarCantidad[i];
        button.addEventListener('click', restarCantidad);
    }

    // Agregamos funcionalidad al botón Agregar al carrito
    var botonesAgregarAlCarrito = document.getElementsByClassName('boton-item');
    for (var i = 0; i < botonesAgregarAlCarrito.length; i++) {
        var button = botonesAgregarAlCarrito[i];
        button.addEventListener('click', agregarAlCarritoClicked);
    }

    // Agregamos funcionalidad al botón comprar
    document.getElementsByClassName('btn-pagar')[0].addEventListener('click', pagarClicked);
});

// Función que controla el botón clickeado de agregar al carrito
function agregarAlCarritoClicked(event) {
    var button = event.target;
    var item = button.parentElement;
    var nombre = button.dataset.nombre;
    var precio = button.dataset.precio;
    var id = button.dataset.id;
    var descripcion = button.dataset.descripcion;

    agregarItemAlCarrito(id, nombre, precio, descripcion);

    hacerVisibleCarrito();
}

// Función que hace visible el carrito
function hacerVisibleCarrito() {
    carritoVisible = true;
    var carrito = document.getElementsByClassName('carrito')[0];
    carrito.style.transform = 'translateX(0)';
    carrito.style.opacity = '1';
}

// Función que agrega un item al carrito
function agregarItemAlCarrito(id, nombre, precio, descripcion) {
    var item = document.createElement('div');
    item.classList.add('carrito-item');

    var itemCarritoContenido = `
        <div class="carrito-item">
            <div class="carrito-item-detalles">
                <span class="carrito-item-titulo">${nombre}</span>
                <span class="carrito-item-descripcion">${descripcion}</span>
                <div class="selector-cantidad">
                    <i class="fas fa-minus restar-cantidad"></i>
                    <input type="text" value="1" class="carrito-item-cantidad" disabled>
                    <i class="fas fa-plus sumar-cantidad"></i>
                </div>
                <span class="carrito-item-precio">$${precio}</span>
            </div>
            <button class="btn-eliminar">
                <i class="fas fa-trash"></i>
            </button>
        </div>
    `;
    item.innerHTML = itemCarritoContenido;

    // Agregamos la funcionalidad eliminar al nuevo item
    item.getElementsByClassName('btn-eliminar')[0].addEventListener('click', eliminarItemCarrito);

    // Agregamos la funcionalidad restar cantidad del nuevo item
    var botonRestarCantidad = item.getElementsByClassName('restar-cantidad')[0];
    botonRestarCantidad.addEventListener('click', restarCantidad);

    // Agregamos la funcionalidad sumar cantidad del nuevo item
    var botonSumarCantidad = item.getElementsByClassName('sumar-cantidad')[0];
    botonSumarCantidad.addEventListener('click', sumarCantidad);

    // Agregamos el nuevo item al carrito
    var itemsCarrito = document.getElementsByClassName('carrito-items')[0];
    itemsCarrito.appendChild(item);

    // Actualizamos total
    actualizarTotalCarrito();
}

// Función para sumar cantidad
function sumarCantidad(event) {
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    var cantidadActual = parseInt(selector.getElementsByClassName('carrito-item-cantidad')[0].value);
    cantidadActual++;
    selector.getElementsByClassName('carrito-item-cantidad')[0].value = cantidadActual;
    actualizarTotalCarrito();
}

// Función para restar cantidad
function restarCantidad(event) {
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    var cantidadActual = parseInt(selector.getElementsByClassName('carrito-item-cantidad')[0].value);
    if (cantidadActual > 1) {
        cantidadActual--;
        selector.getElementsByClassName('carrito-item-cantidad')[0].value = cantidadActual;
        actualizarTotalCarrito();
    }
}

// Función para eliminar un item del carrito
function eliminarItemCarrito(event) {
    var buttonClicked = event.target;
    buttonClicked.parentElement.parentElement.remove();
    actualizarTotalCarrito();
}

// Función para actualizar el total del carrito
function actualizarTotalCarrito() {
    var carritoItems = document.getElementsByClassName('carrito-items')[0];
    var total = 0;
    var items = carritoItems.getElementsByClassName('carrito-item');
    for (var i = 0; i < items.length; i++) {
        var item = items[i];
        var precioElemento = parseFloat(item.getElementsByClassName('carrito-item-precio')[0].innerText.replace('$', ''));
        var cantidadItem = parseInt(item.getElementsByClassName('carrito-item-cantidad')[0].value);
        total += precioElemento * cantidadItem;
    }
    total = total.toFixed(2);
    document.getElementsByClassName('carrito-precio-total')[0].innerText = `Total: $${total}`;
}

// Función para el botón de pagar
function pagarClicked() {
    alert('Gracias por tu compra');
    var carritoItems = document.getElementsByClassName('carrito-items')[0];
    while (carritoItems.hasChildNodes()) {
        carritoItems.removeChild(carritoItems.firstChild);
    }
    actualizarTotalCarrito();
    ocultarCarrito();
}

// Función para ocultar el carrito si está vacío
function ocultarCarrito() {
    var carritoItems = document.getElementsByClassName('carrito-items')[0];
    var carrito = document.getElementsByClassName('carrito')[0];
    if (carritoItems.childElementCount === 0) {
        carrito.style.transform = 'translateX(100%)';
        carrito.style.opacity = '0';
        carritoVisible = false;
    }
}
