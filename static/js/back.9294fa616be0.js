function myFunction(x) {
    if (x.matches) { // If media query matches
      document.getElementById('headd').style.background = "black";
      
    } 
  }


 var x = window.matchMedia("(max-width: 1024px)")
  myFunction(x) // Call listener function at run time
  x.addListener(myFunction) // Atta

