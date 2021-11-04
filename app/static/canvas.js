const canvas = document.getElementById('canvas');
const width = canvas.width
const height = canvas.height
const ctx = canvas.getContext('2d');

function animate__c() {
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 5;

    ctx.beginPath(); // Start a new path
    ctx.moveTo(100, 50); // Move the pen to x=100, y=50.
    ctx.lineTo(300, 150); // Draw a line to x=300, y=150.
    ctx.stroke(); // Render the path
    draw_axes();
    start_drawing_data();
}

function draw_axes(){
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0,0.8*height);
    ctx.lineTo(width,0.8*height);
    ctx.moveTo(0.5*width,0);
    ctx.lineTo(0.5*width,height);
    ctx.stroke();
}

function start_drawing_data(){
    const id = setInterval(get_data,1000)
}
function get_data(){
    console.log('fetching...')
    fetch('/strokedata').then(function (response) {
          return response.json();
      }).then(function (data) {
            console.log(data)
            draw_data(data)
      });
}

function draw_data(data){
    ctx.beginPath();
    ctx.moveTo(width*(data[0]['y']/10+0.5),(1-data[0]['x'])*height)
    for (let i =1; i < parseInt(data['N']); i++){
        // console.log(data[i]['x'])
        // console.log(data[i]['y'])
        console.log((1-data[i]['x'])*height)
        console.log(1.0*width*(data[i]['y']/10+0.5))
        ctx.lineTo(width*(data[i]['y']/10+0.5),(1-data[i]['x'])*height)
    }
    ctx.stroke();
}