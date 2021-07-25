
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function LoadPicture(){
    img_element=document.createElement("img");
    state=document.getElementById("state").innerHTML
    
    if (state=="egg" || state=="frog"){
        picture_name=state;
    }else{
        table={'otama_phase1':'1','otama_phase2':'2','otama_phase3':'3'};
        let face=['angry','laugh','normal'];
        let ribbon=['','_ribbon'];
        picture_name="otama_phase"+table[state]+'_'+face[getRandomInt(3)]+ribbon[getRandomInt(2)];
    }

    img_element.className="image";
    img_element.src='/static/picture/'+picture_name+'.png';
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

//egg
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

//otama
var fishTimeline=anime.timeline({
    loop,
    direction:'alternate'
})
var posX=0;
var posY=0;
var velocityX=0;
var velocityY=0;
var rotate_=0;
for (let index = 0; index < 100; index++) {
    velocityX+=(Math.random()-0.5)*20;
    velocityY+=(Math.random()-0.5)*20;
    if (posX<-400 || 400<posX){
        velocityX=-velocityX;
    }
    if (posY<-300 || 300<posY){
        velocityY=-velocityY;
    }
    posX+=velocityX;
    posY+=velocityY;
    
    duration_=Math.random()*Math.abs(velocityX*velocityY)+500;
    if (velocityX<0){
        rotateX_=0;
    }else{
        rotateX_=180;
    }
    
    if(Math.random()<0.2){
        rotate_+=360*(getRandomInt(3)-1)
    }
    fishTimeline.add({
        targets:fish,
        translateY:{
            value:posY,
            duration:duration_
        },
        translateX:{
            value:posX,
            duration:duration_
        },
        easing,
        duration:duration_,
        rotateY:rotateX_,
        rotate:{
            value:rotate_,
            duration:duration_,
        }
    })
}

//frog
var frogTimeline=anime.timeline({
    loop,
    direction:'alternate'
})
var pos_f_X=0;
var pos_f_Y=0;

for (let index = 0; index < 100; index++) {
    if (Math.random()<0.3){
        frogTimeline.add({
            targets:frog,
            translateY:{
                value:(pos_f_Y-200),
                duration:600
            },
            easing:'spring'
        }).add({
            targets:frog,
            translateY:{
                value:pos_f_Y,
                duration:600
            },
            easing:'spring',
            duration:100
        })
    }else{
        pos_f_X+=(Math.random()-0.5)*100;
        pos_f_Y+=(Math.random()-0.5)*100;
        frogTimeline.add({
            targets:frog,
            translateY:pos_f_Y,
            translateX:pos_f_X,
            easing,
            duration:200
        })
    }
    
    
}

