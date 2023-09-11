'use strict'
const removeButtons = document.querySelectorAll('.p-remove')
const cartContent = document.querySelectorAll('.side')
const cartValue = document.querySelector(".badge");
const total_price = document.querySelector('.p-t-price').childNodes[0]
let value = cartContent.length;
let price = Number(total_price.textContent)


cartValue.setAttribute('value', value)


removeButtons.forEach(function (button) {
    button.addEventListener("click", function () {
        const product_price = Number(button.getAttribute('product_price'))
        const product_id = button.getAttribute('product_id')
        const side = button.parentNode.parentNode
        side.remove()
        value -= 1
        price -= product_price
        total_price.textContent = price
        cartValue.setAttribute('value', value)

        $.get(`/cart/remove/${product_id}`, function (data) {
            if (data.status === "ok") {
                swal({title: "Product Removed"});
            }
        })
        if (value === 0) {
            window.location.href = '/'
        }
    })
})
