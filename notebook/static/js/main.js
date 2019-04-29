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
    var arr=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
    el = $(this).parent();
    // el.children('div.modal-parent').attr('style', 'left:130px');
    // style = el.attr('style');
    el.attr('style', 'visibility: unset; opacity: unset;');
    modal = $(this).parent().children('.modal-parent');
    modal.addClass("show");

  
    //----------------------------------------------------------
    var mobileSelect1 = new MobileSelect({
      trigger: '.trigger1', 
      title: 'Single Selection',  
      wheels: [
            {data: arr}
          ],
      position:[2],
    });

    var baseDiv = modal.children('div').children('div').children('div').children('input');
    // console.log(baseDiv)
    $('.mobileSelect.mobileSelect-show').insertAfter(baseDiv);
   
  }
  var scrollHeight = 0;
  $(window).scroll(function () {
    scrollHeight = $(document).scrollTop();
    // console.log(scrollHeight);
    }); 

  function closeModal(e){
      // el.children('div.modal-parent').removeAttr('style');
      // console.log(, e.clientY)
      // console.log($(this));
      targetUpper = $(this).children().children().children('.img_frame');
      // console.log(targetUpper);
      targetLower = $(this).children().children().children('.img_frame_caption');
      // console.log(targetLower);
      upperOffset = targetUpper.offset();
      // console.log('x:', e.clientX, '->', upperOffset.left, ' ~ ', upperOffset.left + targetUpper.width());
      // console.log('y:', e.clientY + scrollHeight, '->', upperOffset.top, ' ~ ', upperOffset.top + targetUpper.height() + targetLower.height());
      if( e.clientX >= (upperOffset.left) && e.clientX <= (upperOffset.left + targetUpper.width()) 
        && (e.clientY + scrollHeight) >= (upperOffset.top) && (e.clientY + scrollHeight) <= (upperOffset.top + targetUpper.height() + targetLower.height()) ){
            // console.log('pass');
      } else {
        modal.removeClass("show");
        $('.mobileSelect.mobileSelect-show').remove();
      }
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
  $('#main-nav li.home, li.quiz, li.login, li.logout').removeClass('active');
  switch($(location).attr('pathname')) {
    case '/':
      $('#main-nav li.home').addClass('active');
      break;
    case '/#quiz':
      $('#main-nav li.quiz').addClass('active');
      break;

    case '/login/':
      $('#main-nav li.login').addClass('active');
      break;
    default:
      // code block
  };
});

function notebookLogout(service_type) {
  if (service_type == 'KAKAO') {
    $.getScript("//developers.kakao.com/sdk/js/kakao.min.js", function() {
      $.getScript("static/js/kakao.js", function(data, textStatus, jqxhr) { 
        // console.log(data); //data returned 
        console.log(textStatus); //success 
        console.log(jqxhr.status); //200 
        console.log('Loading kakao.js was performed.'); 
        kakaoLogout();
      });
    });
  } else {
    $.getScript("https://static.nid.naver.com/js/naveridlogin_js_sdk_2.0.0.js", function() {
      $.getScript("static/js/naver.js", function(data, textStatus, jqxhr) { 
        // console.log(data); //data returned 
        console.log(textStatus); //success 
        console.log(jqxhr.status); //200 
        console.log('Loading naver.js was performed.');
        naverLogout();
      });
    });
  }
}
