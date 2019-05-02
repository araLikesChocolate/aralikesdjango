$(function(){
  if ('speechSynthesis' in window) {
    console.log('speech initiated...')
    speechSynthesis.onvoiceschanged = function() {
      // var voicelist = $('#voices');
      
      // if(voicelist.find('option').length == 0) {
      //   speechSynthesis.getVoices().forEach(function(voice, index) {
      //     var option = $('<option>')
      //     .val(index)
      //     .html(voice.name + (voice.default ? ' (default)' :''));
      //     if(index==3)
      //       option.attr('selected', 'selected')
      //     voicelist.append(option);
      //   });
        // console.log(voicelist)
        // $voicelist.material_select();
      // }
    }

    // $('#speak').click(function(){
    //   console.log('clicked....')
    //   var text = 'asdfasdf';
    //   var msg = new SpeechSynthesisUtterance();
    //   var voices = window.speechSynthesis.getVoices();
    //   msg.voice = voices[$('#voices').val()];
    //   msg.rate = $('#rate').val() / 10;
    //   msg.pitch = $('#pitch').val();
    //   msg.text = text;

    //   msg.onend = function(e) {
    //     console.log('Finished in ' + event.elapsedTime + ' seconds.');
    //   };

    //   speechSynthesis.speak(msg);
    // })
  } else {
    // $('#modal1').openModal();
  }
});