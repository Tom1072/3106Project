import InfoBar from "./components/InfoBar/InfoBar";
import Board from "./components/Board/Board";
import "./App.css"

function App() {
  return (
    <>
      <InfoBar />
      <div className="body">
        <Board />
      </div>
    </>
  );
}

export default App;
