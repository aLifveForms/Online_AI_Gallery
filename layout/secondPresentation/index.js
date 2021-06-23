var videoDo1, videoDo2, videoDo3, videoDo4, videoDo5, videoDo6, videoDo7, videoDo8, videoDo9; 
var divDo1, divDo2, divDo3, divDo4, divDo5, divDo6, divDo7, divDo8, divDo9;
var video1, video2, video3, video4, video5, video6, video7, video8, video9; 
var div1, div2, div3, div4, div5, div6, div7, div8, div9;   
var vedioCollections, firstSection, divFinal, videofinal;     
   
window.onload = function () {
  videoDo1 = document.getElementById('v1');
  divDo1 = document.getElementById('d1');

  videoDo2 = document.getElementById('v2');
  divDo2 = document.getElementById('d2');

  videoDo3 = document.getElementById('v3');
  divDo3 = document.getElementById('d3');

  videoDo4 = document.getElementById('v4');
  divDo4 = document.getElementById('d4');

  videoDo5 = document.getElementById('v5');
  divDo5 = document.getElementById('d5');

  videoDo6 = document.getElementById('v6');
  divDo6 = document.getElementById('d6');

  videoDo7 = document.getElementById('v7');
  divDo7 = document.getElementById('d7');

  videoDo8 = document.getElementById('v8');
  divDo8 = document.getElementById('d8');

  // videoDo9 = document.getElementById('v9');
  // divDo9 = document.getElementById('d9');

  video1 = document.getElementById('vi1');

  video2 = document.getElementById('vi2');

  video3 = document.getElementById('vi3');

  video4 = document.getElementById('vi4');

  video5 = document.getElementById('vi5');

  video6 = document.getElementById('vi6');

  video7 = document.getElementById('vi7');

  video8 = document.getElementById('vi8');

  video9 = document.getElementById('vi9');

  vedioCollections = document.getElementsByClassName('videoInsert');
  firstSection = document.getElementById('firstSection');

  videofinal = document.getElementById('final');
  divfinal = document.getElementById('divFinal');

  let classesToAdd = ['fade-in', 'banner'];

  for (let i = 0; i < vedioCollections.length; i++) {
    setTimeout(function () {
      console.log('vidioCollections', i, 'play');
      vedioCollections[i].play();
      vedioCollections[i].volume = 0.1;
    }, 107000);
  }

  
  setTimeout(() => {
    video1.className = 'hidden';
    video2.className = 'hidden';
    video3.className = 'hidden';
    video4.className = 'hidden';
    video5.className = 'hidden';
    video6.className = 'hidden';
    video7.className = 'hidden';
    video8.className = 'hidden';
    

    videoDo1.classList.remove('hidden');
    videoDo2.classList.remove('hidden');
    videoDo3.classList.remove('hidden');
    videoDo4.classList.remove('hidden');
    videoDo5.classList.remove('hidden');
    videoDo6.classList.remove('hidden');
    videoDo7.classList.remove('hidden');
    videoDo8.classList.remove('hidden');
   

    video1.pause();
    video2.pause();
    video3.pause();
    video4.pause();
    video5.pause();
    video6.pause();
    video7.pause();
    video8.pause();
    


    videoDo1.play();
    videoDo2.play();
    videoDo3.play();
    videoDo4.play();
    videoDo5.play();
    videoDo6.play();
    videoDo7.play();
    videoDo8.play();
    
  }, 920000);


  setTimeout(function () {
    video1.play();
  }, 1000);

  setTimeout(function () {
    video2.play();
  }, 16000);

  setTimeout(function () {
    video3.play();
  }, 31000);

  setTimeout(function () {
    video4.play();
  }, 46000);

  setTimeout(function () {
    video5.play();
  }, 60000);

  setTimeout(function () {
    video6.play();
  }, 63000);

  setTimeout(function () {
    video7.play();
  }, 64000);

  setTimeout(function () {
    video8.play();
  }, 75000);
  

  setTimeout(function () {
    firstSection.className ="hidden"
    divfinal.className = 'fade-in';
    videofinal.className = 'show';
    videofinal.play();
  }, 107000);

};

