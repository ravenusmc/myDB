(function($){

  let img = $('img');
  let title = $('.home_title');

  TweenLite.from(img, 3, {x: -600}); 
  TweenLite.from(title, 3, {autoAlpha: 0, delay: 3});
   
})(jQuery);