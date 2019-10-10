$(document).ready(function(){

  $('body').on('click','.caisse-row',function(){
    var id=$(this).attr('data-id')
    $.get({
      url:'update/'+id,
      success:function(st){
        $('.caisse-info').html(st)
        $('.modal-part').hide()
        $('#caisse-form-update').show()
        $( ".datepicker" ).datepicker({"dateFormat":'dd/mm/yy'});

      }
    })
  })

    $( ".datepicker" ).datepicker({"dateFormat":'dd/mm/yy'});


})
