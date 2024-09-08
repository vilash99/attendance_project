let navButton = document.querySelector("#nav-toggle");
let navbar = document.querySelector("#nav-links");

navButton.addEventListener("click", () => {
  navButton.classList.toggle("fa-times");
  navbar.classList.toggle("show-links");
});

window.onscroll = () => {
  navButton.classList.remove("fa-times");
  navbar.classList.remove("show-links");
};
