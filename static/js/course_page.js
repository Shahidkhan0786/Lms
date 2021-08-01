var player;
var video_list
document.onreadystatechange = function () {
    if (document.readyState == 'interactive') {
        player = document.getElementById("player")
        video_list = document.getElementById("video_list")

        maintainRatio()


    }
}
function maintainRatio() {
    var w = player.clientWidth
    var h = (w * 9) / 16
    console.log({ w, h });
    player.height = h
    video_list.style.maxHeight = h + "px"
}
window.onresize = maintainRatio

$(document).ready(function(){
    $("#ply1").click(function(){
        
      $("#video_list").toggle();
      
    });
  });

  function myFunction(x) {
    if (x.matches) { // If media query matches
      document.getElementById('ply1').style.display = "inline";
      
    } else {
        document.getElementById('ply1').style.display = "none";
    }
  }
  
  var x = window.matchMedia("(max-width: 570px)")
  myFunction(x) // Call listener function at run time
  x.addListener(myFunction) // Atta