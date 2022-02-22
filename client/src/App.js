import InfoBar from "./components/InfoBar/InfoBar";
import Board from "./components/Board/Board";
import Drawer from "./components/Drawer/Drawer";
import "./App.css"

function App() {
  return (
    <>
      <InfoBar />
      <div className="body">
        <Drawer />
        <Board />
      </div>
    </>
  );
}

export default App;
