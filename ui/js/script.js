Handlebars.getTemplate = function(name) {
	if (Handlebars.templates === undefined || Handlebars.templates[name] === undefined) {
		$.ajax({
			url : '../templates/' + name + '.handlebars',
			success : function(data) {
				if (Handlebars.templates === undefined) {
					Handlebars.templates = {};
				}
				Handlebars.templates[name] = Handlebars.compile(data);
			},
			async : false
		});
	}
	return Handlebars.templates[name];
};

var compiledNavBar = Handlebars.getTemplate('nav-bar');
var navBar = compiledNavBar({ isTeleop : true });

$( document ).ready(function() {

	$('.nav-bar').html(navBar);

});