import { useState } from "react";
import InfoBar from "./components/InfoBar/InfoBar";
import Board from "./components/Board/Board";
import Drawer from "./components/Drawer/Drawer";
import { Modal, Button } from "react-bootstrap";
import "./App.css";

function App() {
  const [gameStarted, setGameStarted] = useState(false);
  const [yourTurn, setYourTurn] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [youWin, setYouWin] = useState(true);

  const handleStartGame = (algorithm) => {
    console.log(`Starting with ${algorithm} algorithm`);
    setGameStarted(true);
  };

  const handleStopGame = () => {
    console.log("Game stopped");
    setGameStarted(false);
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
        />
        <Board
          switchTurn={() => setYourTurn(!yourTurn)}
          disabled={!(gameStarted && yourTurn)}
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
