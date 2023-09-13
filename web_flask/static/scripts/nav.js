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
