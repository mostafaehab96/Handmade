'use strict'
const cart_home = document.querySelector(".cart");
const cartValue = document.querySelector(".badge");


let productIds = [];
let value = 0;

$.get('/cart/count', function (data) {
    productIds = data.product_ids
    value = Number(data.count)
    cartValue.setAttribute('value', value)
})

document.addEventListener("click", function (event) {
    if (event.target.classList.contains("p-card-add")) {
        const productId = event.target.getAttribute('product_id')
        $.get(`/add_cart/${productId}`, function (data) {
            if (data.status === "Login") {
                swal({title:"Login First!"});
            } else {
                if (!productIds.includes(productId)) {
                    productIds.push(productId);
                    value += 1;
                    cartValue.setAttribute('value', value)
                }
            }
        })
    }
})


cart_home.addEventListener("click", function () {
    window.location.href = '/cart'

});
