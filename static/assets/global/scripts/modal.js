/**
 * Created by wonhyuk on 10/12/16.
 */
function open_patient_modal(photoUrl, createdAt, isRotate){
    blockBackButton()
    $('#modal_photo').data('rotate', '0')
    $('#modal_photo').css('transform', 'none')
    $('#modal_photo').attr('src', photoUrl);
    $('#modal_header').text(createdAt);
    $('#picture_modal').css('display', 'block');
    $('#photo_delete').css('display', 'none')
    setInitPictureSize($('#modal_photo'))
    initModalSize($('#modal_photo'))
    // if(isRotate) modalImageRotate($('#modal_photo'))
}

function open_picture_modal(photoSrl, photoUrl, createdAt, isRotate) {
    blockBackButton()
    $('#modal_photo').data('rotate', '0')
    $('#modal_photo').css('transform', 'none')
    $('#modal_photo').attr('src', photoUrl);

    $('#modal_header').text(createdAt);
    $('#picture_modal').css('display', 'block');

    $('#photo_delete').unbind('click')
    $('#photo_delete').click(function () {
        $(".se-pre-con").css('display', "block");
        $.ajax({
        url: "profile_photo/?photoSrl="+String(photoSrl),
        type: "DELETE",
        contentType: "application/json; charset=utf-8",
        success: function (result) {
            $('#image_list').empty();
            $('#image_list').append($(result));
            $(".se-pre-con").fadeOut("slow");
            $('#picture_modal').css('display', 'none');
            return false;
        },
    });
    })
    setInitPictureSize($('#modal_photo'))
    initModalSize($('#modal_photo'))
    //
    // if(isRotate) modalImageRotate($('#modal_photo'))
}

function open_before_picture_modal(photoSrl, photoUrl, createdAt, isRotate) {
    blockBackButton()
    $('#modal_photo').data('rotate', '0')
    $('#modal_photo').css('transform', 'none')
    $('#modal_photo').attr('src', photoUrl);

    $('#modal_header').text(createdAt);
    $('#picture_modal').css('display', 'block');

    $('#photo_delete').unbind('click')
    $('#photo_delete').click(function () {
        $(".se-pre-con").css('display', "block");
        $.ajax({
        url: "before_photo/?photoSrl="+String(photoSrl),
        type: "DELETE",
        contentType: "application/json; charset=utf-8",
        success: function (result) {
            $('#before_image_list').empty();
            $('#before_image_list').append($(result));
            $(".se-pre-con").fadeOut("slow");
            $('#picture_modal').css('display', 'none');
            return false;
        },
    });
    })
    setInitPictureSize($('#modal_photo'))
    initModalSize($('#modal_photo'))
    // if(isRotate) modalImageRotate($('#modal_photo'))
}

function open_after_picture_modal(photoSrl, photoUrl, createdAt, isRotate) {
    blockBackButton()
    $('#modal_photo').data('rotate', '0')
    $('#modal_photo').css('transform', 'none')
    $('#modal_photo').attr('src', photoUrl);
    $('#modal_header').text(createdAt);
    $('#picture_modal').css('display', 'block');

    $('#photo_delete').unbind('click')
    $('#photo_delete').click(function () {
        $(".se-pre-con").css('display', "block");
        $.ajax({
        url: "after_photo/?photoSrl="+String(photoSrl),
        type: "DELETE",
        contentType: "application/json; charset=utf-8",
        success: function (result) {
            $('#after_image_list').empty();
            $('#after_image_list').append($(result));
            $(".se-pre-con").fadeOut("slow");
            $('#picture_modal').css('display', 'none');
            return false;
        },
    });
    })
    setInitPictureSize($('#modal_photo'))
    initModalSize($('#modal_photo'))
    // if(isRotate) modalImageRotate($('#modal_photo'))
}

$('.close, #modal_close').click(function () {
    $('#picture_modal').css('display', 'none');
})

function plusPxVal(val, inc){
    return String(getPxInt(val)+ inc) + 'px'
}

function getPxInt(val){
    return parseInt(String(val).trim('px'))
}

function initModalSize(img_elem) {
    $('#picture_modal .modal-body').css('width', plusPxVal(img_elem.css('width'), 20))
    $('#picture_modal .modal-body').css('height', plusPxVal(img_elem.css('height'), 20))
    $('#modal_photo').css('margin-top', '0')
    $('#modal_photo').css('margin-left', '0')
    $('#picture_modal .modal-content').css('width', plusPxVal(img_elem.css('width'), 30))
    $('#picture_modal .modal-content').css('height',plusPxVal(img_elem.css('height'), 140))
}

function modal_img_rotate(img_elem){
    img_elem.data('rotate', (parseInt(img_elem.data('rotate'))+90) % 360)
    img_elem.css('transform', 'rotate('+img_elem.data('rotate')+'deg)')

    if (img_elem.data('rotate') % 180 == 0) {
        setInitPictureSize(img_elem)
        $('#picture_modal .modal-body').css('width', plusPxVal(img_elem.css('width'), 20))
        $('#picture_modal .modal-body').css('height', plusPxVal(img_elem.css('height'), 20))
        img_elem.css('margin-top', '0')
        img_elem.css('margin-left', '0')
        $('#picture_modal .modal-content').css('width', plusPxVal(img_elem.css('width'), 30))
        $('#picture_modal .modal-content').css('height', plusPxVal(img_elem.css('height'), 140))
    } else {
        setRotatePictureSize(img_elem)
        $('#picture_modal .modal-body').css('width', plusPxVal(img_elem.css('height'), 20))
        $('#picture_modal .modal-body').css('height', plusPxVal(img_elem.css('width'), 20))
        img_elem.css('margin-top', String((getPxInt(img_elem.css('width')) - getPxInt(img_elem.css('height'))) / 2) + 'px')
        img_elem.css('margin-left', String((getPxInt(img_elem.css('height')) - getPxInt(img_elem.css('width'))) / 2) + 'px')
        $('#picture_modal .modal-content').css('width', plusPxVal(img_elem.css('height'), 30))
        $('#picture_modal .modal-content').css('height', plusPxVal(img_elem.css('width'), 140))
    }
}

function setInitPictureSize(img_elem) {
    var w = window.innerWidth;
    var h = window.innerHeight;
    if(getPxInt(img_elem.css('width')) > w) {
        img_elem.css('width', plusPxVal(w, -20))
    }
    // } else if (getPxInt(img_elem.css('height')) > h) {
    //     img_elem.css('height', plusPxVal(h, -20))
    // }
}

function setRotatePictureSize(img_elem) {
    var w = window.innerWidth;
    var h = window.innerHeight;
    if(getPxInt(img_elem.css('width')) > h) {
        img_elem.css('width', plusPxVal(h, -20))
    }
    // } else if (getPxInt(img_elem.css('height')) > w) {
    //     img_elem.css('height', plusPxVal(w, -20))
    // }
}

function blockBackButton(){
    history.pushState(null, null, "#picture");
    $(window).bind("hashchange", function(){
        $('#picture_modal').css('display', 'none');
    });
}