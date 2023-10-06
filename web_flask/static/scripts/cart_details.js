'use strict'
const removeButtons = document.querySelectorAll('.p-remove')
const allPrice = document.querySelector('.p-t-price')
const checkoutButton = document.querySelector(".check-btn")
let total_price = undefined
let price = 0

if (allPrice) {
    total_price = allPrice.childNodes[0]
    Number(total_price.textContent)
}

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
        fetch(`/cart/remove/${product_id}`)
            .then((response) => {
                if (response.status === 200) {
                    swal({title: "Product Removed"})
                    get_update()
                }
            })
        if (value === 0) {
            window.location.href = '/'
        }
    })
})

if (checkoutButton) {
    checkoutButton.addEventListener("click", function () {
        fetch('/checkout').then((response) => {
            if (response.ok) return response.json()
        }).then((data) => {
            if (data['status'] === "ok") {
                swal({
                    title: 'Order was added',
                    text: `ID: ${data['order_id']}`,
                    icon: 'success',
                    closeOnClickOutside: true,
                    buttons: {
                        home: true,
                        orders: true
                    }
                }).then((result) => {
                    if (result === 'orders') window.location.href = "/orders"
                    else window.location.href = "/"

                });
            } else {
                swal({
                    title: "Login First!",
                    closeOnClickOutside: true,
                    buttons: {
                        cancel: true,
                        confirm: true
                    }
                }).then((result) => {
                    if (result) window.location.href = "/login"
                    console.log(result)
                });
            }
        })
    })
}


