$(document).ready(function(){


// $('*').not('.rfid-search-input').blur(function(){
//   setTimeout(function(){$('.rfid-search-input').val('').focus()},300)
// })
//rfid search

$('.rfid-search-input').keyup(function(e){
  if(e.which == 13) {
        $.ajax({
          url:'/client/get/rfid',
          method:'post',
          data:{'rfid':$(this).val()},
          success:function(st){

            $('.client-info').html(st)
            $('.modal-part').hide()
            $('#client-form-update').show()
            $('.photo-input-wrapper label,.photo-input-wrapper input[type="checkbox"],.photo-input-wrapper a').hide()
            $('.photo-label').show()
            $('#modal').modal('show');
            setTimeout(function(){$('.rfid-search-input').val('').focus()},300)
          },
          error:function (xhr, ajaxOptions, thrownError){
              if(xhr.status==404) {
                setTimeout(function(){$('.rfid-search-input').val('').focus()},300)
            }
        }
        })
    }
})

//auto focus rfid
$('.modal').on('hidden.bs.modal', function (e) {
  setTimeout(function(){$('.rfid-search-input').val('').focus()},300)
  $('.marquer-seance').show()
})

$('.modal').on('shown.bs.modal', function (e) {
  setTimeout(function(){$('.rfid-search-input').val('').focus()},300)
})

//marquer seance

$('body').on('click','.marquer-seance',function(){
    if($('#suplaimentaire').val()>$('#suplaimentaire').attr('max')){
      alert('Ce joueur n\'a que '+$('#suplaimentaire').attr('max')+' parties')
      $('.rfid-search-input').focus()
    }

  else
  $.get({
    url:'/client/seance/'+$('.client-id-hidden').html()+'/'+$('#suplaimentaire').val(),
    success:function(st){

      var iframe = document.getElementById('presence');
      iframe.src = iframe.src;
      $('#id_update-seance').val($('#id_update-seance').val()-$('#suplaimentaire').val())
      $('#suplaimentaire').val(1)
      $('#suplaimentaire').attr('max',$('#id_update-seance').val())
      $('.rfid-search-input').focus()
    }

  })
})


//modal navigation
$('body').on('click','.modal-navigate',function(){
  $('.modal-part').hide()
  $($(this).attr('data-show')).show()
})

//auto calcul des prix lors de l'abonement

$('body').on('change','#id_abonnement-forfait,#id_abonnement-remise',function(){
  var unitaire=parseInt($("#id_abonnement-forfait option:selected").text().split(".")[1].split(" ")[4])
  var remise=$('#id_abonnement-remise').val()
  $('#id_abonnement-montant,#id_abonnement-versement').val(unitaire)

})

})
