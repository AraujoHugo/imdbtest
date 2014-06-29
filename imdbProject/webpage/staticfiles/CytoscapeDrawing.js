  	
	/*Draw cytoscape graph with the topics from the LSI process*/ 
	function draw_cytoscape(static_path,vis){
		$(document).ready(function(){	
			$.ajax({
				type: 'GET',
				url: static_path+'data/coordinates.xml', 						// get file with topics coordinates
				dataType: "text",
				cache:false,
				success: function(data){
					cytoscape_create(data,vis);									//create graph
				},
				error: function(){alert("Error: Something went wrong");}
			});
		});
	};

	/*Define options for the graph drawing*/
	function cytoscape_create(net,vis) {		
		var draw_options = {
			network: net,													// load network
			edgeLabelsVisible: false,										// hide edge labels
			nodeLabelsVisible: false,										// hide nodes labels
			layout: "Preset",												// choose layout 
			visualStyle: visual_style,										// set the style at initialisation
			panZoomControlVisible: true 									// show pan zoom
		};          
		vis.draw(draw_options);												//draw graph
	};				
	
									                    
    /*visual style to use*/
    var visual_style = {
        global: {
            backgroundColor: "#ABCFD6"
        },
        nodes: {
            shape: "Circle",
            borderWidth: 3,
            borderColor: "#ffffff",
            size: {
                defaultValue: 20,
            },
            labelHorizontalAnchor: "center"
        },
    };
                    

	

					
