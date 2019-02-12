$(document).ready( function () {
/*  $("#about")
   .transition('pulse')
   ; */
  $('#proceed')
    .transition({
      animation  :  'scale in',
      duration   : '2s'
    }
    )
  ;


});

$("#fileinput").val('');

function loadFile(){
if ($("#fileinput").val() =='') {
  /*$("#searchcol").dimmer('hide'); */
  $("#ui-loader").addClass("disabled")  ;
  $("#ui-loader").removeClass("active");
}
else {
$("#loadlabel").addClass('loading');
/*$("#ui-loader").removeClass("disabled")  ;
$("#ui-loader").addClass("active"); */
$("#fileinputform").submit();
}
}



$(function() {
  $('#searchcol')
    .transition({
      animation  :  'scale in',
      duration   : '2s'
    }
    )
  ;
});

$(function() {
    // setTimeout() function will be fired after page is loaded
    // it will wait for 5 sec. and then will fire
    // transition  function
    setTimeout(function() {
      $('#usercard')
        .transition({
          animation  :  'scale out',
          duration   : '5s'
        }
      )
    }, 6000);
});
// Ajax call to store user name and Location:
$(function() {
$('#btn-approve').click(function() {
  var uname=$("#username").text();

  $.ajax({
           url: '/storeUser',
           data: $('form').serialize(),
           type: 'POST',
           success: function(response) {
               var data=JSON.parse(response)
               //$("#usercard").remove();
               $(".message").show();
               setTimeout(function() {
                 $(".message")
                   .transition({
                     animation  :  'scale out',
                     duration   : '5s'
                   }
                 )
               }, 1000);
           },
           error: function(error) {
               console.log(error);
           }
       });


});
});

$(function() {
$('#btn-decline').click(function() {
  var uname=$("#username").text();
  $("#btn-approve").hide();
  $("#btn-decline").hide();
  $("#thankstxt").show();

});
});
