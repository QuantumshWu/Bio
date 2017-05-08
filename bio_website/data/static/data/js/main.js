
(function($) {
$(document).ready(function(){
   $("#s1").mousemove(function(){
		if ($("#s1").val() == '')
		{
			$("#g1").attr("disabled",false);
			
		}
		else
		{	
			$("#g1").attr("disabled",true);
			
		}
	});

   	$("#g1").mousemove(function(){
		if ($("#g1").val() == '')
		{
			$("#s1").attr("disabled",false);
			
		}
		else
		{	
			$("#s1").attr("disabled",true);
			
		}
	});

   	$(".addtag").click(function(){

	    $(this).prevAll("select:first").after("\
	    	<br>\
	    	<select class='form-control feature'>\
	    	</select>\
	    ");
	    
	});

	$("#data-post").click(function(){
	    var mito = "";
	    $("#MitoFeature").prev().nextUntil("button","select").each(function(){
	    	mito = mito + "," + $(this).val();
	    })
	    $("#MitoFeature").append("<option>"+mito+"</option>");
	    $("#MitoFeature").val(mito);

	    var micro = "";
	    $("#MicroFeature").prev().nextUntil("button","select").each(function(){
	    	micro = micro + "," + $(this).val();
	    })
	    $("#MicroFeature").append("<option>"+micro+"</option>");
	    $("#MicroFeature").val(micro);

	    var cell = "";
	    $("#CellFeature").prev().nextUntil("button","select").each(function(){
	    	cell = cell + "," + $(this).val();
	    })
	    $("#CellFeature").append("<option>"+cell+"</option>");
	    $("#CellFeature").val(cell);

	    
	});

	$("body").on("click",".feature",function()
	{
		var cur = $(this);
		$.ajax(
		{
			url:"/list/"+cur.prevAll("label:first").html(),    
				
			type:'GET',           
			success:function(arg)
			{   
				var obj=jQuery.parseJSON(arg);  
				var length=obj.length;
				var feature = "";
				if (length>0)
				{
					for(var i=0;i<length;i++)
					{
						feature = feature + "<option>" + obj[i] + "</option>";
							
					}
				}
					
	            cur.html(feature);
	            cur.removeClass("feature");
					
			},
					
		});	
	});	
});





$("#AList").bootstrapTable({
			
			columns: [{
        		field: 'name',
        		title: 'Username',
				align: 'center'
    		}, {
				field: 'delete',
                title: 'operate',
				align: 'center'
			
			
    		}],
    		
		});


})(jQuery);
