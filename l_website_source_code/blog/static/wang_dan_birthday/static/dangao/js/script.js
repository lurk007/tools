console.clear();

/* Play with these values! */
const PARTICLE_COUNT = 100;
const SAFE_DISTANCE = 130;
const INFECTED_DISTANCE = 15;
const INFECTION_RATE = 0.25;
const RECOVERY_TIME = 14000;
const STAY_AT_HOME = 0.1;

/* ---------------------------------- */

let particles = [];

const STATUSES = {
  HEALTHY: "HEALTHY",
  INFECTED: "INFECTED",
  RECOVERED: "RECOVERED"
};

const elBody = document.body;
const elCanvas = document.querySelector("#canvas");
const ctx = elCanvas.getContext("2d");

let width, height;

function resize() {
  width = elCanvas.width = elBody.clientWidth;
  height = elCanvas.height = elBody.clientHeight;
}
resize();
window.addEventListener("resize", resize);

/* ---------------------------------- */

class Particle {
  constructor() {
    this.x = Math.random() * width;
    this.y = Math.random() * height;
    this.radius = 3;
    this.color = "white";
    this.speed = Math.random() < STAY_AT_HOME ? 0 : 1;
    this.directionAngle = Math.floor(Math.random() * 360);
    this.vector = {
      x: Math.cos(this.directionAngle) * this.speed,
      y: Math.sin(this.directionAngle) * this.speed
    };
    this.status = STATUSES.HEALTHY;

    if (Math.random() < INFECTION_RATE) {
      this.infect();
    }
  }
  infect() {
    if (
      this.status === STATUSES.INFECTED ||
      this.status === STATUSES.RECOVERED
    ) {
      return;
    }

    this.color = "green";
    this.status = STATUSES.INFECTED;

    setTimeout(() => {
      this.recover();
    }, RECOVERY_TIME);
  }
  recover() {
    this.status = STATUSES.RECOVERED;
    this.color = "hotpink";
  }
  draw(drawCtx) {
    drawCtx.beginPath();
    drawCtx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    drawCtx.closePath();
    drawCtx.fillStyle = this.color;
    drawCtx.fill();
  }
  update() {
    this.checkBoundaries();
    this.x += this.vector.x;
    this.y += this.vector.y;
  }
  checkBoundaries() {
    if (this.x > width || this.x < 0) {
      this.vector.x *= -1;
      /* Ensure the dots are pushed inside */
      this.x = Math.max(0, Math.min(width, this.x));
    }
    if (this.y > height || this.y < 0) {
      this.vector.y *= -1;
      /* Ensure the dots are pushed inside */
      this.y = Math.max(0, Math.min(height, this.y));
    }
  }
}

/* ---------------------------------- */

function distance(x1, y1, x2, y2) {
  var dx = x1 - x2;
  var dy = y1 - y2;
  return Math.sqrt(dx * dx + dy * dy);
}

function linkParticles(particle, otherParticles, drawCtx) {
  for (const p of otherParticles) {
    const d = distance(particle.x, particle.y, p.x, p.y);

    if (d > SAFE_DISTANCE) {
      continue;
    }

    // Infect other particle!
    if (particle.status === STATUSES.INFECTED && d < INFECTED_DISTANCE) {
      p.infect();
    }

    const opacity = 0.8 - (d / SAFE_DISTANCE) * 0.8;
    drawCtx.lineWidth = 1;
    drawCtx.strokeStyle = particle.color; //rgba(255,255,255,${opacity})`;
    drawCtx.globalAlpha = opacity;
    drawCtx.beginPath();
    drawCtx.moveTo(particle.x, particle.y);
    drawCtx.lineTo(p.x, p.y);
    drawCtx.closePath();
    drawCtx.stroke();
    drawCtx.globalAlpha = 1;
  }
}

/* ---------------------------------- */

function render() {
  try {
    requestAnimationFrame(render);

    ctx.clearRect(0, 0, width, height);

    particles.forEach(particle => {
      particle.update();
      if (particle.status === STATUSES.INFECTED) {
        linkParticles(particle, particles, ctx);
      }
      particle.draw(ctx);
    });
  } catch (e) {
    throw e;
  }
}

render();

/* ---------------------------------- */

function reset() {
  particles = [];
  for (var i = 0; i < PARTICLE_COUNT; i++) {
    particles.push(new Particle());
  }
}
reset();

document.addEventListener("click", reset);