$(function() {
    $('#btn_sidebar').hover(function() {
        $('#sidebar-wrapper').slideDown('slow');
    });

    $('#sidebar-wrapper').mouseleave(function() {
        $('#sidebar-wrapper').slideUp('slow');
    });

    $('.container').mouseenter(function() {
        $('#sidebar-wrapper').slideUp('slow');
    });

    $('#triggerRegistrar').click(function(){
    	$('#entrarModal').modal('hide');
    });
});