function postData(){
    var username = $('#username').val();
    var name = $('#name').val();
    var fullname = $('#fullname').val();
    var password = $('#password').val();
    var message = JSON.stringify({
        "username": username,
        "name": name,
        "fullname": fullname,
        "password": password
        });
        $.ajax({
            url:'/users',
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
                    alert("Username ya existe");
                }
            }
        });
    }