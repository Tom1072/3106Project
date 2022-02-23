import { useState } from "react";
import { PIECES_SVG } from "../../assets/pieces";
import "./Board.css";

const initBoard = () => {
  const board = [];

  for (let i = 0; i < 8; i++) {
    if (i === 0) board.push(["br", "bkt", "bb", "bk", "bq", "bb", "bkt", "br"]);
    else if (i === 1) board.push(new Array(8).fill("bp"));
    else if (i === 6) board.push(new Array(8).fill("wp"));
    else if (i === 7)
      board.push(["wr", "wkt", "wb", "wk", "wq", "wb", "wkt", "wr"]);
    else board.push(new Array(8).fill(null));
  }

  return board;
};

const Board = ({ disabled }) => {
  const [board, setBoard] = useState(initBoard());

  const renderBoard = () => {
    return (
      <>
        {board.map((row, r_index) =>
          row.map((cell, c_index) => (
            <div
              key={`${r_index}${c_index}`}
              className={`board-cell ${(r_index + c_index) & 1 ? "" : "colored-cell"}`}
            >
              {PIECES_SVG[cell]}
            </div>
          ))
        )}
      </>
    );
  };

  return (
    <div className={`board-container ${disabled ? "disabled" : ""}`}>
      <div className="board">{renderBoard()}</div>;
    </div>
  );
};

export default Board;
