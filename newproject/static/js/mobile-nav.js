$(function ($) {
  "use strict";

  // Mobile Navigation
  if ($('.main-nav').length) {
    var $mobile_nav = $('.main-nav').clone().prop({
      class: 'mobile-nav d-sm-none'
    });
    $('body').append($mobile_nav);
    $('body').prepend('<button type="button" class="mobile-nav-toggle d-sm-none"><i class="fas fa-bars"></i></button>');
    // $('body').append('<div class="mobile-nav-overly"></div>');

    $(document).on('click', '.mobile-nav-toggle', function(e) {
      $('body').toggleClass('mobile-nav-active');
      $('.mobile-nav-toggle i').toggleClass('fa-arrow-left fa-bars');
      // $('.mobile-nav-overly').toggle();
    });
    
    $(document).on('click', '.mobile-nav .drop-down > a', function(e) {
      e.preventDefault();
      $(this).next().slideToggle(300);
      $(this).parent().toggleClass('active');
    });
    
    $('.main-nav .drop-down > a').click(function(e) {
        if($(window).width() >= 1120){
          e.preventDefault();
          $(this).next().slideToggle(300);
          $(this).parent().toggleClass('active');
        }
    });
    
    $(window).resize(function() {
      // do somthing
      if($(window).width() < 1120){
        if($('.main-nav .drop-down.active').length){
          $('.main-nav .drop-down.active').removeClass('active');
          $('.main-nav .drop-down ul').hide();
          $('.modal-parent').removeAttr('style');
          // $('#header, #content, #footer, #logo, #main-nav').removeAttr('style');
          // $('#header, #content, #footer, #logo, #main-nav').css('margin-left', 'unset');
          // $('#header, #content, #footer, #logo, #main-nav').css('margin-right', 'unset');
        }
      } else {
        $('#header, #content, #footer, #logo, #main-nav').removeAttr('style');
        $('.modal-parent').removeAttr('style');
      }
    });

    
    $('#main-nav').draggable({
      cursor:"move",      // 드래그 시 커서모양 
      stack:".post",      // .post 클래스끼리의 스택 기능 
      opacity:0.8  
    });

    $("#main-nav").bind("dragstart",function(e, ui){
      // e.preventDefault();
      // $('body').attr('style', 'background: yellow')  //bgi 체인지
    });
    
    $("#main-nav").bind("dragstop", function(e, ui){
      console.log('left:', $(this).css('left').split('px')[0], "   ",  $(window).width()/2);
      if($(this).css('left').split('px')[0] < $(window).width() / 2){
        $(this).removeAttr('style');
        $('#header, #content, #footer').css('margin-left', '260px');
        $('#header, #content, #footer').css('margin-right', 'unset');
        $('#logo').css('left', '20px');
        $('#logo').css('right', 'unset');
        // $('.modal-parent').css('left', '130px');
        // $('.modal-parent').css('right', 'unset');
        $('.modal-parent').css('left', '260px')
      } else {
        $(this).removeAttr('style');
        $(this).css('left','unset');
        $(this).css('right','0px');
        $('#header, #content, #footer').css('margin-left', 'unset');
        $('#header, #content, #footer').css('margin-right', '260px');
        $('#logo').css('left', 'unset');
        $('#logo').css('right', '100px');
        $('.modal-parent').css('left', '0')
        $('.modal-parent').css('right', 'unset')
        // $('.modal-parent').css('left', 'unset');
        // $('.modal-parent').css('right', '130px');
      }
      // e.preventDefault();
      // if()
        // $(this).removeClass("color");   //bgi 체인지
    });
  

    $('.main-nav .drop-down > a').hover(function(e) {
        if($(window).width() < 1120){
          if($('.main-nav .drop-down ul').css('display') == 'none')
            $('.main-nav .drop-down ul').show();
        }
      }
    );

    $(document).click(function(e) {
      var container = $(".mobile-nav, .mobile-nav-toggle");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('fa-arrow-left fa-bars');
          // $('.mobile-nav-overly').fadeOut();
        }
      }
    });
  } else if ($(".mobile-nav, .mobile-nav-toggle").length) {
    $(".mobile-nav, .mobile-nav-toggle").hide();
  }

});
