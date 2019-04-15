// kakao login
var kakaoLogin;
var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
var success;

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(function () {
    // 사용할 앱의 JavaScript 키를 설정해 주세요.
    Kakao.init('1d42e53bd6515bec851dc1ba04e83568');
    kakaoLogin = function loginWithKakao() {
        // 로그인 창을 띄웁니다.
        Kakao.Auth.login({
            success: function(authObj) {
                Kakao.API.request({
                    url: '/v2/user/me',
                    success: function(res) {
                        // alert(JSON.stringify(authObj));
                        // alert(JSON.stringify(res));
                        $.ajaxSetup({
                            beforeSend: function(xhr, settings) {
                                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                                }
                            }
                        });
                        $.ajax({
                            type: 'POST',
                            url: 'kakao',
                            data: { 'authObj' : JSON.stringify(authObj),
                                    'res' : JSON.stringify(res)},
                            async: false,
                            success: function(data) {
                                 if(data != null) {
                                      // Do somothing when data is not null
                                      console.log('ajax success...')
                                 }
                            },
                            fail: function(error) {
                                console.log(JSON.stringify(error));
                            }
                       });
                    },
                    fail: function(error) {
                        alert(JSON.stringify(error));
                    }
                });
            },
            fail: function(err) {
                alert(JSON.stringify(err));
            }
        });
    };
});