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
  const [turnPlayer1, setTurnPlayer1] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [outcome, setOutcome] = useState(null);
  const [player1, setPlayer1] = useState("human");

  useEffect(() => {
    const init = async () => {
      const response = await fetchAPI("/reset", "POST");
      setBoard(response.board);
      setTurnPlayer1(!response.is_black_turn) // You're a white piece
    };

    const AIAutoMove = async () => {
      console.log("Bot AI is playing.")
      const response = await fetchAPI(`/ai_move/${turnPlayer1 ? 1 : 2}`, "GET");
      if (typeof response !== "string") {
        setBoard(response.board);
        setTurnPlayer1(!turnPlayer1);
      }
    }

    if (!gameStarted) {
      init();
    } else if (gameStarted && player1 !== "human") {
      AIAutoMove();
    }
  }, [gameStarted, turnPlayer1]);

  const handleStartGame = (algorithm) => {
    console.log(`P1: ${player1} vs P2: ${algorithm}`);
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
          turnPlayer1={turnPlayer1}
          shuffleBoard={() => setBoard(shuffleBoard(board))}
          player1={player1}
          setPlayer1={setPlayer1}
        />
        <Board
          board={board}
          setBoard={setBoard}
          setTurnPlayer1={setTurnPlayer1}
          disabled={player1 !== "human" || !(gameStarted && turnPlayer1)}
          choosePiece={handleChoosePiece}
          endGame={handleEndGame}
          player1={player1}
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
