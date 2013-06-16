function beatHeart(){
    $el = $('#heart')
    $el.toggleClass('beat');
    //var str= $el.html();
    //str = str.replace("1","2","g");
    //str = str.replace("0","1","g");
    //str = str.replace("2","0","g");
    //$el.html(str);
}


var authTimer = setInterval(function() {
    beatHeart();
}, 1000);

$('.heart-container').click(function() {
    beatHeart();
});

// on roll-over change 0's to 1's
// can we make this "wave" through the ascii?
