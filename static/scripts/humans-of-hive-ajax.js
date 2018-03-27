$('#likes').click(function(){
	var postid;
	postid = $(this).attr("data-catid");
	$.get('/rango/like/', {post_id: catid}, function(data){
	$('#point_count').html(data);
	$('#likes').hide();
	});
});