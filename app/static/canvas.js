const canvas = document.getElementById('canvas');
const width = canvas.width
const height = canvas.height
const ctx = canvas.getContext('2d');
let dataindex = 0;

function animate__c() {
    start_drawing_data();
}

function draw_axes(){
    ctx.clearRect(0,0,width, height)
    ctx.lineWidth = 1;
    ctx.strokeStyle = 'black';
    ctx.beginPath();
    ctx.moveTo(0,0.8*height);
    ctx.lineTo(width,0.8*height);
    ctx.moveTo(0.5*width,0);
    ctx.lineTo(0.5*width,height);
    ctx.stroke();
}

function start_drawing_data(){
    const id = setInterval(get_data,50)
}
function get_data(){
    console.log('fetching...')
    fetch('/strokedata/' + dataindex).then(function (response) {
          return response.json();
      }).then(function (data) {
            draw_data(data)
      });
    dataindex ++;
}

function draw_data(data){
    draw_axes();
    ctx.lineWidth = 3;
    ctx.strokeStyle = 'red';
    ctx.beginPath();
    const squish = 2;
    ctx.moveTo(width*(data[0]['y']/squish+0.5),(1-data[0]['x'])*height)
    for (let i =1; i < parseInt(data['N']); i++){
        // console.log(data[i]['x'])
        // console.log(data[i]['y'])
        ctx.lineTo(width*(data[i]['y']/squish+0.5),(1-data[i]['x'])*height)
    }
    ctx.stroke();
}