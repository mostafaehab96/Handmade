'use strict'

document.addEventListener("click", function (event) {
    if (event.target.classList.contains("p-card-add")) {
        const productId = event.target.getAttribute('product_id')
        $.get(`/add_cart/${productId}`, function (data){
            if (data.status === "Login") {
                swal({title:"Login First!"});
            } else {
                if (!productIds.includes(productId)) {
                    productIds.push(productId);
                    value += 1;
                    cartValue.setAttribute('value', value)
                    swal({title: "Product added!"});
                }
            }
        })
    }
})

