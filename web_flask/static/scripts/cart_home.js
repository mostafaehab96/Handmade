const cart = document.querySelector(".cart");
const cartValue = document.querySelector(".badge");

const cartContent = document.querySelectorAll('.side')
const productIds = [];
let value = cartContent.length;
cartValue.setAttribute('value', value)

document.addEventListener("click", function (event) {
    if (event.target.classList.contains("p-card-add")) {
        const productId = event.target.getAttribute('product_id')
        if (!productIds.includes(productId)) {
            productIds.push(productId);
            value += 1;
            cartValue.setAttribute('value', value)
        }
    }
})


cart.addEventListener("click", function () {
    window.location.href = `/cart?productIds=${productIds.join(',')}`

});