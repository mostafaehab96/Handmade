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