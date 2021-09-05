$(document).ready(function(){
    $('.sidenav').sidenav();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('select').formSelect();
  });


$(".btn-floating").click(function(){
  $(".col").removeClass("l8 offset-l2");
  $(".card").removeClass("expand");
  $(this).parents(".col").addClass("l8 offset-l2");
  $(this).parents(".card").addClass("expand");
  $(".col").not($(this).parents(".col")).addClass("Hide");
});