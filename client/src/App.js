import { useState } from "react";
import InfoBar from "./components/InfoBar/InfoBar";
import Board from "./components/Board/Board";
import Drawer from "./components/Drawer/Drawer";
import { Modal, Button } from "react-bootstrap";
import { shuffleBoard } from "./utils/utilFunctions";
import { fetchAPI } from "./services/api";
import "./App.css";
import { Results } from "./assets/constants";
import { useEffect } from "react";

function App() {
  const [gameStarted, setGameStarted] = useState(false);
  const [board, setBoard] = useState([]);
  const [yourTurn, setYourTurn] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [outcome, setOutcome] = useState(null);

  useEffect(() => {
    const init = async () => {
      const response = await fetchAPI("/reset", "POST");
      setBoard(response.board);
      setYourTurn(!response.is_black_turn) // You're a white piece
    };

    init();
  }, [gameStarted]);

  const handleStartGame = (algorithm) => {
    console.log(`Starting with ${algorithm} algorithm`);
    setGameStarted(true);
  };

  const handleStopGame = () => {
    console.log("Game stopped");
    setGameStarted(false);
    // setYourTurn(true);
  };

  const handleChoosePiece = async (row, col) => {
    try {
      const data = await fetchAPI("/move", "GET", { row, col });
      return data.availablePositions;
    } catch (err) {
      console.log(err);
    }
  };

  // const handleMove = (row, col, prevRow, prevCol) => {
  //   const newBoard = board;
  //   newBoard[row][col] = newBoard[prevRow][prevCol];
  //   newBoard[prevRow][prevCol] = null;
  // }


  const toggleModal = () => setShowModal(!showModal);

  const getOutcomeText = () => {
    if (outcome === Results.WHITE)
      return "You win!";
    else if (outcome === Results.BLACK)
      return "You lose!";

    return "Tie!";
  }

  const getOutcomeClass = () => {
    if (outcome === Results.WHITE)
      return "win-modal";
    else if (outcome === Results.BLACK)
      return "lose-modal";

    return "tie-modal";
  }

  const handleEndGame = (winner) => {
    setOutcome(winner);
    setGameStarted(false);
    toggleModal();
  }

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
          setBoard={setBoard}
          setYourTurn={setYourTurn}
          disabled={!(gameStarted && yourTurn)}
          choosePiece={handleChoosePiece}
          endGame={handleEndGame}
          // move={handleMove}
        />
        <Modal
          className={getOutcomeClass()}
          show={showModal}
          onHide={toggleModal}
        >
          <Modal.Header>{getOutcomeText()}</Modal.Header>
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
