'use strict'

document.addEventListener("click", function (event) {
    if (event.target.classList.contains("p-card-add")) {
        const productId = event.target.getAttribute('product_id')
        fetch(`/add_cart/${productId}`).then((response) => {
            if (response.ok) return response.json()
        }).then((data) => {
            if (data.status === "Login") {
                swal({
                    title: "Login First!",
                    closeOnClickOutside: true,
                    buttons: {
                        cancel: true,
                        confirm: true
                    }
                }).then((result) => {
                    if (result) window.location.href = "/login"
                });
            } else {
                if (!productIds.includes(productId)) {
                    productIds.push(productId);
                    value += 1;
                    cartValue.setAttribute('value', value)
                    swal({title: "Product added!", icon: "success"});
                    event.target.textContent = ' Added !'
                } else {
                    swal({title: "Product already added!"})
                }
            }
        })
    }
})

