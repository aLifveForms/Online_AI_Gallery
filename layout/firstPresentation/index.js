window.onload = function () {
  var video1 = document.getElementById('1');
  var div1 = document.getElementById('v1');

  var video2 = document.getElementById('2');
  var div2 = document.getElementById('v2');

  var video3 = document.getElementById('3');
  var div3 = document.getElementById('v3');

  var video4 = document.getElementById('4');
  var div4 = document.getElementById('v4');

  var video5 = document.getElementById('5');
  var div5 = document.getElementById('v5');

  var vedioCollections = document.getElementsByClassName('videoInsert');
  var sectionTwo = document.getElementById('sectionTwo');

  var video6 = document.getElementById('6');
  var div6 = document.getElementById('v6');

  var video7 = document.getElementById('7');
  var div7 = document.getElementById('v7');

  var video8 = document.getElementById('8');
  var div8 = document.getElementById('v8');

  // var video9 = document.getElementById('9');
  // var div9 = document.getElementById('v9');

  var videofinal = document.getElementById('final');
  var divfinal = document.getElementById('final-section');

  let classesToAdd = ['fade-in', 'banner'];

  for (let i = 0; i < vedioCollections.length; i++) {
    setTimeout(function () {
      console.log('vidioCollections', i, 'play');
      vedioCollections[i].play();
      vedioCollections[i].volume = 0.1;
    }, 1000);
  }

  setTimeout(() => {
    console.log('sectionTwo show');
    sectionTwo.className = 'hidden';
    div1.classList.remove('hidden');
    div1.classList.add(...classesToAdd);
    video1.play();
  }, 16000);

  setTimeout(function () {
    div1.className = 'hidden';
    div2.classList.remove('hidden');
    div2.classList.add(...classesToAdd);
    video2.play();
  }, 31000);

  setTimeout(function () {
    div2.className = 'hidden';
    div3.classList.remove('hidden');
    div3.classList.add(...classesToAdd);
    video3.play();
  }, 46000);

  setTimeout(function () {
    div3.className = 'hidden';
    div4.classList.remove('hidden');
    div4.classList.add(...classesToAdd);
    video4.play();
  }, 61000);

  setTimeout(function () {
    div4.className = 'hidden';
    div5.classList.remove('hidden');
    div5.classList.add('show');
    div5.classList.add('banner');
    video5.play();
  }, 76000);

  setTimeout(function () {
    div5.className = 'hidden';
    div6.classList.remove('hidden');
    div6.classList.add('show', 'banner');
    video6.play();
  }, 80000);

  setTimeout(function () {
    div6.className = 'hidden';
    div7.classList.remove('hidden');
    div7.classList.add(...classesToAdd);
    video7.play();
  }, 82000);

  setTimeout(function () {
    div7.className = 'hidden';
    div8.classList.remove('hidden');
    div8.classList.add(...classesToAdd);
    video8.play();
  }, 93000);

  // setTimeout(function () {
  //   div8.className = 'hidden';
  //   div9.classList.remove('hidden');
  //   div9.classList.add(...classesToAdd);
  //   video9.play();
  // }, 110000);

  setTimeout(function () {
    div8.className = 'hidden';
    divfinal.className = 'fade-in';
    videofinal.className = 'show';
    videofinal.play();
  }, 126000);
};

function scrollDown(el) {
  el.animate(
    {
      scrollTop: el[0].scrollHeight,
    },
    500,
    function () {}
  );
}

$(document).ready(function () {
  window.setInterval(function () {
    scrollDown($('html,body'));
  }, 10000);
});
