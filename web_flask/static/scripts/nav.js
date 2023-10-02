// show the mobile-nav //
const tog = document.querySelector(".tog-btn");
const barsIcon = document.querySelector(".tog-btn i");
const mobNav = document.querySelector(".mobile-nav");

tog.onclick = () => {
    mobNav.classList.toggle("show-nav");
    const activeClass = mobNav.classList.contains("show-nav");

    if (activeClass) {
        barsIcon.classList = "fa-solid fa-xmark";
    } else {
        barsIcon.classList = "fa-solid fa-bars";
    }
};

// //////////////////////////////////////
// change the color of header after scrolling

const header = document.querySelector(".header");
const scrollThreshold = 520;

window.addEventListener("scroll", function () {
    if (window.scrollY >= scrollThreshold) {
        header.classList.add("active");
    } else {
        header.classList.remove("active");
    }
});

//Cart behavior

const cart_home = document.querySelector(".cart");
const cartValue = document.querySelector(".badge");
const addButtons = document.querySelectorAll('.p-card-add')
const addButton = document.querySelector("input.p-det-add")

let productIds = [];
let value = 0;

$.get('/cart/count', function (data) {
    productIds = data.product_ids
    value = Number(data.count)
    cartValue.setAttribute('value', value)
    if (addButton !== null) {
        const productId = addButton.getAttribute("product_id")
        if (productIds.includes(productId)) {
            addButton.setAttribute("value", " Added! ")
            addButton.disabled = true;
        }
    }
    addButtons.forEach((button) => {
        const id = button.getAttribute("product_id")
        if (productIds.includes(id)) button.textContent = " Added! "
    })
})

cart_home.addEventListener("click", function () {
    window.location.href = '/cart'

});
