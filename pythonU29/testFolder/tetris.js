// Simple Tetris implementation in vanilla JS
(function(){
  const canvas = document.getElementById('game');
  const ctx = canvas.getContext('2d');
  const scoreEl = document.getElementById('score');
  const levelEl = document.getElementById('level');
  const linesEl = document.getElementById('lines');
  const restartBtn = document.getElementById('restart');

  const COLS = 10;
  const ROWS = 20;
  const SCALE = canvas.width / COLS; // assume 300/10 = 30

  let arena = createMatrix(COLS, ROWS);
  let dropCounter = 0;
  let dropInterval = 1000;
  let lastTime = 0;
  let score = 0;
  let lines = 0;
  let level = 1;
  let paused = false;

  const colors = [null,'#FF5733','#FFCB2B','#3CE6C3','#4DA6FF','#B84DFF','#FF6EC7','#7DFF7D'];

  const tetrominoes = {
    'T': [[0,1,0],[1,1,1]],
    'O': [[2,2],[2,2]],
    'L': [[0,0,3],[3,3,3]],
    'J': [[4,0,0],[4,4,4]],
    'I': [[5,5,5,5]],
    'S': [[0,6,6],[6,6,0]],
    'Z': [[7,7,0],[0,7,7]]
  };

  function createMatrix(w,h){
    const m = [];
    for(let y=0;y<h;y++){
      m.push(new Array(w).fill(0));
    }
    return m;
  }

  function drawMatrix(matrix, offset){
    matrix.forEach((row,y)=>{
      row.forEach((value,x)=>{
        if(value){
          ctx.fillStyle = colors[value];
          ctx.fillRect((x+offset.x)*SCALE, (y+offset.y)*SCALE, SCALE-1, SCALE-1);
        }
      })
    })
  }

  function draw(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    // draw arena
    drawMatrix(arena, {x:0,y:0});
    // draw player
    drawMatrix(player.matrix, player.pos);
  }

  function merge(arena, player){
    player.matrix.forEach((row,y)=>{
      row.forEach((value,x)=>{
        if(value){
          arena[y+player.pos.y][x+player.pos.x] = value;
        }
      })
    })
  }

  function collide(arena, player){
    const m = player.matrix;
    for(let y=0;y<m.length;y++){
      for(let x=0;x<m[y].length;x++){
        if(m[y][x] !== 0 && (arena[y+player.pos.y] && arena[y+player.pos.y][x+player.pos.x]) !== 0){
          return true;
        }
      }
    }
    return false;
  }

  function rotate(matrix, dir){
    for(let y=0;y<matrix.length;y++){
      for(let x=0;x<y;x++){
        [matrix[x][y], matrix[y][x]] = [matrix[y][x], matrix[x][y]];
      }
    }
    if(dir>0) matrix.forEach(row => row.reverse()); else matrix.reverse();
  }

  function playerRotate(dir){
    const pos = player.pos.x;
    let offset = 1;
    rotate(player.matrix, dir);
    while(collide(arena, player)){
      player.pos.x += offset;
      offset = -(offset + (offset>0?1:-1));
      if(offset > player.matrix[0].length){
        rotate(player.matrix, -dir);
        player.pos.x = pos;
        return;
      }
    }
  }

  function playerDrop(){
    player.pos.y++;
    if(collide(arena, player)){
      player.pos.y--;
      merge(arena, player);
      sweepLines();
      playerReset();
      updateScore();
    }
    dropCounter = 0;
  }

  function playerMove(dir){
    player.pos.x += dir;
    if(collide(arena, player)) player.pos.x -= dir;
  }

  function sweepLines(){
    let rowCount = 1;
    outer: for(let y = arena.length -1; y>=0; --y){
      for(let x=0;x<arena[y].length;x++){
        if(arena[y][x] === 0){
          continue outer;
        }
      }
      const row = arena.splice(y,1)[0].fill(0);
      arena.unshift(row);
      y++;
      lines += 1;
      score += 10 * rowCount * level;
      rowCount *= 2;
    }
    // increase level every 10 lines
    const newLevel = Math.floor(lines/10)+1;
    if(newLevel !== level){
      level = newLevel;
      dropInterval = Math.max(100, 1000 - (level-1)*100);
    }
  }

  function playerReset(){
    const pieces = 'TJLOSZI';
    const type = pieces[Math.floor(Math.random()*pieces.length)];
    player.matrix = tetrominoes[type].map(r=>r.slice());
    player.pos.y = 0;
    player.pos.x = Math.floor((COLS - player.matrix[0].length)/2);
    if(collide(arena, player)){
      arena = createMatrix(COLS, ROWS);
      score = 0; lines = 0; level = 1; dropInterval = 1000; paused = false;
    }
  }

  function updateScore(){
    scoreEl.textContent = score;
    linesEl.textContent = lines;
    levelEl.textContent = level;
  }

  function update(time = 0){
    const deltaTime = time - lastTime;
    lastTime = time;
    if(!paused){
      dropCounter += deltaTime;
      if(dropCounter > dropInterval){
        playerDrop();
      }
    }
    draw();
    requestAnimationFrame(update);
  }

  const player = {
    pos: {x:0,y:0},
    matrix: null
  };

  document.addEventListener('keydown', event => {
    if(event.key === 'ArrowLeft'){ playerMove(-1); }
    else if(event.key === 'ArrowRight'){ playerMove(1); }
    else if(event.key === 'ArrowDown'){ playerDrop(); }
    else if(event.key === 'ArrowUp'){ playerRotate(1); }
    else if(event.code === 'Space'){ // hard drop
      while(!collide(arena, player)) player.pos.y++;
      player.pos.y--;
      merge(arena, player);
      sweepLines();
      playerReset();
      updateScore();
      dropCounter = 0;
      event.preventDefault();
    }
    else if(event.key === 'p' || event.key === 'P'){
      paused = !paused;
    }
  });

  restartBtn.addEventListener('click', () => {
    arena = createMatrix(COLS, ROWS);
    score = 0; lines = 0; level = 1; dropInterval = 1000; paused = false;
    playerReset();
    updateScore();
  })

  // initialize
  playerReset();
  updateScore();
  requestAnimationFrame(update);

})();
