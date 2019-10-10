$(document).ready(function(){

  $('body').on('click','.client-row',function(){
    var id=$(this).attr('data-id')
    $.get({
      url:'update/'+id,
      success:function(st){
        $('.client-info').html(st)
        $('.modal-part').hide()
        $('#client-form-update').show()
        $( ".datepicker" ).datepicker({"dateFormat":'dd/mm/yy'});
        /*remove django default file input **/
        $('.photo-input-wrapper label,.photo-input-wrapper input[type="checkbox"],.photo-input-wrapper a').hide()
        $('.photo-input-wrapper').html($('.photo-input-wrapper').html().replace('Currently:','').replace('Change:',''))
        $('.photo-label').show()
        ////////////////////////////////////
      }
    })
  })

    


})
