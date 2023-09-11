const addButton = document.querySelector(".p-det-add")
const cartValue = document.querySelector(".badge");
const cart_home = document.querySelector(".cart");
let value = 0;
let productIds = [];

$.get('/cart/count', function (data) {
    productIds = data.product_ids
    value = Number(data.count)
    cartValue.setAttribute('value', value)
})

addButton.addEventListener("click", function () {
    const productId = addButton.getAttribute("product_id")
    $.get(`/add_cart/${productId}`, function (data) {
        if (data.status === "Login") {
            swal({title: "Login First!"});
        } else {
            if (!productIds.includes(productId)) {
                productIds.push(productId);
                value += 1;
                cartValue.setAttribute('value', value)
                swal({title: "Product added!"});
            }
        }
    })

})


cart_home.addEventListener("click", function () {
    window.location.href = '/cart'

});