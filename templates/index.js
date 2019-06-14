function comprobar_usuario(){
        $.ajax({
            url:'/current',
            type:'GET',
            contentType: 'application/json',
            dataType:'json',
            success: function(response){
                var nombre = response['name']+' '+response['fullname'];
                $('#welcome_user').html(nombre)
            },
            error: function(response){
                alert(JSON.stringify(response));
            }
        });
    }