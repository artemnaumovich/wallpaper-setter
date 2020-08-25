let directory = 'D:/jsp';
let picture_url = null;
let filters = null;

async function get_filters(){
	filters = await eel.get_filters()();
	console.log(filters);
	//document.getElementById('category').value = filters['categories'];
	//document.getElementById('resolution').value = filters['resolutions'];
}

async function get_picture_url(){	
	let category = document.getElementById('category').value;
	let resolution = document.getElementById('resolution').value;
	
	try{
		picture_url = await eel.get_picture_url(category, resolution)();	
		document.getElementById('sample').src = picture_url;
		console.log(picture_url);
	} catch(e){
		console.log('error');
	}

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

get_filters();