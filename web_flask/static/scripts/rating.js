// stars at review section //
const ratingContainer = document.querySelector(".rating");
const stars = ratingContainer.querySelectorAll(".star");

let selectedStarIndex = -1;

stars.forEach((star, index) => {
    star.addEventListener("click", function () {
        const rating = parseInt(star.getAttribute("data-rating"));
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
