$('.btn-normal').on('click', function(event){
	target = event.target
	this_block = target.parentNode

	result_text = this_block.getElementsByClassName('result_code_watch')[0]

	result_text.classList.toggle("hidden");
	target.classList.toggle("hidden");

})
