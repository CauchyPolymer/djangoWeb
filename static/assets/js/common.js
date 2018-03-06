/**
 * Created by wonhyukcho on 2018. 3. 3..
 */
function goToMain(){
    $.ajax({
        url: "main/",
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        success: function (result) {
            $('.main-container').empty()
            $('.main-container').append(result)
        },
    });
}

function validateEmail(sEmail) {
        var filter = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
        if (filter.test(sEmail)) {
            return true;
        }
        else {
            return false;
        }
    }

function chkPwd(str){
     var pw = str;
     var num = pw.search(/[0-9]/g);
     var eng = pw.search(/[a-z]/ig);
     var spe = pw.search(/[`~!@@#$%^&*|₩₩₩'₩";:₩/?]/gi);

     if(pw.length < 6 || pw.length > 20){
      alert("비밀번호는 6자리 ~ 20자리 이내로 입력해주세요.");
      return false;
     }
     if(pw.search(/₩s/) != -1){
      alert("비밀번호는 공백업이 입력해주세요.");
      return false;
     } if(num < 0 || eng < 0){
      alert("비밀번호는 영문, 숫자를 혼합하여 입력해주세요.");
      return false;
     }

     return true;
}