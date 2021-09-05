$(document).ready(function(){
    $('.sidenav').sidenav();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('select').formSelect();
  });

var open = false;

jQuery('.btn-floating').click(function() {
    open = !open;

    if(open) {
      $(".col").removeClass("l8 offset-l2 m8 offset-m2 s8");
      $(".card").removeClass("expand");
      $(this).parents(".col").addClass("l8 offset-l2 m8 offset-m2 s8");
      $(this).parents(".card").addClass("expand");
      $(".col").not($(this).parents(".col")).addClass("Hide");
    } else {
      $(".col").removeClass("l8 offset-l2 m8 offset-m2 s8");
      $(".card").removeClass("expand");
      $(".col").removeClass("Hide");
    }
});