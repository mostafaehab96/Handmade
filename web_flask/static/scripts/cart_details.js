'use strict'
const removeButtons = document.querySelectorAll('.p-remove')
const cartContent = document.querySelectorAll('.side')
const cartValue = document.querySelector(".badge");
const total_price = document.querySelector('.p-t-price').childNodes[0]

let value = cartContent.length;
let price = Number(total_price.textContent)

cartValue.setAttribute('value', value)

removeButtons.forEach(function(button) {
    button.addEventListener("click", function () {
        const product_price = Number(button.getAttribute('product_price'))
        console.log(product_price)
        const side = button.parentNode.parentNode
        side.remove()
        value -= 1
        price -= product_price
        total_price.textContent = price
        cartValue.setAttribute('value', value)
    })
})
