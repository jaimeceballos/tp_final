var geocoder;
var map;
var marker;
var address = document.getElementById('id_direccion');

function initialize() {
  geocoder = new google.maps.Geocoder();
  var latlng = new google.maps.LatLng(-43.3000101, -65.1089705);
  var mapOptions = {
    zoom: 17,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    //disableDefaultUI: true
  }
  map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
  google.maps.event.addListener(map, 'click', function() {

  });


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
        document.getElementById('ciudad').value =  responses[0].address_components[2].long_name;
        document.getElementById('provincia').value =  responses[0].address_components[4].long_name;
        $("#id_provincia option").each(function(){
          if ($(this).text().toUpperCase() == $('#provincia').val().toUpperCase() )
            $(this).attr("selected","selected");
        });
        $("#id_localidad option").each(function(){
          alert('ingreso');
          if ($(this).text().toUpperCase() == $('#ciudad').val().toUpperCase() )
            $(this).attr("selected","selected");
            $('#id_localidad').removeAttr("disabled");
        });
        document.getElementById('pais').value =  responses[0].address_components[5].long_name;
        document.getElementById('id_direccion').value = responses[0].address_components[1].long_name;
        document.getElementById('id_numero').value = responses[0].address_components[0].long_name;
        document.getElementById('id_latitud').value = responses[0].geometry.location.lat();
        document.getElementById('id_longitud').value = responses[0].geometry.location.lng();
        document.getElementById('address').value = responses[0].formatted_address;
        codeAddress();
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
function geocodePosition(pos) {

geocoder.geocode({
  latLng: pos
}, function(responses) {
  if (responses && responses.length > 0) {
    marker.formatted_address = responses[0].formatted_address;
    //marker.formatted_address = responses[0].formatted_address;
  } else {
    marker.formatted_address = 'No se puede obtener datos de la ubicacion';
  }
  document.getElementById('address').value = marker.formatted_address;
  document.getElementById('id_direccion').value = responses[0].address_components[1].long_name;
  document.getElementById('id_numero').value = responses[0].address_components[0].long_name;
  document.getElementById('id_latitud').value = responses[0].geometry.location.lat();
  document.getElementById('id_longitud').value = responses[0].geometry.location.lng();
});
}

function codeAddress() {
var address = document.getElementById('address').value;
geocoder.geocode({
  'address': address
}, function(results, status) {
  if (status == google.maps.GeocoderStatus.OK) {
    map.setCenter(results[0].geometry.location);
    if (marker) {
      marker.setMap(null);
    }
    marker = new google.maps.Marker({
      map: map,
      draggable: true,
      position: results[0].geometry.location,
      title:"Arrastre para seleccionar la ubicacion"
    });
    google.maps.event.addListener(marker, 'dragend', function() {
      geocodePosition(marker.getPosition());
      if($("#slider-icon").hasClass('glyphicon-chevron-right')){
        $("#slider").trigger("click");
      }
    });
    google.maps.event.addListener(marker, 'click', function() {

      if (marker.formatted_address) {
        document.getElementById('id_direccion').value = marker.formatted_address;
      } else {
        //document.getElementById('id_direccion').value = address;
      }

    });
    google.maps.event.trigger(marker, 'click');
  } else {
    alert('No se pudo geolocalizar la posicion: ' + status);
  }
});
}
