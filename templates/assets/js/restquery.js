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
        // var listitem = document.createElement("li");
        // var link = document.createElement("a");
        // link.innerHTML = jjdata[i]["email"];
				// listitem.appendChild(link);

				var div = document.createElement("div")
				div.classList.add("button")
				div.classList.add("card")
				div.innerHTML =  jjdata[i]["email"];


        // el.appendChild(listitem);
				el.appendChild(div);
    }
 })
