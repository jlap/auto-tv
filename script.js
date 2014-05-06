channels = null;
colWidth = 90

function init(){
	loadChannels();
	buildChannels(channels);
}

function loadChannels(){
	var url = "http://localhost/tv/auto-tv/channels.json";
	$.ajax({
		type:'GET',
		url:url,
	        dataType:'json',
		success: function(data) {
			channels = data;	
		},
		async:false
	});

}

function buildChannels(channels){
	buildTimeTable();
	var table = $("#channel-list");
	var body = $('<div class="tbody"></div>');
	table.append(body);
	for(i in channels){
		var channel = channels[i].channel;
		var tr = $('<div class="tr"></div>');
		var time = Date.now();
		var timeSoFar = parseInt(channel.channelStarted);
		for(var j in channel.movies){
			//currently playing?
			timeSoFar += parseInt(channel.movies[j].duration);
			if(timeSoFar > time){
				var width = Math.floor(colWidth * channel.movies[j].duration / 30 / 60 / 1000);
				channel.movies[j].start = 0;
				width = width - 5;//Accounting for padding
				//If movie is already started
				if((timeSoFar - time) < parseInt(channel.movies[j].duration)){
					width -= Math.floor((timeSoFar - time) / 60 /1000);
					channel.movies[j].start = (timeSoFar - time);
				}
				tr.append('<div class="td" style="width:'+width+'px;">'+
					'<a href="player.html?movie='+
					channel.movies[j].key+
					'&start='+
					channel.movies[j].start+
					'&title='+
					channel.movies[j].title+
					'">'+
					channel.movies[j].title+
					'</a></div>');
			}
		}
		body.append(tr);
	}
}

function buildTimeTable(){
	var table = $("#channel-list");
	var head = $('<div class="thead"></div>');
	var tr = $('<div class="tr"></div>');
	head.append(tr);
	table.append(head);

	var width = table.width();

	var columns = Math.floor(width/colWidth);

	var time = Date.now();

	for(var i=0; i<columns; i++){
		var timeHeadValue = new Date(time+(1*(i*30)*60*1000));
		var hours = timeHeadValue.getHours();
		var minutes = timeHeadValue.getMinutes();
		
		tr.append('<div class="th">'+hours+"h"+minutes+'m</div>');
	}
}

function getColor(){
	var colors = [
		"#FFA398",
		"#FFC48C",
		"#FCE5C0",
		"#9AD9D2",
		"#D0F7A6",

	];
	return colors[Math.floor(Math.random() * colors.length)]; 
}
