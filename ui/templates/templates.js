(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['nav-bar'] = template({"1":function(container,depth0,helpers,partials,data) {
    return "        <li><a class=\"waves-effect waves-light btn light-green\">TELEOP</a></li>\n        <li><a class=\"waves-effect waves-light btn brown darken-4\">AUTONOMOUS</a></li>\n";
},"3":function(container,depth0,helpers,partials,data) {
    return "        <li><a class=\"waves-effect waves-light btn brown darken-4\">TELEOP</a></li>\n        <li><a class=\"waves-effect waves-light btn light-green\">AUTONOMOUS</a></li>\n";
},"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "<nav class=\"blue lighten-1\">\n  <div class=\"nav-wrapper container\">\n    <a href=\"#!\" class=\"brand-logo\">Team4Element</a>\n    <ul class=\"right hide-on-med-and-down\">\n"
    + ((stack1 = helpers["if"].call(depth0 != null ? depth0 : {},(depth0 != null ? depth0.isTeleop : depth0),{"name":"if","hash":{},"fn":container.program(1, data, 0),"inverse":container.program(3, data, 0),"data":data})) != null ? stack1 : "")
    + "    </ul>\n  </div>\n</nav>";
},"useData":true});
})();