var geocoder;
var map;
var marker;
var address = document.getElementById('id_direccion');

function initialize() {
  geocoder = new google.maps.Geocoder();
  var latlng = new google.maps.LatLng(-43.3000101, -65.1089705);
  var mapOptions = {
    zoom: 14,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    //disableDefaultUI: true
  }
  map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
  google.maps.event.addListener(map, 'click', function() {

  });
  var customicons = {
    1:{
      icon:'/static/img/iconos/seguridad4040.ico'
    },
    2:{
      icon:'/static/img/iconos/hospital2032.ico'
    }
  }
  function bindInfoWindow(marker,map,infoWindow,html){
    google.maps.event.addListener(marker,'click',function(){
      infoWindow.setContent(html);
      infoWindow.open(map,marker);
    });
  }
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      map.setCenter(pos);
      geocoder.geocode({
        latLng: pos
      }, function(responses) {
        if (responses && responses.length > 0) {

          var infoWindow = new google.maps.InfoWindow;
          var ciudad =  responses[0].address_components[2].long_name;
          var provincia = responses[0].address_components[4].long_name;
          //var pais = responses[0].address_components[5].long_name;
          var to_load =  '../obtenercontactos/'+provincia+'/'+ciudad+'/'
          $.get(to_load, function(data){
      			for (var i =0; i < data.length; i ++){
              var nombre = data[i]['fields']['nombre']
              var direccion = data[i]['fields']['direccion'] + ' ' + data[i]['fields']['numero']
              var tipo = data[i]['fields']['tipo_contacto']
              var telefono = data[i]['fields']['telefono_area']+data[i]['fields']['telefono_numero']
              var point = new google.maps.LatLng(
                parseFloat(data[i]['fields']['latitud']),
                parseFloat(data[i]['fields']['longitud']));
              var html = "<b>" + nombre + "</b><br><i class='glyphicon glyphicon-map-marker'></i> " + direccion + "<br><i class='glyphicon glyphicon-phone-alt'></i> " + telefono;
              var icon = customicons[tipo] || {};
              var marker = new google.maps.Marker({
                map: map,
                position: point,
                icon: icon.icon
              });
              bindInfoWindow(marker, map, infoWindow, html);
      				//options += '<option value="'+data[i]["pk"]+'">' + data[i]["fields"]["localidad"] + '</option>';
      			}

      		},"json");
        } else {
          marker.formatted_address = 'No se puede determinar la direccion en esta ubicacion.';
        }

      });

    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }


}
