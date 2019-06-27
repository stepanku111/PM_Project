let page_counter = 1;

$(document).on('click', '#reset-filter-btn', function() {
    $("#form-filter").trigger('reset');
    $("#reset-filter-btn").hide();
});

$(document).on('click', '#btn-scroll-to-top', function() {
    srollToTop();
});

$(document).ready(function(){
    $(window).scroll(function () {
        if ($(this).scrollTop() > 2500) {
            $('#btn-scroll-to-top').show();
        } else {
            $('#btn-scroll-to-top').hide();
        }
    });
});


function filter(data) {
    startLoadingAnimation();
    $.ajax({
        type: "GET",
        url: "filter",
        data: data,
        cache: false,
        success: function (html) {
            $('#cards').html(html);
            stopLoadingAnimation();
        }
    });
}

function filterUpdatePage(data) {
    srollToTop();
    $('#reset-filter-btn').show();
    filter(data);
}

function pagintationUpdatePage(data) {
    srollToTop();
    filter(data);
}

function srollToTop(){
    $("body,html").animate({
       scrollTop: 0
    }, 400);
}

function startLoadingAnimation() {
    $('#loadWrapper').show();
}

function stopLoadingAnimation() {
    $("#loadWrapper").hide();
}

$(document).on('click', '#form-filter-btn', function() {
    let data = { };
    let sizes = '';
    $.each($('#form-filter').serializeArray(), function () {
        if (this.name === 'user-size') {
            if (data[this.name] !== undefined){
                sizes += this.value + ',';
            }
            data['user-size'] = sizes.substring(0, sizes.length - 1);
        } else if (this.name === 'min-price'){
            if (this.value === ''){
                data['min-price'] = 0;
            } else {
                data['min-price'] = this.value;
            }
        } else if (this.name === 'max-price') {
            if (this.value === '') {
                data['max-price'] = 999999;
            } else {
                data['max-price'] = this.value;
            }
        } else {
            data[this.name] = this.value;
        }
    });
    sizes = '';
    filterUpdatePage(data);
});
