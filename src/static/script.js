var burgers = document.querySelectorAll(".navbar-burger");

burgers.forEach(burger => {
    burger.addEventListener("click", () => {
        burger.classList.toggle("is-active");

        var target = document.getElementById(burger.dataset.target);
        target.classList.toggle("is-active");
    });
});
