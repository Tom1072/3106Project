import { useState } from "react";
import InfoBar from "./components/InfoBar/InfoBar";
import Board from "./components/Board/Board";
import Drawer from "./components/Drawer/Drawer";
import "./App.css";

function App() {
  const [gameStarted, setGameStarted] = useState(false);
  const [yourTurn, setYourTurn] = useState(true);

  const handleStartGame = (algorithm) => {
    console.log(`Starting with ${algorithm} algorithm`);
    setGameStarted(true);
  };

  const handleStopGame = () => {
    console.log("Game stopped");
    setGameStarted(false);
  };

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
      </div>
    </>
  );
}

export default App;
