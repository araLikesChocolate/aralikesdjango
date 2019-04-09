$(function ($) {
  "use strict";

  // Mobile Navigation
  if ($('.main-nav').length) {
    var $mobile_nav = $('.main-nav').clone().prop({
      class: 'mobile-nav d-sm-none'
    });
    $('body').append($mobile_nav);
    $('body').prepend('<button type="button" class="mobile-nav-toggle d-sm-none"><i class="fa fa-bars"></i></button>');
    $('body').append('<div class="mobile-nav-overly"></div>');

    $(document).on('click', '.mobile-nav-toggle', function(e) {
      $('body').toggleClass('mobile-nav-active');
      $('.mobile-nav-toggle i').toggleClass('fa-times fa-bars');
      $('.mobile-nav-overly').toggle();
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
        // alert($('.main-nav .drop-down.active').length);
        if($('.main-nav .drop-down.active').length){
          $('.main-nav .drop-down.active').removeClass('active');
          $('.main-nav .drop-down ul').hide();
        }
      }
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
          $('.mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('.mobile-nav-overly').fadeOut();
        }
      }
    });
  } else if ($(".mobile-nav, .mobile-nav-toggle").length) {
    $(".mobile-nav, .mobile-nav-toggle").hide();
  }

});
