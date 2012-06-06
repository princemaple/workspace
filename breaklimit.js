javascript:(function(){
	var doc = document;
	var body = doc.body;
	body.onselectstart = body.oncopy = body.onpaste = body.onkeydown = body.oncontextmenu = body.onmousemove = body.onselectstart = body.ondragstart = doc.onselectstart = doc.oncopy = doc.onpaste = doc.onkeydown = doc.oncontextmenu = null;
	body.style.webkitUserSelect ='auto';
})()