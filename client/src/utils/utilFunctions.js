/**
 * Generate an initial chess board.
 * @returns {[Array<string | null>]}
 */
export const initBoard = () => {
  const board = [];

  for (let i = 0; i < 8; i++) {
    if (i === 0) board.push(["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]);
    else if (i === 1) board.push(new Array(8).fill("wp"));
    else if (i === 6) board.push(new Array(8).fill("bp"));
    else if (i === 7)
      board.push(["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"]);
    else board.push(new Array(8).fill(null));
  }

  return board;
};

export const shuffleBoard = (board) => {
  var newBoard = board.map(function (row) {
    return row.slice();
  });

  for (var i = 0; i < newBoard.length; i++) {
    for (var j = 0; j < newBoard[i].length; j++) {
      var i1 = Math.floor(Math.random() * newBoard.length);
      var j1 = Math.floor(Math.random() * newBoard.length);

      var temp = newBoard[i][j];
      newBoard[i][j] = newBoard[i1][j1];
      newBoard[i1][j1] = temp;
    }
  }
  return newBoard;
};
