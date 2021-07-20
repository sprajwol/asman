var slider = tns({
    container: '.testimonial-slider',
    gutter: 16,
    autoplay: false,
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
