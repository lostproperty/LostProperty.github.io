function beatHeart(){
    $('#heart').toggleClass('beat');
}


var authTimer = setInterval(function() {
    beatHeart();
}, 1000);

$('.heart-container').click(function() {
    beatHeart();
});

// on roll-over change 0's to 1's
// can we make this "wave" through the ascii?
