let sizeListTitleClickCount = 0;
let priceTitleClickCount = 0;
const animationTime = 500;
const animationType = this.easing;

$(document).on('click', '#size-list-title', function() {
    if (sizeListTitleClickCount % 2 === 0){
        sizeListTitleClickCount += 1;
        $('#size-list-block').show(animationTime, animationType);
    } else {
        sizeListTitleClickCount += 1;
        $('#size-list-block').hide(animationTime, animationType);
    }
});

$(document).on('click', '#price-title', function() {
    if (priceTitleClickCount % 2 === 0){
        priceTitleClickCount += 1;
        $('#price-block').show(animationTime, animationType);
    } else {
        priceTitleClickCount += 1;
        $('#price-block').hide(animationTime, animationType);
    }
});
