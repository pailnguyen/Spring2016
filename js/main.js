// Written by Paul Nguyen

function loadFontPrefs() {
	var body = document.body;
	var nav = document.getElementsByClassName("site-nav")[0];
	if (localStorage.getItem("useReadableFont") == "true") {
		body.className = "readable";
		nav.className = "site-nav readable";
	}
	else {
		body.className = "";
		nav.className = "site-nav";
	}
	console.log("Font preferences loaded.")
}

function changeFont() {
	localStorage.setItem("useReadableFont", 
		localStorage.getItem("useReadableFont") == "true" ? "false" : "true"
	)
	loadFontPrefs();
}

window.onload = loadFontPrefs();