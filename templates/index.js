function comprobar_usuario(){
        $.ajax({
            url:'/current',
            type:'GET',
            contentType: 'application/json',
            dataType:'json',
            success: function(response){
                var nombre = response['name']+' '+response['fullname'];
                $('#welcome_user').html(nombre);
                show_bussiness();
            },
            error: function(response){
                alert("No hay usuario");
            }
        });
    }

function show_bussiness(){
        $.ajax({
            url:'/bussiness',
            type:'GET',
            contentType: 'application/json',
            dataType:'json',
            success: function(response){
                //alert(JSON.stringify(response));
                var i = 0;
                $.each(response, function(){

                    f = '<ul></ul><li>';

                    nombre = '<h4 class="subheading">';
                    nombre = nombre + response[i].bussiness_name;
                    nombre = nombre + '</h4>';

                    email = '<p class="text-muted">';
                    email = email + "Email: " + response[i].bussiness_email;
                    email = email + '</p>';

                    telefono = '<p class="text-muted">';
                    telefono = telefono + "Teléfono: "+ response[i].bussiness_number;
                    telefono = telefono + '</p>';

                    descricion = '<p class="text-muted">';
                    descricion = descricion + response[i].bussiness_description;
                    descricion = descricion + '</p>';

                    f = f + nombre + '</div><div class="timeline-body">';
                    f = f + descricion + email + telefono;
                    f = f + '</div></div></li></ul>';

                    i = i+1;
                    $('#all').append(f);
                });
            },
            error: function(response){
                alert(JSON.stringify(response));
            }
        });
    }

function addBussiness(){
    var bussiness_name = $('#bussiness_name').val();
    var bussiness_email = $('#bussiness_email').val();
    var bussiness_number = $('#bussiness_number').val();
    var bussiness_description = $('#bussiness_description').val();
    var message = JSON.stringify({
        "bussiness_name": bussiness_name,
        "bussiness_email": bussiness_email,
        "bussiness_number": bussiness_number,
        "bussiness_description": bussiness_description
        });
        $.ajax({
            url:'/bussiness',
            type:'POST',
            contentType: 'application/json',
            data: message,
            dataType:'json',
            success: function(response){
                },
            error: function(response){
                if(response['responseText'] == 'OK'){
                    window.location.replace("/static/index.html")
                }else if(response['responseText']=='NOT'){
                    alert("Esta empresa ya existe");
                }
            }
        });
    }