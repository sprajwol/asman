var slider = tns({
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
