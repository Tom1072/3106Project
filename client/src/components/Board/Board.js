import { useState } from "react";
import { PIECES_SVG } from "../../assets/pieces";
import { Results } from "../../assets/constants";
import { fetchAPI } from "../../services/api";
import "./Board.css";

const Board = ({ board, setBoard, disabled, setYourTurn, choosePiece, endGame, move }) => {
  const [validMoves, setValidMoves] = useState([]);
  const [choosingPiece, setChoosingPiece] = useState(true);
  const [prevPosition, setPrevPosition] = useState(null);

  /**
   * Get the class name of a cell to add interaction according to the cell's piece.
   * @param {string | null} cell_piece Piece code to identify your own pieces
   * @param {number} row_index Index of the row
   * @param {number} column_index Index of the column
   * @returns {string} The class name
   */
  const getCellClass = (cell_piece, row_index, column_index, valid = false, capture = false) => {
    let className = `board-cell ${valid || (row_index + column_index) & 1 ? "" : "colored-cell"
      }`;

    if (choosingPiece && cell_piece && cell_piece.startsWith("w")) {
      className += " available-piece";
    } else if (valid) {
      if (capture) {
        className += " valid-move-capture"
      } else {
        className += " valid-move-no-capture";
      }
    }

    return className;
  };

  const handleChoosePiece = async (row, col, pieceCode) => {
    if (!pieceCode) return; // Change to next line after finishing AI
    // if (!pieceCode || pieceCode[0] !== "w") return;

    setPrevPosition({ row, col });
    const availableMoves = await choosePiece(row, col);
    setValidMoves(availableMoves);

    if (availableMoves.length > 0) {
      setChoosingPiece(false);
    } else {
      console.log("No available moves.");
    }
  };

  const handleMove = async (row, col, valid) => {
    try {
      setChoosingPiece(true);
      setValidMoves([]);

      if (!valid || !prevPosition) {
        return;
      }

      // console.log(`Attempt move at (${row}, ${col})`);
      setYourTurn(false);

      const yourMove = await fetchAPI("/move", "POST", {
        prev: prevPosition,
        next: { row, col },
      });
      setBoard(yourMove.board);

      if (yourMove.outcome) {
        endGame(Results[yourMove.outcome]);
        return;      
      }
      
      console.log("Bot AI is playing.")
      const aiMove = await fetchAPI("/ai_move", "GET");
      setBoard(aiMove.board);

      // TODO: enable this line after finishing AI
      // setYourTurn(!opponentMoves.is_black_turn);
    } catch (err) {
      console.log(err);
    }

    setYourTurn(true);
    setPrevPosition(null);
  };

  const isMoveValid = (row, col) => {
    return (
      validMoves.filter((move) => move.row === row && move.col === col).length >
      0
    );
  };

  const renderCell = (row, col, piece) => {
    const valid = isMoveValid(row, col);
    const capture = piece && piece.startsWith("b");

    return (
      <div
        key={`${row}${col}`}
        className={getCellClass(piece, row, col, valid, capture)}
        onClick={() =>
          choosingPiece
            ? handleChoosePiece(row, col, piece)
            : handleMove(row, col, valid)
        }
      >
        {PIECES_SVG[piece]}
      </div>
    );
  };

  /**
   * Render the board based on the board state.
   * @returns {[ReactComponent]} The generated cell list converted into React Component
   */
  const renderBoard = () => {
    return (
      <>
        {board.map((row, r_index) =>
          row.map((piece, c_index) => renderCell(r_index, c_index, piece))
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
