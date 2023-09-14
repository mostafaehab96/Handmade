'use strict'
const removeButtons = document.querySelectorAll('.p-remove')
const total_price = document.querySelector('.p-t-price').childNodes[0]
let price = Number(total_price.textContent)


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




