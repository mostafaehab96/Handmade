const list = document.querySelectorAll(".list .item");
const pagUl = document.querySelector(".pagUl");
let page = 1;
let limit = 9;

function loadItems() {
  const start = limit * (page - 1);
  const end = limit * page - 1;

  list.forEach((item) => (item.style.display = "none"));

  for (let i = start; i <= end; i++) {
    list[i].style.display = "block";
  }
}

loadItems();

function updatePageNavigation() {
  pagUl.innerHTML = "";

  if (page !== 1) {
    const prevButton = document.createElement("li");
    prevButton.innerText = "Prev";
    prevButton.setAttribute("onclick", "changePage(" + (page - 1) + ")");
    pagUl.appendChild(prevButton);
  }

  for (let i = 1; i <= Math.ceil(list.length / limit); i++) {
    const pageNumberButton = document.createElement("li");
    pageNumberButton.innerText = i;
    if (i === page) {
      pageNumberButton.classList.add("active-pag");
    }
    pageNumberButton.setAttribute("onclick", "changePage(" + i + ")");
    pagUl.appendChild(pageNumberButton);
  }

  if (page !== Math.ceil(list.length / limit)) {
    const nextButton = document.createElement("li");
    nextButton.innerText = "Next";
    nextButton.setAttribute("onclick", "changePage(" + (page + 1) + ")");
    pagUl.appendChild(nextButton);
  }
}

function changePage(newPage) {
  page = newPage;
  loadItems();
  updatePageNavigation();
}

loadItems();
updatePageNavigation();
