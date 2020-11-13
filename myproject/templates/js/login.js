// alert('ok');

$(function () {
    $('#sub').click(function () {
        var username = $('#username').val();
        var pwd = $('#pwd').val();
        var data = {
            'username':username,
            'password':pwd
        };
        $.ajax({
            type:'POST',
            url:'http://127.0.0.1:9000/myproject/token/',
            contentType:'application/json;charset=UTF-8',
            data:JSON.stringify(data),
            success:function (data) {
                localStorage.token = data.token
                console.log(data);
                location.href='/user.html'
                // location.hash='/user.html'
            },
            error:function () {
                console.log('error')
            }
        })
    })
});