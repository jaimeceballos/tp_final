$(document).ready(function() {
	$('#compartir_contacto_form').submit(function(event){
		if ( $('#id_numero').val().length > 4 ) {
			alert('Revise la altura de calle.')
			event.preventDefault();
		}
		return;

	});
	$('.solo-numero').keyup(function (){
    this.value = (this.value + '').replace(/[^0-9]/g, '');
  });


	$('#interseccion_btn').click(function(event){
		$('#interseccion').toggle("slow",function(){

		});
		if($(this).text() == ' Agregar calle Intersección '){
			$(this).text(' Cancelar ');
		}else{
			$(this).text(' Agregar calle Intersección ');
		}
	});
	$('#buscar-direccion').click(function(event){
		var direccion = $('#id_direccion').val();
		var numero = $('#id_numero').val();
		var interseccion = $('#id_interseccion').val();
		var localidad = $("#id_localidad option:selected").text();
		var provincia = $('#id_provincia option:selected').text();
		var pais ='Argentina'
		if(direccion != ''){
			if(numero!=''){
				direccion = direccion.concat(' '+numero);
				if(interseccion != ''){
					direccion = direccion.concat(' & '+interseccion)
				}
				direccion = direccion.concat(' '+localidad.concat(' '+pais));
				var request = {
					address: direccion
				}
				geocoder.geocode(request,function(results,status){
					if(status = google.maps.GeocoderStatus.OK){
						 map.setCenter(results[0].geometry.location);
						 map.setZoom(17);
						 marker.setVisible(true);
            marker.setPosition(results[0].geometry.location);
						document.getElementById('id_latitud').value = results[0].geometry.location.lat();
		        document.getElementById('id_longitud').value = results[0].geometry.location.lng();
					}else{
						alert(status);
					}
				});
			}else if(numero == "" && interseccion != ""){
				direccion = direccion.concat(' & '+interseccion)
				direccion = direccion.concat(' '+localidad.concat(' '+pais));
				var request = {
					address: direccion
				}
				geocoder.geocode(request,function(results,status){
					if(status = google.maps.GeocoderStatus.OK){
						 map.setCenter(results[0].geometry.location);
						 map.setZoom(17);
						 marker.setVisible(true);
            marker.setPosition(results[0].geometry.location);
						document.getElementById('id_latitud').value = results[0].geometry.location.lat();
		        document.getElementById('id_longitud').value = results[0].geometry.location.lng();
					}else{
						alert(status);
					}
				});
			}else{
								alert('debe indicar una altura de calle.')
			}
		}else{
			alert('debe indicar una calle.')
		}
	})
	$('#id_localidad').change(function(event){
		var localidad = $("#id_localidad option:selected").text();
		var provincia = $('#id_provincia option:selected').text();
		var pais ='Argentina'
		localidad = localidad.concat(' '+provincia.concat(' '+pais));
		var request = {
			address: localidad
		}
		geocoder.geocode(request,function(results,status){
			if(status = google.maps.GeocoderStatus.OK){
				 map.setCenter(results[0].geometry.location);
				 map.setZoom(14);
			}else{
				alert(status);
			}
		});
		//$('#buscar-direccion').toggle();
	});
	$('#id_provincia').change(function(event){
		var localidades = $("#id_localidad");
		var valor = $(this).val()
		var to_load = '/core/obtenerciudades/'+valor+'/'
		var div = $('#share-contact');
		if(div.length > 0){
			var provincia = $('#id_provincia option:selected').text();
			provincia = provincia.concat(' argentina');
			var request = {
				address: provincia
			}
			geocoder.geocode(request,function(results,status){
				if(status = google.maps.GeocoderStatus.OK){
					 map.setCenter(results[0].geometry.location);
					 marker.setPosition(results[0].geometry.location);
					 map.setZoom(7);

				}
			});
		}
		$.get(to_load, function(data){
			var options = '<option value="">Seleccione Localidad</option>';
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

	function readURL(input){

		if(input.files && input.files[0]){
				var reader = new FileReader();
				reader.onload = function(e){
					$('#profileImg').attr('src',e.target.result);
				}
				reader.readAsDataURL(input.files[0]);
			}
		}
		$("#id_avatar").change(function(){
			readURL(this);
		});

		$("#id_editar_provincia").change(function(){
			var valor = $(this).val()
			var localidades = $("#id_editar_localidad");
			var to_load = '/core/obtenerciudades/'+valor+'/'
			$.get(to_load, function(data){
				var options = '<option value="">Seleccione Localidad</option>';
				for (var i =0; i < data.length; i ++){
					options += '<option value="'+data[i]["pk"]+'">' + data[i]["fields"]["localidad"] + '</option>';
				}
				localidades.empty();
				localidades.html(options);
				localidades.removeAttr('disabled');
			},"json");
			to_load = '/core/cantidad_en_provincia/'+valor+'/';
			$.get(to_load,function(data2){
				if($('#cantidad').is(':visible')){
						$('#cantidad').empty().append(data2)
				}else{
						$('#cantidad').empty().append(data2).parent().parent().toggle();
				}

			});
			to_load = '/core/contactos_provincia/'+ valor + '/';
			$.get(to_load,function(data3){
				$("#editar-results").empty();
				for(var i = 0; i < data3.length; i ++){

						var href = '<a href="javascript:editar('+ data3[i]["pk"] +');"><i class="glyphicon glyphicon-edit"></i></a>';
						var p = '<p>'+ data3[i]["fields"]["nombre"] +' - '+ data3[i]["fields"]["localidad"] +' '+ href +'</p>';
						$("#editar-results").append(p);
				}

			});
		});
		$("#id_editar_localidad").change(function(){
			var valor = $(this).val()
			var to_load = '/core/cantidad_en_ciudad/'+valor+'/';
			$.get(to_load,function(data2){
				$('#cantidad').empty().append(data2).parent().parent().toggle().toggle();
			});
			to_load = '/core/contactos_ciudad/'+ valor + '/';
			$.get(to_load,function(data3){
				$("#editar-results").empty();
				for(var i = 0; i < data3.length; i ++){
						var href = '<a href="javascript:editar('+ data3[i]["pk"] +');"><i class="glyphicon glyphicon-edit"></i></a>';
						var p = '<p>'+ data3[i]["fields"]["nombre"] + ' ' + href +'</p>';
						$("#editar-results").append(p);
				}

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

function mostrarDetalles(id){
	var toLoad ='/core/sugerido/'+id+'/';
	$.get(toLoad,function(data){

		$('#lblNombre').empty().append(data[0]["fields"]["nombre"]);
		var direccion;
		var telefono;
		if(data[0]["fields"]["interseccion"]!=""){
			direccion = data[0]["fields"]["direccion"] +' '+data[0]["fields"]["numero"]+' y '+data[0]["fields"]["interseccion"];
		}else{
			direccion = data[0]["fields"]["direccion"] +' '+data[0]["fields"]["numero"];
		}
		if(data[0]["fields"]["telefono_area"]!="" && data[0]["fields"]["telefono_numero"]!=""){
			telefono = '('+data[0]["fields"]["telefono_area"] +') - '+data[0]["fields"]["telefono_numero"];
		}
		$('#lblTelefono').empty().append(telefono);
		$('#lblDireccion').empty().append(direccion);
		$('#lblWeb').empty().append('<a href="http://'+data[0]["fields"]["sitio_web"]+'">'+ data[0]["fields"]["sitio_web"] +'</a>');
		$('#lblMail').empty().append(data[0]["fields"]["mail"]);
		var mapa = '<iframe class="col-md-12" frameborder="0" style="border:0;height:280px" src="https://www.google.com/maps/embed/v1/place?key=AIzaSyBuneURtJfQGvMv3cG5TQMomWarGPIQ14c&q='+ data[0]["fields"]["latitud"]+','+ data[0]["fields"]["longitud"] +'" allowfullscreen></iframe>';
		$('#showMapa').empty().append(mapa);
		var botonAceptar = '<a href="javascript:validar('+ data[0]["pk"] +');" class="btn btn-success" id="validar"> Validar </a>';
		var hiddenId = '<input type="hidden" val="'+ data[0]["pk"] +'" id="contactId">'
		var botonEditar =  '<a href="../editar/'+ data[0]["pk"] +'/" class="btn btn-info pull-right" id="editar"> Editar </a>';
		$('#botonsBox').empty().append(botonAceptar).append(botonEditar);
	});

}

function verificarSugeridos(){
	var toLoad = "/core/verificar_sugeridos/";
	var actual = parseInt($('#sugeridos').text());
	$.get(toLoad,function(data){
			if(parseInt(data) > 0 && parseInt(data)!= actual){
				$('#sugeridos').empty().append(data).parent().parent().show();
				//document.getElementById('alerta').play();
			}else if(parseInt(data) == 0 ){
				$('#sugeridos').empty().parent().parent().hide();
			}
		});
}

function validar(id){
	var toLoad = '../validar/'+id+'/';
	$.get(toLoad,function(data){
		$('#loader').show();
	})
		.done(function(){
			verificarSugeridos();
			$('#loader').hide();
			$('#lblNombre').empty();
			$('#lblTelefono').empty();
			$('#lblDireccion').empty();
			$('#lblWeb').empty();
			$('#lblMail').empty();
			$('#showMapa').empty();
			$('#botonsBox').empty();
			$('#sugerencia-'+id).fadeOut('1000');
		})
		.fail(function(){
			alert('Ocurrio un Error al intentar validar, vuelva a intentarlo mas tarde.');
			$('#loader').hide();
		})

}

function editar(id){
	var toLoad = '/core/editar_contacto/'+id+'/';
	$("#formulario").load(toLoad);
}
