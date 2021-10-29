// values to keep track of the number of letters typed, which quote to use. etc. Don't change these values.
var i = 0,
    a = 0,
    isBackspacing = false;

// Typerwrite text content. Use a pipe to indicate the start of the second line "|".  
var textArray = [
    "AskReddit", "AskMen", "Gaming", "FemaleFashionAdvice", "Nosleep", "LetsNotMeet", "Technology", "Funny", "Memes", "Politics", "News"
];

// Speed (in milliseconds) of typing.
var speedForward = 100, //Typing Speed
    speedWait = 1000, // Wait between typing and backspacing
    speedBackspace = 25; //Backspace Speed

//Run the loop
typeWriter("typewriter", textArray);

function typeWriter(id, ar) {

  var element = $("#" + id),
      aString = ar[a],
      eHeader = element.children("h1"); //Header element

  // Determine if animation should be typing or backspacing
  if (!isBackspacing) {
    
    // If full string hasn't yet been typed out, continue typing
    if (i < aString.length) {
        eHeader.text(eHeader.text() + aString.charAt(i));
        i++;
        setTimeout(function(){ typeWriter(id, ar); }, speedForward);
    }  
    // If full string has been typed, switch to backspace mode.
    else if (i == aString.length) {
      
      isBackspacing = true;
      setTimeout(function(){ typeWriter(id, ar); }, speedWait);
      
    }
    
  // If backspacing is enabled
  } else {
    
    // If either the header, continue backspacing
    if (eHeader.text().length > 0) {
      
      // If paragraph still has text, continue erasing, otherwise switch to the header.
      if (eHeader.text().length > 0) {
        eHeader.addClass("cursor");
        eHeader.text(eHeader.text().substring(0, eHeader.text().length - 1));
      }
      setTimeout(function(){ typeWriter(id, ar); }, speedBackspace);
    
    // If the head has no text, switch to next quote in array and start typing.
    } else { 
      
      isBackspacing = false;
      i = 0;
      a = (a + 1) % ar.length; //Moves to next position in array, always looping back to 0
      setTimeout(function(){ typeWriter(id, ar); }, 50);
      
    }
  }
}