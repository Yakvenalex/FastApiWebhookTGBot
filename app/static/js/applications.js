// Анимация появления элементов
function animateElements() {
    const elements = document.querySelectorAll('h1, table');
    elements.forEach((el, index) => {
        setTimeout(() => {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, 200 * index);
    });
}

// Запуск анимации при загрузке страницы
window.addEventListener('load', animateElements);

// Обработчик для прокрутки на мобильных устройствах
document.addEventListener('DOMContentLoaded', (event) => {
    const main = document.querySelector('main');
    let isScrolling;

    main.addEventListener('scroll', function () {
        window.clearTimeout(isScrolling);
        isScrolling = setTimeout(function () {
            console.log('Scrolling has stopped.');
        }, 66);
    }, false);
});