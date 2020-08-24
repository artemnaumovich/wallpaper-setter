let directory = 'D:/jsp';
let picture_url = null;

async function get_picture_url(){	
	let category = document.getElementById('category').value;
	let resolution = document.getElementById('resolution').value;
	picture_url = await eel.get_picture_url(category, resolution)();
	document.getElementById('sample').src = picture_url;

	console.log(picture_url);
}

async function set_picture(){
	let category = document.getElementById('category').value;
	let resolution = document.getElementById('resolution').value;
	let path = await eel.build_path(directory, category, resolution)();
	await eel.save_picture(path, picture_url)();
	await eel.set_wallpaper(path);
}

jQuery('#get').on('click', function(){
	get_picture_url();
});

jQuery('#set').on('click', function(){
	set_picture();
});