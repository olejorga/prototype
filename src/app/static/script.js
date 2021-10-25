var burgers = document.querySelectorAll(".navbar-burger");

burgers.forEach(burger => {
    burger.addEventListener("click", () => {
        burger.classList.toggle("is-active");

        var target = document.getElementById(burger.dataset.target);
        target.classList.toggle("is-active");
    });
});


var fakeLoginBtns = document.querySelectorAll(".fake-login-btn");

fakeLoginBtns.forEach(fakeLoginBtn => {
    fakeLoginBtn.addEventListener("click", () => {
        const userType = fakeLoginBtn.dataset.target;
        let formData = new FormData();

        switch (userType) {
            case "SELLER":
                formData.append('username', 'enForhandler');
                formData.append('password', 'abc123');

                break;

            case "PLATFORM_OWNER":
                formData.append('username', 'enPlattformeier');
                formData.append('password', 'abc123');

                break;

            case "END_USER":
                formData.append('username', 'enSluttbruker');
                formData.append('password', 'abc123');

                break;
        
            default:
                return null;
        }

        fetch("/api/users/login", {
            body: formData,
            method: "post"
        }).then(res => {
            window.location.href = res.url
        });
    });
});
