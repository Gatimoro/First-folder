let lastplayer= 'red';
let board={
    a:{1:null,2:null,3:null},
    b:{1:null,2:null,3:null},
    c:{1:null,2:null,3:null}
}
let win='';
const check=function(tile){
    if (board[ tile[0]][1]===board[tile[0]][2] && board[tile[0]][1]===board[tile[0]][3]){
        win='column'
        return true;
    }else if(board['a'][tile[1]]===board['b'][tile[1]]&&board['b'][tile[1]]===board['c'][tile[1]]){
        win='row'
        return true
    } 
    if (board['b'][2]!=null){
        if(board['a'][1]==board['c'][3]&&board['a'][1]==board['b'][2] || board['a'][3]==board['c'][1]&&board['a'][3]==board['b'][2]){
            return true;
        }
    }
}
const place=function(tile){
    document.getElementById(tile).disabled = true;
    if(lastplayer=='red'){
        document.getElementById(tile).style.backgroundColor = 'blue';
        lastplayer='blue';
    }else{
        document.getElementById(tile).style.backgroundColor = 'red';
        lastplayer='red';
    }
    board[tile[0]][tile[1]]=lastplayer
    let lettas=['bruh','a','b','c'];
    if (check(tile)){
        for(numbah=1;numbah<4;numbah++){
            if(win=='row'){
                    document.getElementById(lettas[numbah]+tile[1]).style.backgroundColor = 'gold';
            }
            else if(win=='column'){
                    document.getElementById(tile[0]+numbah).style.backgroundColor = 'gold';
            }
            else if(board['a'][1]==board['c'][3]){
                    document.getElementById(lettas[numbah]+numbah).style.backgroundColor = 'gold';
            }
            else{
                    document.getElementById(lettas[4-numbah]+numbah).style.backgroundColor = 'gold';
            }
        }
    }
}