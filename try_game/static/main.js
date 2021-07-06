document.addEventListener("DOMContentLoaded", ( () => {

    var canvas = document.querySelector("#layer1");
    canvas.width = 480;
    canvas.height = 320;
    var ctx = canvas.getContext("2d");
    var game_loop = null;

    var background = document.querySelector("#layer2");
    background.width = 480;
    background.height = 320;
    var scn = background.getContext("2d");
    scn.beginPath();
    scn.rect(0, 0, canvas.width, canvas.height);
    scn.fillStyle = "#00000";
    scn.fill();
    scn.closePath();

    //Ball
    let Ball = {
        radious: 10,
        x: canvas.width/2,
        y: canvas.height-30,
        dx: 2,
        dy: -2,
        newBall: function() {
            return Ball
        },
        drawBall: function() {
            ctx.beginPath();
            ctx.arc(x, y, this.radious, 0, Math.PI*2);
            ctx.fillStyle = "#FFFFFF";
            ctx.fill();
            ctx.closePath();
        },    
        colided: function() {
            if(this.x + this.dx > canvas.width-this.radious || this.x + this.dx < this.radious) {
                this.dx = -this.dx;
            }
            if(this.y + this.dy > canvas.height-this.radious || this.y + this.dy < this.radious) {
                this.dy = -this.dx;
            }
        },
    }

    //Palyer
    let Player = {
        width: 10,
        height: 75,
        x: 0,
        y: canvas.height/2,
        moves: false,
        baseVeloc: 9,
        acc: 0.7,
        veloc: this.baseVeloc,
        newPlayer: function(x) {
            this.x = x;
            return Player
        },
        drawPlayer: function() {
            ctx.beginPath();
            ctx.rect(450, this.y, this.width, this.height);
            ctx.fillStyle = "#FFFFFF";
            ctx.fill();
            ctx.closePath();
        },
        colided: function(ball) {
            if(ball.x + ball.dx > canvas.width-this.x-ball.radious || ball.x + ball.dx < ball.radious-this.x) {
                if(ball.y > this.y && ball.y < this.y + this.height) {
                    ball.dx = -ball.dx;
                }
            }
        },
        exMove: function() {
            if(this.moves) {
                if(this.veloc < this.baseVeloc*2) {
                    this.veloc += this.acc;
                }
                if((this.moves === "ArrowUp") || (this.moves === "w") ? true : false) {
                    this.y -= this.veloc;
                    if(this.y < 0) {
                        this.y = 0;
                    }
                    this.moves = false;
                }
                if((this.moves === "ArrowDown") || (this.moves === "s") ? true : false) {
                    this.y += this.veloc;
                    if(this.y + this.height > canvas.height) {
                        this.y = canvas.height - this.height;
                    }
                    this.moves = false;
                }
                //console.log(veloc);
            } else {
                if(this.veloc > this.baseVeloc) {
                    this.veloc -= this.acc/3;
                }
            }
        }
    }

    /*
    var radious = 10;
    var x = canvas.width/2;
    var y = canvas.height-30;
    var dx = 2;
    var dy = -2;

    var width = 10;
    var height = 75;
    var x = 0;
    var y = canvas.height/2;
    var moves = false;
    const baseVeloc = 9;
    const acc = 0.7;
    var veloc = baseVeloc;
    */

    let ball = Ball.newBall();
    let p1 = Player.newPlayer(30);
    let p2 = Player.newPlayer(450);

    function update() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ball.drawBall();
        p1.drawPlayer();
        p2.drawPlayer();

        // Ball's colider
        ball.colided();

        //Player's colider
        p1.colided(ball);
        p2.colided(ball);

        p1.exMove();
        p2.exMove();

        x += ball.dx;
        y += ball.dy;
    }

    document.addEventListener("keydown", (ev) => {
        moves = (ev.key === "ArrowUp") || (ev.key === "ArrowDown") || (ev.key === "w") || (ev.key === "s") ? ev.key : false;
    });

    document.querySelector("#pause").onclick = function() {
        clearInterval(game_loop);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    };
    document.querySelector("#start").onclick = function() {
        game_loop = setInterval(update, 10);
    };

}));