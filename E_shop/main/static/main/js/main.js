(function ($) {
    const hosturl = 'http://127.0.0.1:8000/'
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });


    // Related carousel
    $('.related-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            }
        }
    });


    // Product Quantity
    $('.quantity button').on('click', function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        button.parent().parent().find('input').val(newVal);
    });


    $.ajax({
        type: 'GET',
        url: hosturl+'jsonlocation/',
        success: function (data){
           const loctionitems = data.map(function(item,index){
                return item.status_Location === 1 ? `<a class="text-light mb-2 " href="shop.html" style="text-transform: uppercase;">${index+1} . ${item.name}</a>` : ''
            })
            $('#location__list').html(loctionitems.join(''))
          
        }
    })
    const linknavitem = hosturl + 'shop/'
    $.ajax({
        type: 'GET',
        url: hosturl+'jsoncategory/',
        success: function (data){
            const categoryitems = data.map(function(item){
                
                return `<a href="${linknavitem}${item.name.toLowerCase()}/" class="dropdown-item o-text-transform"> ${item.name} </a>`
            })
            $('#nav-category').html(`<a href="${linknavitem}all-item/" class="dropdown-item o-text-transform">ALL ITEMS</a>`.concat(categoryitems.join('')))
        }
    })
})(jQuery);


