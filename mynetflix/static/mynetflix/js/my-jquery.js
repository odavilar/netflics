$(document).ready(function() {

	$("#insearch").focus(function() {
		$(this).attr("placeholder", "");
	});

	$("#insearch").blur(function() {
		$(this).attr("placeholder", "Search...");
	});

});