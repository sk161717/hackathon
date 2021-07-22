var elem=document.getElementById("elem");
elem.addEventListener('click',function(){
    anime({
        targets: elem,
        translateX: 250
    })
})
anime({
    targets: 'lib',
    translateX: 2500,
    rotate: '10turn',
    backgroundColor: '#FFF',
    duration: 80000
  });
  