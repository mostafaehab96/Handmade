const addButton = document.querySelector("input.p-det-add")

if (addButton != undefined) {
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
}
