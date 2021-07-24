function LoadPicture(){
    var img_element=document.createElement("img");
    img_element.id="fish";
    img_element.src='/static/picture/otama_1_normal.png';
    img_element.width=200;
    img_element.height=200;
    document.getElementsByClassName("parent_picture")[0].appendChild(img_element);
}
window.onload=LoadPicture();

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