$.ajax({
	type: "GET",
	url: 'https://reqres.in/api/users',
 })
 .done(function(result) 
 {
	// console.log(result.data);

    var jdata = JSON.stringify(result.data);
    var jjdata = JSON.parse(jdata);

    for(let i=0;i<jjdata.length;i++){
        var el = document.getElementById("notelist");
        var listitem = document.createElement("li");
        var link = document.createElement("a");
        link.innerHTML = jjdata[i]["email"];

        listitem.appendChild(link);
        el.appendChild(listitem);
    }
 })
