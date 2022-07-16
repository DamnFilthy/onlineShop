$(document).ready(function () {
    $('.js-burger').on('click tap', function () {
         $('.js-burger').toggleClass('active-burger')
        let height = $('.header').outerHeight(true)
        $('.js-mobile-menu').css({'top': height + 'px'})
        $('.js-mobile-menu').toggleClass('menu-show')
    })
});