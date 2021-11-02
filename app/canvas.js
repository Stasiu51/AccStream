const ctx = canvas.getContext('2d');

ctx.strokeStyle = 'black';
ctx.lineWidth = 5;

ctx.beginPath(); // Start a new path
ctx.moveTo(100, 50); // Move the pen to x=100, y=50.
ctx.lineTo(300, 150); // Draw a line to x=300, y=150.
ctx.stroke(); // Render the path