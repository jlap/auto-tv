function playerinit(){
	loadChannels(); // from script.js
	var videolink = getUrlParameter("movie");
	//Note: it would be nice to start fullscreen right away
	var video = $('<video width="720" controls><source src="http://192.168.1.72:32400'+videolink+'" type="video/mp4"></video>');
	$('#video-goes-here').append(video);
	var title = getUrlParameter("title");
	$('h1').html(decodeURIComponent(title));

}
function getUrlParameter(sParam){
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++) 
    {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam) 
        {
            return sParameterName[1];
        }
    }
}

