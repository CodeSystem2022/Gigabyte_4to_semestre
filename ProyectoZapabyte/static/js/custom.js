//variables
let allContainerCart = document.querySelector('.products');
let containerBuyCart = document.querySelector('.card-items');
let priceTotal = document.querySelector('.price-total');
let amountProduct = document.querySelector('.count-product');


//let buyThings = [];
let buyThings = JSON.parse(localStorage.getItem('cart')) || [];// 1
let totalCard = 0;
let countProduct = 0;


function loadCartFromStorage() {
    const cartData = JSON.parse(localStorage.getItem('cart')) || [];
    buyThings = cartData;
    countProduct = cartData.length;
    loadHtml();
    updateCartCount();

}
function updateCartCount() {
    amountProduct.innerHTML = countProduct;
}
loadCartFromStorage()

//functions
loadEventListenrs();
function loadEventListenrs() {
    allContainerCart.addEventListener('click', addProduct);

    containerBuyCart.addEventListener('click', deleteProduct);
}
function showCart(x) {
    document.getElementById("products-id").style.display = "block";

}

function addProduct(e) {
    
    e.preventDefault();
    if (e.target.classList.contains('btn-add-cart')) {
        const selectProduct = e.target.parentElement;
        readTheContent(selectProduct);

        // Incrementa countProduct
        countProduct++;

        // Actualiza el localStorage con los datos del carrito.
        localStorage.setItem('cart', JSON.stringify(buyThings));

        // Actualiza el contador de productos y la sumatoria total
        updateCartCount();
        loadHtml();
    }
}


function deleteProduct(e) {
    if (e.target.classList.contains('delete-product')) {
        const deleteId = e.target.getAttribute('data-id');

        buyThings.forEach((value, index) => {
            if (value.id == deleteId) {
                let priceReduce = parseFloat(value.price) * parseFloat(value.amount);
                totalCard = totalCard - priceReduce;
                totalCard = totalCard.toFixed(2);

                // Disminuye countProduct
                countProduct -= value.amount;

                // Asegura que el contador de productos no sea negativo
                if (countProduct < 0) {
                    countProduct = 0;
                }

                // Elimina el producto del carrito
                buyThings.splice(index, 1);
            }
        });

        // Actualiza el localStorage con los datos del carrito.
        localStorage.setItem('cart', JSON.stringify(buyThings));

        // Actualiza el contador de productos y la sumatoria total
        updateCartCount();
        loadHtml();
    }
}


function readTheContent(product) {
    const selectedSizeButton = product.querySelector('.btn-size.selected');
    if (!selectedSizeButton) {
        // If no size is selected, you can choose to handle it or return early.
        // For example, you can show an error message.
        alert('Please select a size.');
        return;
    }

    const selectedSize = selectedSizeButton.textContent;
    
    const infoProduct = {
        image: product.querySelector('img').src,
        title: product.querySelector('.title').textContent,
        price: parseFloat(product.querySelector('p span').textContent.replace(',', '')),
        id: product.querySelector('.btn-add-cart').getAttribute('data-id'),
        amount: 1,
        sizesSelected: [selectedSize], // Add only the selected size
    };

    const exist = buyThings.some((product) => product.id === infoProduct.id);

    if (exist) {
        const productIndex = buyThings.findIndex((product) => product.id === infoProduct.id);
        buyThings[productIndex].amount++;
    } else {
        buyThings.push(infoProduct);
    }

    loadHtml();
    updateCartCount();

    totalCard = buyThings.reduce((total, product) => total + product.price * product.amount, 0);
    totalCard = parseFloat(totalCard).toFixed(2);

    priceTotal.innerHTML = totalCard;

    localStorage.setItem('cart', JSON.stringify(buyThings));
}

function loadHtml() {
    clearHtml();

    if (buyThings.length === 0) {
        // Si el carrito está vacío, muestra un mensaje
        containerBuyCart.innerHTML = '<p>Aun no hay items en el carrito</p>';
        priceTotal.innerHTML = ''; // Limpia el total
        amountProduct.innerHTML = 0;
        return; // Sal de la función
    }

    totalCard = 0; // Reiniciar el total a 0

    buyThings.forEach(product => {
        const { image, title, price, amount, id, sizesSelected } = product;
        const row = document.createElement('div');
        row.classList.add('item');
        
        row.innerHTML = `
            <img src="${image}" alt="">
            <div class="item-content">
                <h5>${title}</h5>
                <h5 class="cart-price">${price.toLocaleString('es-ES', { minimumFractionDigits: 2 })}$</h5>
                <h6>Cantidad: ${amount}</h6>
                <p>Talles:</p>
                <ul class="container-sizes">
                    ${sizesSelected.map(size => `<li>${size}</li>`).join('')}
                </ul>
            </div>
            <span class="delete-product" data-id="${id}">X</span>
        `;
    
        containerBuyCart.appendChild(row);
    });
    
    // Calcular el total después de mostrar todos los productos
    totalCard = buyThings.reduce((total, product) => {
        const { price, amount } = product;
        return total + parseFloat(price) * amount;
    }, 0);
    

totalCard = totalCard.toFixed(2);

amountProduct.innerHTML = countProduct;
priceTotal.innerHTML = totalCard; // Actualizar el elemento HTML del total al final de la función
}

function clearHtml() {
    containerBuyCart.innerHTML = '';
}

function showCart(x) {
    document.getElementById("products-id").style.display = "block";
}
function closeBtn() {
    document.getElementById("products-id").style.display = "none";
}




///////////////////////////////////////////////////////////////////////////////////////////
//      REDIRIGIR ZAPA
////////////////////////////////////////////////////////////////////////////////
document.addEventListener("DOMContentLoaded", function () {
    // Obtiene todos los elementos con la clase "redirigirZapa"
    var redirigirZapaLinks = document.querySelectorAll(".redirigirZapa");

    // Agrega un evento click a cada enlace
    redirigirZapaLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            // Evita el comportamiento predeterminado del enlace
            event.preventDefault();

            // Obtiene la URL del atributo href
            var href = this.getAttribute("href");

            // Redirige a la URL deseada
            window.location.href = href;
        });
    });
});



document.addEventListener('DOMContentLoaded', function() {
    // Obtén una referencia al elemento del menú hamburger
    var menuHamburger = document.querySelector('.menu-hamburger');

    // Obtén una referencia al menú responsive
    var menuResponsive = document.querySelector('.menu-responsive');

    // Agrega un controlador de eventos al menú hamburger
    menuHamburger.addEventListener('click', function() {
        // Verifica si el menú responsive está visible o no
        if (menuResponsive.style.display === 'block') {
            // Si está visible, ocúltalo
            menuResponsive.style.display = 'none';
        } else {
            // Si no está visible, muéstralo
            menuResponsive.style.display = 'block';
        }
    });

    // Agrega un controlador de eventos para cerrar el menú responsive cuando se haga clic en el botón de cierre
    var btnCloseResponsive = document.querySelector('.btn-close-responsive');
    btnCloseResponsive.addEventListener('click', function() {
        menuResponsive.style.display = 'none';
    });
});