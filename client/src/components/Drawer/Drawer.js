import "./Drawer.css";
import { Algorithms } from "../../assets/constants";
import { Form, Button } from "react-bootstrap";
import { useState } from "react";

const Drawer = ({ handleStart, handleStop, started }) => {
  const [algorithm, setAlgorithm] = useState(Algorithms.MINIMAX);
  const [goFirst, setGoFirst] = useState(true);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (started) handleStop();
    else handleStart(algorithm);
  };

  return (
    <div className="drawer">
      <Form onSubmit={handleSubmit}>
        <Form.Group>
          <Form.Label>Search Algorithm</Form.Label>
          <Form.Select
            disabled={started}
            value={algorithm}
            onChange={(e) => setAlgorithm(e.target.value)}
          >
            <option value={Algorithms.MINIMAX}>Minimax Search</option>
            <option value={Algorithms.MONTE_CARLO}>Monte Carlo Search</option>
          </Form.Select>
        </Form.Group>

        <Form.Switch
          disabled={started}
          checked={goFirst}
          onChange={(e) => setGoFirst(e.target.checked)}
          label="You go first (White)"
        />

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
