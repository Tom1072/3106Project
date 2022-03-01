import { useState } from "react";
import InfoBar from "./components/InfoBar/InfoBar";
import Board from "./components/Board/Board";
import Drawer from "./components/Drawer/Drawer";
import { Modal, Button } from "react-bootstrap";
import { initBoard, shuffleBoard } from "./utils/utilFunctions";
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

  const handleChoosePiece = (r, c) => {
    // const config = {
    //   method: "get",
    //   url: process.env.
    // }
    console.log(process.env.REACT_APP_SERVER_URL);
    setChoosingPiece(false);
  };

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
