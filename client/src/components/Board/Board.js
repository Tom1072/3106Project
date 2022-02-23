import { useState } from "react";
import { PIECES_SVG } from "../../assets/pieces";
import "./Board.css";

/**
 * Generate an initial chess board.
 * @returns {[Array<string | null>]}
 */
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
  const [choosingPiece, setChoosingPiece] = useState(true);

  /**
   * Get the class name of a cell to add interaction according to the cell's piece.
   * @param {string | null} cell_piece Piece code to identify your own pieces
   * @param {number} row_index Index of the row
   * @param {number} column_index Index of the column
   * @returns {string} The class name
   */
  const getCellClass = (cell_piece, row_index, column_index) => {
    let className = `board-cell ${
      (row_index + column_index) & 1 ? "" : "colored-cell"
    }`;

    if (choosingPiece && cell_piece && cell_piece.startsWith("w")) {
      className += " available-piece";
    }

    return className;
  };

  const handleChoosePiece = (pieceCode) => {
    if (!pieceCode)
      return;

    console.log(pieceCode + " chose!");
    setChoosingPiece(false);
  };

  const handleMove = (r, c, valid) => {
    if (!valid)
      return;

    console.log(`Move at (${r}, ${c})`);
    setChoosingPiece(true);
  };

  /**
   * Render the board based on the board state.
   * @returns {[ReactComponent]} The generated cell list converted into React Component
   */
  const renderBoard = () => {
    return (
      <>
        {board.map((row, r_index) =>
          row.map((cell, c_index) => (
            <div
              key={`${r_index}${c_index}`}
              className={getCellClass(cell, r_index, c_index)}
              onClick={() =>
                choosingPiece
                  ? handleChoosePiece(cell)
                  : handleMove(r_index, c_index, true)
              }
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
