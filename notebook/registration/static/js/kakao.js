
// kakao login
var kakaoLogin;

$(function () {
    // 사용할 앱의 JavaScript 키를 설정해 주세요.
    Kakao.init('1d42e53bd6515bec851dc1ba04e83568');
    kakaoLogin = function loginWithKakao() {
        // 로그인 창을 띄웁니다.
        Kakao.Auth.login({
            success: function(authObj) {
                alert(JSON.stringify(authObj));
                Kakao.API.request({
                    url: '/v2/user/me',
                    success: function(res) {
                        alert(JSON.stringify(res));
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