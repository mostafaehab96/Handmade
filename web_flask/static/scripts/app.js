// show the links //
const baars = document.querySelector(".bars-icon");
baars.addEventListener("click", function () {
  document.querySelector("ul").style.display = "block";
  document.querySelector(".nd").style.width = "100%";
});

// rehide the links //
document.body.addEventListener(
  "click",
  function () {
    document.querySelector("ul").style.display = "none";
    document.querySelector(".nd").style.width = "60%";
  },
  true
);
