$(document).ready(function(){
    $('.sidenav').sidenav();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('select').formSelect();
  });


$(".btn-floating").click(function(){
  $(".col").removeClass("l8");
  $(".card").removeClass("expand");
  $(this).parents(".col").addClass("l8");
  $(this).parents(".card").addClass("expand");
});