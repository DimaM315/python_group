$('.btn-primary').on('click', function(event){
	target = event.target
	this_block = target.parentNode


	div_code_field = this_block.getElementsByClassName('task-solution')
	console.log(div_code_field)
	div_code_field[0].classList.toggle("hidden");
})

$('.btn-success').on('click', function(event){
	target = event.target
	this_block = target.parentNode
	
	div_code_field = this_block.getElementsByClassName('task-solution')
	console.log(div_code_field)
	div_code_field[1].classList.toggle("hidden");
})