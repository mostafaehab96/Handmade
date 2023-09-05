const cart = document.querySelector(".cart");
const cartValue = document.querySelector(".badge");


const productIds = [];
let value = 0;

document.addEventListener("click", function (event) {
    if (event.target.classList.contains("p-card-add")) {
        const productId = event.target.getAttribute('product_id')
        productIds.push(productId);
        value += 1;
        cartValue.setAttribute('value', value)
    }
})

cart.addEventListener("click", function () {
    window.location.href = `/cart?productIds=${productIds.join(",")}`;
});