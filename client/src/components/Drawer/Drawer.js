import "./Drawer.css";
import { Algorithms } from "../../assets/constants";
import { Form, Button } from "react-bootstrap";
import { useState } from "react";

const Drawer = ({ handleStart, handleStop, started, yourTurn, shuffleBoard }) => {
  const [algorithm, setAlgorithm] = useState(Algorithms.MINIMAX);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (started) handleStop();
    else handleStart(algorithm);
  };

  return (
    <div className="drawer">
      <Button variant={yourTurn ? "success" : "danger"} className="turn-status" size="lg">
        {yourTurn ? "Your turn" : "Opponent's turn"}
      </Button>
      <Form onSubmit={handleSubmit}>
        <Form.Group>
          <Form.Label>Search Algorithm</Form.Label>
          <Form.Select
            disabled={started}
            value={algorithm}
            onChange={(e) => setAlgorithm(e.target.value)}
          >
            <option value={Algorithms.MINIMAX}>Minimax Search</option>
            <option value={Algorithms.MONTE_CARLO}>Monte-Carlo Search</option>
          </Form.Select>
        </Form.Group>

        <Form.Label>You go first with <b>white</b> pieces.</Form.Label>

        <Button
          className="button"
          variant={started ? "danger" : "primary"}
          type="submit"
        >
          {started ? "Stop Game" : "Start Game"}
        </Button>
      </Form>
      <Button
        className="button"
        variant="warning"
        onClick={shuffleBoard}
        disabled={started}
      >
        Shuffle Board
      </Button>
    </div>
  );
};

export default Drawer;
