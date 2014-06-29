	/*get word clouds for a specific topic with ajax*/
	/*function getcloud(node_id,mesh){
		//if we need mesh terms select proper file
		//and reduce word size to 50%
		/*if (mesh){
		var file = 'topicwords2.js';
		var wordsize = "50%"; 
		}
		//if we need regular terms select proper file
		//and reduce word size to 70%
		else {
		var file = 'topicwords.js';
		var wordsize = "70%";
		}
		
		$(document).ready(function(){
			$.ajax({
				type: 'GET',
				url: '/UA/IEETA/Redmine/LSIproject/LSIsearch/static/data/'+file, 		// name of file to get
				dataType: "json",
				success: function(data){
					$("#content_clouds").css("font-size",wordsize);						//reduce word size
					$("#content_clouds").empty(),										//clear clouds div
					$("#content_clouds").jQCloud(data[node_id],{						//create cloud word with JQCloud
						delayedMode: true
					});
				},
				error: function(){alert("Error: Something went wrong");}
			});
		});
	}*/
	
						
	/*get most relevant documents by topic from json file with ajax*/	
	function retrieved_docs(static_path,topicid) {
		$("#content_docs").empty(),																					//clear documents div
		$(document).ready(function(){								
				$.ajax({
					type: 'GET',
					url: static_path+'data/list.json', 															// name of file to get
					dataType: "json",
					cache: false,
					success: function(data){
						for (doc in data){																	// for document relevant for a specific topic 
							var title = data[doc]["title"] + "<br />";										// get document title
							//var rating = data[doc]["rating"];													// get document pmid
							$("#content_docs").append(title.link("http://www.imdb.com/"+data[doc]["link"]));		// append title with link to pubmed
						}
					},
					error: function(){alert("Error: Something went wrong");}
				});
			});
	}