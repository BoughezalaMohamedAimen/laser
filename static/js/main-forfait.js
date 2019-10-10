$(document).ready(function(){

    $('.forfait-row').click(function(){
          $('#update').attr('action','update/'+$(this).find('th').html())
        $(this).find('td').each(function(){
          $('input[name="update-'+$(this).attr('class')+'"').val($(this).html())
          })
      $('input[name="update-id"]').val($(this).find('th').html())

      setTimeout(function(){
        if(0<parseInt($('#id_update-seance').val())<3) $('#id_update-seance').css('background','rgba(255,215,0.3)')
        if(parseInt($('#id_update-seance').val())<=0) $('#id_update-seance').css('background','rgba(220,20,60,.5)')
      },1000)

    })


})
