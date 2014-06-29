
	/*changes to do in the web page when performing a search*/
	function search_query(static_path) {
		$(document).ready(function(){ 
			
			$("#search-submit").click(function(){																// when clicking in the submit button		
				var image = '<div id='+"cytoscapeweb"+'><img src='+static_path+"data/ajax-loader.gif"+'></div>' // load div with loading image
				$("#cytoscapeweb").replaceWith(image);															// replace	map div with loading image	
				$("#content_docs").html("");																	//clear documents div
				$("#content_clouds").html("");																	//clear cloud words div
				send_query($("#search").val(),0);																//send query  	
			});
		});
	};


	/*send query throught ajax to django to process LSI*/
	function send_query(query,bit) {
		$.ajax({
			type: 'POST',								
			url: '', 
			data: {"query": query},	
			success: function(data){					//when lsi processing is finished
				if (bit==0){							//if bit==0, reload page	
					location.reload();
				}
				else{	
					location.href="LSITopics.html";		//if bit==1, go to LSITopics.html	
				}
			},	
			error: function(){							//if an error occurred
				alert("Error: Something went wrong");	//send error massage
				$("#cytoscapeweb").html("");			//clear map div
			}
		});
	}
