$(function ($) {
  "use strict";

  // Preloader (if the #preloader div exists)
  $(window).on('load', function () {
    if ($('#preloader').length) {
      $('#preloader').delay(100).fadeOut('slow', function () {
        $(this).remove();
      });
    }
  });

  // Initiate the wowjs animation library
  //new WOW().init();

  // Header scroll class
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('#header').addClass('header-scrolled');
    } else {
      $('#header').removeClass('header-scrolled');
    }
  });

  if ($(window).scrollTop() > 100) {
    $('#header').addClass('header-scrolled');
  }

  // Smooth scroll for the navigation and links with .scrollto classes
  $('.main-nav a, .mobile-nav a, .scrollto').on('click', function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      if (target.length) {
        var top_space = 0;

        if ($('#header').length) {
          top_space = $('#header').outerHeight();

          if (! $('#header').hasClass('header-scrolled')) {
            top_space = top_space - 20;
          }
        }

        $('html, body').animate({
          scrollTop: target.offset().top - top_space
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.main-nav, .mobile-nav').length) {
          $('.main-nav .active, .mobile-nav .active').removeClass('active');
          $(this).closest('li').addClass('active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('.mobile-nav-overly').fadeOut();
        }
        return false;
      }
    }
  });

  // Navigation active state on scroll
  var nav_sections = $('section');
  var main_nav = $('.main-nav, .mobile-nav');
  var main_nav_height = $('#header').outerHeight();

  $(window).on('scroll', function () {
    var cur_pos = $(this).scrollTop();
  
    nav_sections.each(function() {
      var top = $(this).offset().top - main_nav_height,
          bottom = top + $(this).outerHeight();
  
      if (cur_pos >= top && cur_pos <= bottom) {
        main_nav.find('li').removeClass('active');
        main_nav.find('a[href="#'+$(this).attr('id')+'"]').parent('li').addClass('active');
      }
    });
  });
});

/*******************************************************
 
          custom modal effects for home-images        

*******************************************************/
$(function(){
  var img_modal = $(".img_modal_origin"),
      modal = $(".modal-parent"),
      closeButton = $(".close-modal"),
      style = '';
      el = '';

  function init(){
      if($(".img_modal_origin").length){
          img_modal.on("click", openModal);
          modal.on("click", closeModal);
          closeButton.on("click", closeModal);
      }
  }

  function openModal(){
    el = $(this).parent();
    // el.children('div.modal-parent').attr('style', 'left:130px');
    style = el.attr('style');
    el.attr('style', 'visibility: unset; opacity: unset;');
    modal = $(this).parent().children('.modal-parent');
    modal.addClass("show");
  }

  function closeModal(){
      // el.children('div.modal-parent').removeAttr('style');
      modal.removeClass("show");
  }

  init();
});



/****************************************
        Image fade-in effect
****************************************/
// FADE UP & IN
$(function(){
  $('[fade-up-in]').each(function(index, el) {
    // Init ScrollMagic Controller
    var scrollMagicController = new ScrollMagic.Controller();
    
    var tl = new TimelineMax({pause: true});    
    tl.add("start") // add timeline label
      .fromTo(el, 0.8, { autoAlpha: 0, y: 60 }, { autoAlpha: 1, y: 0, ease: Power2.easeOut }, "start")

    // Create the Scene and trigger when visible
    var scene = new ScrollMagic.Scene({
      triggerElement: el,
      triggerHook: 'onEnter',
      // offset: 170
      offset: 55 
    })
    .setTween(tl)
    .addTo(scrollMagicController);
  });
});

// main nav active
$(function () {
  $('#home, #quiz, #login, .logout').removeClass('active');
  switch($(location).attr('pathname')) {
    case '/':
      $('#home').addClass('active');
      break;
    case '/#quiz':
      $('#quiz').addClass('active');
      break;

    case '/registration/login/':
      $('#login').addClass('active');
      break;
    default:
      // code block
  };
});
