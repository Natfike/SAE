const toggleButton = document.getElementsByClassName('bouton_3_barres')[0]
const navbarLinks = document.getElementsByClassName('barre_de_navigation_liens')[0]
toggleButton.addEventListener('click', () => {
  navbarLinks.classList.toggle('active')
})

$(function(){
  var position_top_raccourci = $("#navigation").offset().top;
  $(window).scroll(function () {
  if ($(this).scrollTop() > position_top_raccourci) {
  $('#navigation').addClass("fixNavigation"); 
  } else {
  $('#navigation').removeClass("fixNavigation");
  }
});
});