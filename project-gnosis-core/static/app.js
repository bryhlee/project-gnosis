/*
 * http://stackoverflow.com/questions/18260815/use-gapi-client-javascript-to-execute-my-custom-google-api
 * https://developers.google.com/appengine/docs/java/endpoints/consume_js
 * https://developers.google.com/api-client-library/javascript/reference/referencedocs#gapiclientload
 *
 */

/**
 * After the client library has loaded, this init() function is called.
 * The init() function loads the helloworldendpoints API.
 */

function init() {
	
	// You need to pass the root path when you load your API
	// otherwise calls to execute the API run into a problem
	
	// rootpath will evaulate to either of these, depending on where the app is running:
	// //localhost:8080/_ah/api
	// //your-app-id/_ah/api

	var rootpath = "//" + window.location.host + "/_ah/api";
	
	// Load the helloworldendpoints API
	// If loading completes successfully, call loadCallback function
	gapi.client.load('gnosis_endpoints', 'v1', loadCallback, rootpath);
}

/*
 * When helloworldendpoints API has loaded, this callback is called.
 * 
 * We need to wait until the helloworldendpoints API has loaded to
 * enable the actions for the buttons in index.html,
 * because the buttons call functions in the helloworldendpoints API
 */
function loadCallback () {	
	// Enable the button actions
	enableButtons ();
	loadEntities();
}

function enableButtons () {
	// Set the onclick action for the first button
	btn = document.getElementById("submit_e");
	//submiting and uploading data to the cloud
	btn.onclick= function(){
		register();
	};
	btn.value="Submit/Update";

	btn = document.getElementById("delete_e");
	//submiting and uploading data to the cloud
	btn.onclick= function(){
		removeEntities();
	};
	btn.value="Delete";

	btn = document.getElementById("retrieve_e");
	btn.onclick=function(){
		loadEntities();
	};
	btn.value="Retrieve Entities";

}

function register(){
	var name=document.getElementById("entity_id").value;
	var description=document.getElementById("entity_description").value;
	var dl_link=document.getElementById("entity_dl").value;
	var doc_link=document.getElementById("entity_doc").value;

	var request = gapi.client.gnosis_endpoints.update({'name':name, 'description':description,'dl_link':dl_link,'doc_link':doc_link});

	request.execute(packageCallback);
}

function loadEntities(){
	var request = gapi.client.gnosis_endpoints.getEntities();
	request.execute(updateTableCallback);
}


// Process the JSON response
// In this case, just show an alert dialog box
// displaying the value of the message field in the response
function updateTableCallback (response){
	var lines = response.display_msg.split('\n');
	var i,j;
	var table = document.getElementById("e_list");

	//delete all rows first
	for(j=(table.rows.length-1); j>0; j--){
		table.deleteRow(j);
	}

	for(i =0; i<(lines.length-1); i++){
		//code here using lines[i]
		var words = lines[i].split('*');

		var row = table.insertRow(1);

		var c1 = row.insertCell(0);
		var c2 = row.insertCell(1);
		var c3 = row.insertCell(2);
		var c4 = row.insertCell(3);
		var c5 = row.insertCell(4)
		var btn = document.createElement("input");
		btn.type = 'checkbox';
		btn.id = words[0];

		//assign words to cells
		c1.innerHTML = words[0];
		c2.innerHTML = words[1];
		c3.innerHTML = words[2];
		c4.innerHTML = words[3];
		c5.appendChild(btn);
	}
}

function removeEntities(){
	var table = document.getElementById("e_list");
	var checkboxes = document.getElementsByTagName("input");
	var entity_list = "";

	var i,j;
	for(i=1; i<checkboxes.length;i++){
		if(checkboxes[i].type == 'checkbox'){
			var chk = checkboxes[i].checked;
			// alert(chk);
			if(chk){
				entity_list+=(checkboxes[i].id+"*");
			}
		}
	}
	// alert(entity_list);
	var request = gapi.client.gnosis_endpoints.deleteEntities({'entity_list':entity_list});
	request.execute(packageCallback);
}

function packageCallback (response) {
	loadEntities();
	alert(response.display_msg);
}



