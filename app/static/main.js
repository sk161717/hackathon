
function LoadPicture(){
    img_element=document.createElement("img");
    state=document.getElementById("state").innerHTML

    img_element.className="image";
    img_element.src='/static/picture/'+state+'.png';
    if (state=="egg") {
        img_element.id="egg";
        img_element.width=600;
        img_element.height=600;
    }else if(state=="frog"){
        img_element.id="frog";
        img_element.width=400;
        img_element.height=400;
    }else{
        img_element.id="fish";
        img_element.width=400;
        img_element.height=400;
    }
    
    document.getElementsByClassName("parent_picture")[0].appendChild(img_element);
}
window.onload=LoadPicture();


var loop=true;
var easing='easeInOutQuad';
var direction='alternate';

var egg=document.getElementById("egg");
var fish=document.getElementById("fish");
var frog=document.getElementById("frog");

var eggTimeline=anime.timeline({
    loop,
    direction:'alternate'
})
eggTimeline.add({
    targets: egg,
    translateX:30,
    easing
}).add({
    targets:egg,
    translateX:-30,
    easing
}).add({
    targets:egg,
    translateX:0,
    easing
})

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

  var frogTimeline=anime.timeline({
      loop,
      direction:'alternate'
  })
  frogTimeline.add({
      targets:frog,
      translateY:200,
      easing:'spring',
      duration:200
  })