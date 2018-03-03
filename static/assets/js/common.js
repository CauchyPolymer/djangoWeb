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