$(document).ready(function() {

	$("#insearch").focus(function() {
		$(this).attr("placeholder", "");
	});

	$("#insearch").blur(function() {
		$(this).attr("placeholder", "Search...");
	});

	
	$('.autoplay').slick({
	  slidesToShow: 9,
	  slidesToScroll: 1,
	  autoplay: true,
	  autoplaySpeed: 2000,
	});
    
});