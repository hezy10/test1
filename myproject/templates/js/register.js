$(function () {

    $('#subbtn').click(function () {
        var username = $('#username').val();
        var pwd = $('#pwd').val();
        var cpwd = $('#cpwd').val();
        var phone = $('#phone').val();
        var email = $('#email').val();
        var address = $('#address').val();
        var data = {
            'username':username,
            'password':pwd,
            'cpwd':cpwd,
            'phone':phone,
            'email':email,
            'address':address
        };
        $.ajax({
            type:'POST',
            url:'http://127.0.0.1:9000/myproject/register/',
            contentType:'application/json;charset=UTF-8',
            data:JSON.stringify(data),
            success:function (data) {
                // location.href = '/user.html'
                //浏览器关闭失效
                sessionStorage.token = data.token;
                //长期有效
                localStorage.token = data.token;
                console.log(data);
                location.href = '/login.html'

            },
            error:function () {
                location.href = '/register.html'
            }

        })
    })
});