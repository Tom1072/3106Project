import "./Drawer.css";
import { Algorithms } from "../../assets/constants";
import { Form, Button } from "react-bootstrap";
import { useState } from "react";
import { fetchAPI } from "../../services/api";

const Drawer = ({ handleStart, handleStop, started, yourTurn }) => {
  const [algorithm, setAlgorithm] = useState(Algorithms.MINIMAX);

  const handleChangeAlgorithm = async (e) => {
    try {
      setAlgorithm(e.target.value);
      await fetchAPI("/algorithm", "PUT", { algorithm: e.target.value })
    } catch (err) {
      console.log(err)
    }
  }

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
            onChange={handleChangeAlgorithm}
          >
            <option value={Algorithms.MINIMAX}>Minimax Search</option>
            <option value={Algorithms.ALPHA_BETA_PRUNING}>Alpha-Beta Pruning Search</option>
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
    </div>
  );
};

export default Drawer;
