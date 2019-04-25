// csrf
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// naver login
var naverLogin = new naver.LoginWithNaverId(
        {
            clientId: "eSp9Qh3o0n6xt21BDo57",
            // callbackUrl: "http://localhost:8000/registration/login/",
            callbackUrl: "http://localhost:8000/login/",
            // callbackUrl: "http://" + window.location.hostname + ((location.port==""||location.port==undefined)?"":":" + location.port) + "/oauth/sample/callback.html",
            isPopup: false,
            loginButton: {color: "green", type: 3, width:240, height: 50}
        });

/* (4) 네아로 로그인 정보를 초기화하기 위하여 init을 호출 */
$(function () {
    naverLogin.init();
})
        
/* (5) 현재 로그인 상태를 확인 */
window.addEventListener('load', function () {
    naverLogin.getLoginStatus(function (status) {
        if (status) {
            /* (6) 로그인 상태가 "true" 인 경우 로그인 버튼을 없애고 사용자 정보를 출력합니다. */
            var list = [typeof(naverLogin['user']['id']), typeof(naverLogin['user']['email']), typeof(naverLogin['user']['name']),
            typeof(naverLogin['user']['nickname']), typeof(naverLogin['user']['profile_image'])];
            console.log($.inArray('undefined', list));

            if( list.includes('undefined') || list.includes('null') ) {
                alert('정보 제공에 모두 동의해주세요.');
                naverLogin.reprompt();
                return;
            }
            setLoginStatus();
        }
    });
});

/* (6) 로그인 상태가 "true" 인 경우 로그인 버튼을 없애고 사용자 정보를 출력합니다. */
function setLoginStatus() {
    // var profileImage = naverLogin.user.getProfileImage();
    // var nickName = naverLogin.user.getNickName();
    console.log(naverLogin);
    
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            var csrftoken = $.cookie('csrftoken');
            console.log(csrftoken);
            console.log('csrf: ', $.removeCookie('csrftoken', { path: '/',}));
            $.cookie('csrftoken', csrftoken, { path: '/',});
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            }
        }
    });

    $.ajax({
        type: 'POST',
        url: '',
        data: { 
                service_type: 'NAVER',
                id: naverLogin['user']['id'],
                email: naverLogin['user']['email'],
                name: naverLogin['user']['name'],
                nickname: naverLogin['user']['nickname'],
                profile_image: naverLogin['user']['profile_image']
            },
        async: false,
        success: function(data) {
            if(data != null) {
                // Do somothing when data is not null
                // console.log(res['properties']['nickname'])
                console.log('ajax naver login success...')
                // console.log(data)
                window.location.replace(data)
            }
        },
        fail: function(error) {
            console.log('ajax naver login failed...')
            // window.location.replace('/')
            console.log(JSON.stringify(error));
        }
    });   
 }


 // logout

function naverLogout() {
    naverLogin.getLoginStatus(function (status) {
        if (status) {
            /* (6) 로그인 상태가 "true" 인 경우 로그아웃 */
            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                    }
                }
            });
    
            $.ajax({
                type: 'POST',
                url: 'logout/',
                async: false,
                success: function(data) {
                    if(data != null) {
                        // Do somothing when data is not null
                        // console.log(res['properties']['nickname'])
                        console.log('ajax naver logout success...')
                        // console.log(data)
                        console.log('csrf remove:', $.removeCookie('csrftoken', { path: '/',}))
                        window.location.replace(data)
                    }
                },
                fail: function(error) {
                    console.log('ajax naver logout failed...')
                    // window.location.replace('/')
                    console.log(JSON.stringify(error));
                }
            });
            naverLogin.logout();
        }
    });
};