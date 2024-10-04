document.querySelector('.btn').addEventListener('click', function (e) {
    e.preventDefault();
    alert('Благодарим за ваш интерес! Мы свяжемся с вами в ближайшее время для подтверждения записи.');
});

// Эффект параллакса для фонового изображения
window.addEventListener('scroll', function () {
    var scrolled = window.pageYOffset;
    var headerImage = document.querySelector('.header-image');
    headerImage.style.transform = 'translateY(' + (scrolled * 0.3) + 'px)';
});

// Анимация появления элементов при прокрутке
function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

function handleScroll() {
    var elements = document.querySelectorAll('h2, p, .btn, .divider');
    elements.forEach(function (el) {
        if (isElementInViewport(el)) {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }
    });
}

window.addEventListener('scroll', handleScroll);
window.addEventListener('load', handleScroll);

// Стили для анимации
var styleSheet = document.styleSheets[0];
styleSheet.insertRule(`
    h2, p, .btn, .divider {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.5s ease, transform 0.5s ease;
    }
`, styleSheet.cssRules.length);

// Плавное появление страницы при загрузке
window.addEventListener('load', function () {
    document.body.style.opacity = '1';
});
styleSheet.insertRule(`
    body {
        opacity: 0;
        transition: opacity 0.5s ease;
    }
`, styleSheet.cssRules.length);

document.addEventListener('DOMContentLoaded', function () {
    const user = Telegram.WebApp.initDataUnsafe.user;

    if (user) {
        document.getElementById('user-id').textContent = 'User ID: ' + user.id;
        document.getElementById('username').textContent = 'Username: ' + (user.username ? user.username : 'N/A');
        document.getElementById('first-name').textContent = 'First Name: ' + (user.first_name ? user.first_name : 'N/A');
        document.getElementById('last-name').textContent = 'Last Name: ' + (user.last_name ? user.last_name : 'N/A');

        // Обновляем ссылку на запись
        const bookButton = document.getElementById('book-button');
        bookButton.href = `/forma?user_id=${user.id}`; // Подставляем user.id в ссылку
    } else {
        document.querySelector('.user-info').innerHTML = '<p>User data is not available.</p>';
    }
});
