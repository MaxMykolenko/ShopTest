// slider.js

// Ініціалізація Swiper
document.addEventListener('DOMContentLoaded', function () {
    const swiper = new Swiper('.swiper', {
        loop: true,
        effect: 'fade',
        fadeEffect: {
            crossFade: true // Дозволяє плавну зміну без показу попереднього слайда
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
    });
});
