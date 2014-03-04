$(document).on('click', '#icon-menu', function () {
	$('header.wrapper nav ul').toggle();
	$('#icon-menu').toggleClass('connect');
});

$(window).on('resize', function () {
	if ($(this).width() >= 768) $('header.wrapper nav ul').show();
	if ($(this).width() < 768) $('header.wrapper nav ul').hide();
});