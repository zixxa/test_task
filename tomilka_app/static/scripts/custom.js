$(document).ready(function () {
    
    $('.fancybox').fancybox();
    
    $('.fancybox-gallery').fancybox({
        loop: true,
        animationEffect: 'zoom',
        transitionEffect: 'slide',
        transitionDuration: 500
    });
    
    $('.faq .question-title').on('click', function(){
        $(this).toggleClass('opened');
        if ($(this).hasClass('opened')){
            $(this).parent().find('.answer').slideDown(300);
        } else {
            $(this).parent().find('.answer').slideUp(300);
        }
    });
    
    $('.header-top ul li a').on('click', function(){
        var scroll_el = $(this).attr('href');
        $('html, body').animate({ scrollTop: $(scroll_el).offset().top }, 500);
        return false;
    });
    
    $('.models-item .btn').on('click', function() {
        var id = $(this).data('id');
        var price = $(this).closest('.models-prices').find('.new-price').text();
        var name = $(this).closest('.models-item').find('.model-name').text();
        $('#order-model .name').html(name);
        $('#order-model .price').html(price);
        $('#order-model input[name=id]').val(id);
    });

});    