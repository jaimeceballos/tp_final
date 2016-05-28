$(document).ready(function() {
	$('#id_localidad').prop('disabled','disabled');
	$('#interseccion_btn').click(function(event){
		$('#interseccion').toggle("slow",function(){

		});
		if($(this).text() == ' Agregar calle Intersección '){
			$(this).text(' Cancelar ');
		}else{
			$(this).text(' Agregar calle Intersección ');
		}
	});
	$('#id_provincia').change(function(event){
		var localidades = $("#id_localidad");
		var valor = $(this).val()
		var to_load = '../obtenerciudades/'+valor+'/'
		$.get(to_load, function(data){
			var options;
			for (var i =0; i < data.length; i ++){
				options += '<option value="'+data[i]["pk"]+'">' + data[i]["fields"]["localidad"] + '</option>';
			}
			localidades.empty();
			localidades.html(options);
			localidades.removeAttr('disabled');
		},"json");
	});
	$('#provincia').change(function(event){
		$("#id_provincia option").each(function(){
	  	alert($(this).text().toUpperCase());

		});
	});
});
$(function(){
	$("#slider").click(function(){
			if($("#slider-icon").hasClass('glyphicon-chevron-right')){
				$("#content,#slider-icon,#slider-back-icon").animate({
					left:"+="+$("#content").outerHeight()
				},800,function(){

				});
				$("#slider-icon").removeClass('glyphicon-chevron-right').addClass('glyphicon-chevron-left');
				$("#slider").removeAttr('title').attr('title','Haga click aqui para cerrar el panel de carga');
			}else{
				$("#content,#slider-icon,#slider-back-icon").animate({
					left:"-="+$("#content").outerHeight()
				},800,function(){

				});
				$("#slider-icon").removeClass('glyphicon-chevron-left').addClass('glyphicon-chevron-right');
				$("#slider").removeAttr('title').attr('title','Haga click aqui para Cargar un nuevo lugar.');
			}
	});
});
