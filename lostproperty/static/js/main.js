function beatHeart(state){
    if(state == 1){
        $('#heart_1').addClass('hide');
        $('#heart_2').removeClass('hide');
        state = 2;
    }else{
        $('#heart_2').addClass('hide');
        $('#heart_1').removeClass('hide');
        state = 1;
    }
    return state;
}

state = 1;
var authTimer = setInterval(function() {
    state = beatHeart(state);
}, 1500);

$('.heart-container').click(function() {
    state = beatHeart(state);
});

// on roll-over change 0's to 1's
// can we make this "wave" through the ascii?
