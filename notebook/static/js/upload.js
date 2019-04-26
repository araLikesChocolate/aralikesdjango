$(function () {
    $('#modalUpload').on('click', function(){
        console.log("Button Clicked")

        $.ajax({
            type: 'GET',
            url: '/upload_files',
            async: false,
            success: function(data) { //받아오는 것
                if(data != null) {
                    console.log(data)
                    $("#modalForm").html(data);
                    // $('div:last').removeClass('modal-backdrop');
                    // console.log($('#btnsubmit'));
                    $('div.modal-backdrop').remove();
                }
                else {
                    console.log("데이터 받기 실패");
                }
            },
            fail: function(error) {
                console.log('error');
            }
        });  
    });

    $("#btnsubmit").click(function(event){
        event.preventDefault();
        var data = new FormData();
        data.append("url", $("input[name=url]")[0].files[0]);
        data.append("publish", $("input[name=publish]").val());

        $.ajax({
            url:"upload_files/submit/",
            data:data,
            processData:false,
            contentType:false,
            type:'POST',
            success:function(data){
                alert("사진 로드 성공");

            },
            error: function(xhr,status){				
                alert("사진 로드 실패");
            }
        });
    });
});  