// $(document).on('click', '#form-filter-btn', function() {
//     $.get(showFilter, onAjaxSuccess);
//     startLoadingAnimation();

//     function onAjaxSuccess(data)
//     {
//         stopLoadingAnimation();

//     }

//     function startLoadingAnimation()
//     {
//         let img = $("#img");
//         let imgWrapper = $('#load-img-wrapper');

//         img.each(function () {
//             let h = $(this).height();
//             let w = $(this).width();

//             let div_h = $('#img').height();
//             let div_w = $('#img').width();

//             this.style.marginLeft = Math.round(((div_w - w) / 2) + window.innerWidth / 2) - 32 - 8 + 'px';
//             this.style.marginTop = Math.round(((div_h - h) / 2) + window.innerHeight / 2) - 32 - 8 + 'px';
//         });

//         imgWrapper.show();
//         img.show();

//     }

//     function stopLoadingAnimation()
//     {
//         $("#img").hide();
//     }
// });

// function showFilter(url, selector, data) {
//     $.ajax({
//         type: "GET",
//         url: "filter",
//         data: data,
//         cache: false,
//         success: function (html) {
//             $(selector).html(html);
//         }
//     });
// }
