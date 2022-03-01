import { useState } from "react";
import InfoBar from "./components/InfoBar/InfoBar";
import Board from "./components/Board/Board";
import Drawer from "./components/Drawer/Drawer";
import { Modal, Button } from "react-bootstrap";
import { initBoard, shuffleBoard } from "./utils/utilFunctions";
import { fetchAPI } from "./services/api";
import "./App.css";

function App() {
  const [gameStarted, setGameStarted] = useState(false);
  const [board, setBoard] = useState(initBoard());
  const [yourTurn, setYourTurn] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [youWin, setYouWin] = useState(true);
  const [choosingPiece, setChoosingPiece] = useState(true);

  const handleStartGame = (algorithm) => {
    console.log(`Starting with ${algorithm} algorithm`);
    setGameStarted(true);
  };

  const handleStopGame = () => {
    console.log("Game stopped");
    setGameStarted(false);
    setYourTurn(true);
    setBoard(initBoard());
    setChoosingPiece(true);
  };

  const handleChoosePiece = async (row, col) => {
    try {
      const data = await fetchAPI("/move", "GET", { row, col });
      setChoosingPiece(false);
      return data.availablePositions;
    } catch (err) {
      console.log(err);
    }
  };

  const handleMove = (row, col, prevRow, prevCol) => {
    const newBoard = board;
    newBoard[row][col] = newBoard[prevRow][prevCol];
    newBoard[prevRow][prevCol] = null;
  }

  const toggleModal = () => setShowModal(!showModal);

  return (
    <>
      <InfoBar />
      <div className="body">
        <Drawer
          handleStart={handleStartGame}
          handleStop={handleStopGame}
          started={gameStarted}
          yourTurn={yourTurn}
          shuffleBoard={() => setBoard(shuffleBoard(board))}
        />
        <Board
          board={board}
          switchTurn={() => setYourTurn(!yourTurn)}
          disabled={!(gameStarted && yourTurn)}
          choosingPiece={choosingPiece}
          choosePiece={handleChoosePiece}
          move={handleMove}
        />
        <Modal
          className={youWin ? "win-modal" : "lose-modal"}
          show={showModal}
          onHide={toggleModal}
        >
          <Modal.Header>{youWin ? "You win." : "You lose."}</Modal.Header>
          <Modal.Footer>
            <Button variant="light" onClick={toggleModal}>
              Close
            </Button>
          </Modal.Footer>
        </Modal>
      </div>
    </>
  );
}

export default App;
