import { useState } from "react";
import { PIECES_SVG } from "../../assets/pieces";
import "./Board.css";

const Board = ({ board, disabled, switchTurn, choosingPiece, choosePiece }) => {
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

  const handleChoosePiece = (r, c, pieceCode) => {
    if (!pieceCode)
      return;

    console.log(pieceCode + " chose!");
    choosePiece(r, c);
  };

  const handleMove = (r, c, valid) => {
    if (!valid)
      return;

    console.log(`Move at (${r}, ${c})`);
    switchTurn();
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
                  ? handleChoosePiece(r_index, c_index, cell)
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
      <div className="board">{renderBoard()}</div>
    </div>
  );
};

export default Board;
