'use strict'
// stars at review section //
const ratingContainer = document.querySelector(".rating");
const stars = ratingContainer.querySelectorAll(".star");
const addReview = document.querySelector(".add-review-btn")
const reviewText = document.querySelector(".allrev-inp")
let rating = 1
let selectedStarIndex = -1;

stars.forEach((star, index) => {
    star.addEventListener("click", function () {
        rating = parseInt(star.getAttribute("data-rating"));
        selectedStarIndex = index;
        resetStars();
        highlightStars(selectedStarIndex);
    });

    star.addEventListener("mouseover", function () {
        highlightStars(index);
    });

    star.addEventListener("mouseout", function () {
        resetStars();
        highlightStars(selectedStarIndex);
    });
});

function highlightStars(index) {
    for (let i = 0; i <= index; i++) {
        stars[i].classList.add("active");
    }
}

function resetStars() {
    stars.forEach((star) => {
        star.classList.remove("active");
    });
}

addReview.addEventListener("click", function () {
    fetch('/status').then((response) => {
        if (response.ok) return response.json()
    }).then((data) => {
        if (data['status'] === 'login') {
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
            const productId = addReview.getAttribute("product_id")
            const review = {
                rating: rating,
                text: reviewText.value,
                product_id: productId
            }
            const formData = new FormData();
            for (const key in review) {
                formData.append(key, review[key]);
            }
            fetch("/add_review", {
                method: "POST",
                body: formData,
            }).then((response) => response.json()).then((data) => {
                swal({title: "Review Added", icon: "success"}).then((result) => {
                    window.location.href = `/products/${productId}`
                })
            })
        }
    })
})


