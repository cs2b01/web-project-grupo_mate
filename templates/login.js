function getData(){
        var username = $('#username').val();
        var password = $('#password').val();
        var message = JSON.stringify({
                "username": username,
                "password": password
            });

        $.ajax({
            url:'/authenticate',
            type:'POST',
            contentType: 'application/json',
            data : message,
            dataType:'json',
            success: function(response){
            },
            error: function(response){
                if(response['status']==401){
                    alert("Comprobar username y/o contraseña");
                }else{
                    window.location.replace("/static/index.html")
                }
            }
        });
    }