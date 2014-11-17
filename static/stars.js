$(document).ready(function(){
    $('.star').hover(function(){
        if(!$(this).hasClass('live-star-clicked'))
        {
            $(this).toggleClass('live-star');
            $(this).prevAll().toggleClass('live-star');
        }
    });

    $('.star').click(function(){
        var value = $(this).prevAll().length +1;
        $('#value').val(value);

        $(this).removeClass('live-star-clicked live-star');
        $(this).prevAll().removeClass('live-star-clicked live-star');
        $(this).nextAll().removeClass('live-star-clicked live-star');

        $(this).toggleClass('live-star-clicked');
        $(this).prevAll().toggleClass('live-star-clicked');
    });
});
