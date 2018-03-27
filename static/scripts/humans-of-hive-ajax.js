$(document).ready(function(){

	$('#points').click(function(){
		var postid;
		postid = $(this).attr("data-postid");
		$.get('/humans_of_hive/like/', {post_id: postid}, function(data){
			$('#point_count').html(data);
			$('#points').hide();
			});
	});

});