import "./Drawer.css";
import { AlgorithmCodes } from "../../assets/constants";
import { Form, Button } from "react-bootstrap";
import { useState } from "react";
import { fetchAPI } from "../../services/api";

const Drawer = ({ handleStart, handleStop, started, turnPlayer1, player1, setPlayer1 }) => {
  const [player2, setPlayer2] = useState(AlgorithmCodes.minmax);

  const handleChangeAlgorithm1 = async (e) => {
    try {
      setPlayer1(e.target.value);
      if (e.target.value === "human") return;
      await fetchAPI("/algorithm/1", "PUT", { algorithm: e.target.value })
    } catch (err) {
      console.log(err)
    }
  }

  const handleChangeAlgorithm2 = async (e) => {
    try {
      setPlayer2(e.target.value);
      await fetchAPI("/algorithm/2", "PUT", { algorithm: e.target.value })
    } catch (err) {
      console.log(err)
    }
  }

  const handleSubmit = (e) => {
    e.preventDefault();

    if (started) handleStop();
    else handleStart(player1);
  };

  return (
    <div className="drawer">
      <Button variant={turnPlayer1 ? "success" : "danger"} className="turn-status" size="lg">
        {turnPlayer1 ? "Player 1's turn" : "Player 2's turn"}
      </Button>
      <Form onSubmit={handleSubmit}>
        <Form.Group>
          <Form.Label>Player 1</Form.Label>
          <Form.Select
            disabled={started}
            value={player1}
            onChange={handleChangeAlgorithm1}
          >
            {[["human", "Human"], ...Object.entries(AlgorithmCodes)].map(([code, algo_name], index) => 
              <option key={code} value={code}>{algo_name}</option>
            )}
          </Form.Select>

          <div className="vs-text">V.S.</div>

          <Form.Label>Player 2</Form.Label>
          <Form.Select
            disabled={started}
            value={player2}
            onChange={handleChangeAlgorithm2}
          >
            {Object.entries(AlgorithmCodes).map(([code, algo_name], index) => 
              <option key={code} value={code}>{algo_name}</option>
            )}
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
