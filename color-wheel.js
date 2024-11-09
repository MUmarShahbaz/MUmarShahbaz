let hue = 0;
let saturation = 100; // Full saturation for vivid colors
let lightness = 81; // Moderate lightness for balanced brightness

function changeBackgroundColor() {
  // Set the body's background color using the HSL color model
  document.body.style.backgroundColor = `hsl(${hue}, ${saturation}%, ${lightness}%)`;

  // Increment the hue for the next color; reset to 0 after reaching 360
  hue = (hue + 1) % 360;
}

// Set an interval to call changeBackgroundColor every 20 milliseconds
setInterval(changeBackgroundColor, 20);