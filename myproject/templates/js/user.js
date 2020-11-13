// alert('ok')

$(function () {
    var token = localStorage.token;
    // var token = sessionStorage.token;
    $.ajax({
        url:'http://127.0.0.1:9000/myproject/userinfo',
        method:'GET',
        headers:{'Authorization':'JWT '+token},
        success:function (data) {
            var username = data['username'];
            var phone = data['phone'];
            var email = data['email'];
            var address = data['address'];
            var id = data['id'];
            $('#username').val(username);
            $('#phone').val(phone);
            $('#email').val(email);
            $('#address').val(address);
            console.log(data);
        },
        error:function (data) {
            console.log('error')
            console.log(data)
        }
    });

    var phonebut = $('#phone');
    // console.log(phonebut.val());
    //得到焦点
    phonebut.focus(function () {
        // console.log('13');
        // alert('ok');
        $.ajax({
            url:'http://127.0.0.1:9000/ver/phone/'+phonebut.val()+'/',
            method:'GET',
            headers:{'Authorization':'JWT '+token},
            success:function (data) {
                console.log('ok')
            },
            error:function (data) {
              console.log('error');
              if(data.status==404){
                  console.log('123');
                  $('#st1').css('display','block')
              }
            }
        })
    });
    //失去焦点
    phonebut.blur(function () {
        console.log('失去')
    });
    $('#sub').click(function () {

    })
});