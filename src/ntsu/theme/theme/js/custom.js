jQuery(document).ready(function($){
	"use strict";
	



    //Main Home Page Slider Full Width
    if ($(".cp-child-slider").length) {
        $('.cp-child-slider').bxSlider({
            auto: true,
            controls: false,
        });
    }


    //Main Home Page Slider Full Width
    if ($(".cp-about-slider").length) {
        $('.cp-about-slider').bxSlider({
            auto: true,
            controls: true,
            pager: false,
        });
    }


    //About Us Page Testimonials
    if ($(".cp-about-testi").length) {
        $('.cp-about-testi').bxSlider({
            auto: true,
            controls: false,
            pager: false,
        });
    }

    //About Us Page Client words
	if ($("#cp-about-clientwords").length) {
         $("#cp-about-clientwords").owlCarousel({
			autoPlay: 6000, //Set AutoPlay to 3 seconds
			items : 2,
			itemsMobile: [480,1],
			itemsDesktop : [1199,3],
			itemsDesktopSmall : [979,3]
			});
		}





    //Main Home Page Product Slider Full Width
    if ($(".tab-products").length) {
        $(".tab-products").owlCarousel({
            //autoPlay: 3000, //Set AutoPlay to 3 seconds
            items: 6,
            pagination: false,
			itemsMobile: [480,1],
            itemsDesktop: [1199, 3],
            itemsDesktopSmall: [979, 3]

        });
    }

    //Main Home Page Partner Logos
    if ($(".plogo-slider").length) {
        $(".plogo-slider").owlCarousel({
            autoPlay: 3000, //Set AutoPlay to 3 seconds
            items: 7,
            pagination: false,
			itemsMobile: [480,1],
            itemsDesktop: [1199, 3],
            itemsDesktopSmall: [979, 3]

        });
    }

    //Footer Pro Sliders
    if ($(".footer-pro-slider").length) {
        $('.footer-pro-slider').bxSlider({
            auto: true,
            pager: false,
        });
    }

    //Pretty Photo
    if ($(".gallery").length) {
        $("area[data-rel^='prettyPhoto']").prettyPhoto();
        $(".gallery:first a[data-rel^='prettyPhoto']").prettyPhoto({
            animation_speed: 'normal',
            theme: 'light_square',
            slideshow: 3000,
            autoplay_slideshow: false
        });
        $(".gallery:gt(0) a[data-rel^='prettyPhoto']").prettyPhoto({
            animation_speed: 'fast',
            slideshow: 10000,
            hideflash: true
        });
    }
	
	
	
		if($('.video-header').length){
		$('.video-header').prepend('<div class="video-background"></div>');
				$('.video-background').videobackground({
					videoSource: [['video/dock.mp4', 'video/mp4'],
						['video/dock.webm', 'video/webm'], 
						['video/dock.ogv', 'video/ogg']], 
					controlPosition: '#main',
					poster: 'images/mslider1.jpg',
					loadedCallback: function() {
						$(this).videobackground('mute');
					}
				});
		}



	
	
	if($('.eventcountdown').length){
	var austDay = new Date();
	austDay = new Date(2015, 12-1, 5,12,15)
	$('.eventcountdown').countdown({
	labels: ['Years', 'Months', 'Weeks', 'Days', 'Hours', 'Minutes', 'Seconds'],
	until: austDay
	});
	$('#year').text(austDay.getFullYear());
	}






    //End Tag
});