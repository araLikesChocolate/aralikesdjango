function file_get() {
    console.log("Button Clicked")     

    if($(".modal-content").hasClass("modal-footer") === false) {
        $(".modal-footer").show();
    }

    $.ajax({
        type: 'GET',
        url: '/upload',
        async: false,
        success: function(data) { //받아오는 것
            if(data != null) {
                console.log(data)
                $("#modalForm").html(data);
                // $('div').removeClass("modal-backdrop");
                var m = $('#myModal')
                m.addClass('show')
                m.attr('style', 'display:block;')
                // show  aria-modal="true", style="display:block"
                $('span.loading').hide();
            }
            else {
                console.log("데이터 받기 실패");

            }
        },
        fail: function(error) {
            console.log('error');
        }
    });  
}

$(function () {

    $("#btnsubmit").click(function(event){

        event.preventDefault();
        // var data = new FormData();
        // data.append("url", $("input[name=url]")[0].files[0]);
        // data.append("publish", $("input[name=publish]").val());

        $('span.loading').show();
        $('#img-form').hide();
        $(".modal-footer").hide();

        var form = $('form')[0];
        //FormData parameter에 담아줌
        var formData = new FormData(form);

        $.ajax({
            url:"upload/",
            data:formData,
            processData:false,
            contentType:false,
            type:'POST',
            success:function(data){
                alert("사진 로드 성공");
                if(data != null) {
                    // 업로드 결과 보여주기
                    $('span.loading').hide();
                    $("#modalForm").html(data);
                    $(".modal-footer").hide();
                    $(".close").click(function(event){
                        $('#myModal').removeClass('show')
                        $('#myModal').removeAttr("style");                    
                        window.location.replace('/')
                        });
                }
            },
            error: function(xhr,status){				
                alert("사진 로드 실패");
                $('#myModal').removeClass('show')
                $('#myModal').removeAttr("style");
            }
        });
    });            
});  

