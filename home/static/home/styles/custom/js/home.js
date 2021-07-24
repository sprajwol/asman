var main = tns({
    container: '.main-slider',
    autoplay: true,
    autoplayTimeout: 3500,
    autoplayButtonOutput: false,
    loop: true,
    mouseDrag: true,
    items: 1,
    slideBy: 'page',
    controls: false,
    nav: false,
    navPosition: 'bottom',
    controlsText: [
        '<span><i class="fa fa-angle-left fa-lg"></i></span>',
        '<span><i class="fa fa-angle-right fa-lg"></i></span>',
    ],
});

var testimonial_slider = tns({
    container: '.testimonial-slider',
    gutter: 16,
    autoplay: true,
    autoplayTimeout: 3500,
    autoplayButtonOutput: false,
    loop: true,
    mouseDrag: true,
    controls: false,
    nav: true,
    navPosition: 'bottom',
    responsive: {
        576: {
            items: 1,
        },
        768: {
            items: 1,
        },
        900: {
            items: 2,
        },
    },
});
