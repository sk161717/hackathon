function LoadPicture(){
    
}
window.onload=LoadPicture()

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