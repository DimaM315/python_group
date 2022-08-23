$('.btn-normal').on('click', click_result_in_watch_code)

function click_result_in_watch_code(event){
	target = event.target
	this_block = target.parentNode

	result_text = this_block.getElementsByClassName('result_code_watch')[0]

	result_text.classList.toggle("hidden");
	target.classList.toggle("hidden");
}


function add_to_lenta(){
	$.ajax({
	  url: "get_contents",
	  error: function(er){
		console.log(er);  
	  },
	  success: function(data){	  	
	  	var code_watch_block = $("<div class=\"code_watch block\"></div>")
	  	var img_block = $("<div class=\"block_img block\"></div>")

	  	// for watch_code
	  	$(code_watch_block).append($("<p class=\"text_code_watch\"><div class='block_code'>"+data.watch_code_question+"</div></p>"))
	  	btn_result = $("<div class=\"btn btn-normal\">Результат</div>")
	  	$(btn_result).on('click', click_result_in_watch_code)
	  	$(code_watch_block).append(btn_result)
		$(code_watch_block).append($("<div class=\"result_code_watch hidden\"><br><hr>"+data.watch_code_answer+"</div>"))

		// for img-mem
		$(img_block).append($("<img src="+data.mem_img_url+" alt='Pict' width='350' height='300'><br>"))
		$(img_block).append($("<div class='row'><div>"+data.mem_text_on_photo+"<text>Likes: 9</text></div></div>"))

		// insert
	  	$(".content").append(code_watch_block)
	  	$(".content").append(img_block)

	  }
	});
}


window.addEventListener('scroll', function() {
	let windowHeight = document.documentElement.clientHeight;
	let documentHeight = document.documentElement.scrollHeight;
	
	if (documentHeight - windowHeight == pageYOffset){
		add_to_lenta();
	};
});

	
	
