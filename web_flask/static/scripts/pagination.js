'use strict'
let thisPage = 1;
let limit = 9;
const list = document.querySelectorAll(".list .item");

function loadItem() {
  let beginGet = limit * (thisPage - 1);
  let endGet = limit * thisPage - 1;
  list.forEach((item, key) => {
    if (key >= beginGet && key <= endGet) {
      item.style.display = "block";
    } else {
      item.style.display = "none";
    }
  });
  pagUl();
}
loadItem();
function pagUl() {
  let count = Math.ceil(list.length / limit);
  let startPage = Math.max(1, thisPage - 2);

  if (count - startPage < 4) {
    startPage = Math.max(1, count - 4);
  }

  document.querySelector(".pagUl").innerHTML = "";

  if (thisPage != 1) {
    const prev = document.createElement("li");
    prev.classList = "arrow fa-solid fa-circle-left";
    prev.setAttribute("onclick", "changePage(" + (thisPage - 1) + ")");
    document.querySelector(".pagUl").appendChild(prev);
  }

  for (let i = startPage; i < startPage + 5 && i <= count; i++) {
    const newPage = document.createElement("li");
    newPage.innerText = i;
    if (i == thisPage) {
      newPage.classList.add("active-pag");
    }
    newPage.setAttribute("onclick", "changePage(" + i + ")");
    document.querySelector(".pagUl").appendChild(newPage);
  }

  if (thisPage != count) {
    const next = document.createElement("li");
    next.classList = "arrow fa-solid fa-circle-right";
    next.setAttribute("onclick", "changePage(" + (thisPage + 1) + ")");
    document.querySelector(".pagUl").appendChild(next);
  }
}
function changePage(i) {
  thisPage = i;
  loadItem();
}