var elem=document.getElementById("elem");
elem.addEventListener('click',function(){
    anime({
        targets: elem,
        translateX: 250
    })
})

var content=document.getElementById("content");
var animation = anime({
    targets: content,
    translateX: 270,
    direction: 'alternate',
    loop: true,
    easing: 'easeInOutQuad',
    autoplay: false
});

function loopp(t) {
    animation.tick(t);
    customRAF = requestAnimationFrame(loopp);
}

requestAnimationFrame(loopp);

var loop=true;
var easing='easeInOutQuad';
var direction='alternate';


var fish=document.getElementById("fish");

var fishTimeline=anime.timeline({
    loop,
    direction:'alternate'
})
fishTimeline.add({
    targets: fish,
    translateY: 100,
    translateX: 470,
    easing
  }).add({
    targets: fish,
    translateY: 0,
    translateX: 0,
    easing
  }).add({
    targets: fish,
    translateY: '-80',
    translateX: 470,
    easing
  })