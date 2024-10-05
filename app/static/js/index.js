document.addEventListener('DOMContentLoaded', function () {
    const user = Telegram.WebApp.initDataUnsafe.user;

    const bookButton = document.getElementById('book-button');

    bookButton.addEventListener('click', function () {
        // Если пользователь существует, добавляем его user_id и first_name в URL, иначе редирект без него
        if (user && user.id) {
            window.location.href = `/form?user_id=${user.id}&first_name=${user.first_name}`;
        } else {
            window.location.href = `/form`;
        }
    });
});
