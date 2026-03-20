const API_KEY = "f79be76149db7ad5b3aabb097d0c7a7e";
const ZOOM = 2;

const map = L.map("map").setView([20, 0], ZOOM);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "© OpenStreetMap"
}).addTo(map);

// Create canvas overlay
const canvas = document.createElement("canvas");
const ctx = canvas.getContext("2d");
document.getElementById("map").appendChild(canvas);

function resizeCanvas() {
  canvas.width = map.getSize().x;
  canvas.height = map.getSize().y;
}
resizeCanvas();
map.on("resize", resizeCanvas);

// Fetch and recolor cloud tile
function drawClouds() {
  const img = new Image();
  img.crossOrigin = "anonymous";
  img.src = `https://tile.openweathermap.org/map/clouds_new/${ZOOM}/1/1.png?appid=${API_KEY}`;

  img.onload = () => {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

    let data = ctx.getImageData(0,0,canvas.width,canvas.height);
    let d = data.data;

    for (let i = 0; i < d.length; i += 4) {
      const intensity = d[i]; // cloud density
      if (intensity > 20) {
        d[i] = 255;       // Red
        d[i+1] = 215;     // Green
        d[i+2] = 0;       // Blue (YELLOW)
        d[i+3] = intensity; // alpha = density
      }
    }
    ctx.putImageData(data,0,0);
  };
}

// Animate cloud motion
let offset = 0;
setInterval(() => {
  offset = (offset + 5) % canvas.width;
  ctx.setTransform(1,0,0,1,offset,0);
  drawClouds();
}, 2000);

drawClouds();
