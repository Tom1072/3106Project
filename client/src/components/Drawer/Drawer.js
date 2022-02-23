import "./Drawer.css";
import { Algorithms } from "../../assets/constants";
import { Form, FloatingLabel, Button } from "react-bootstrap";
import { useState } from "react";

const Drawer = ({ handleStart, handleStop, started }) => {
  const [algorithm, setAlgorithm] = useState(Algorithms.MINIMAX);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (started)
      handleStop();
    else
      handleStart(algorithm);
  };

  return (
    <div className="drawer">
      <Form onSubmit={handleSubmit}>
        <FloatingLabel label="Search Algorithm">
          <Form.Select
            value={algorithm}
            onChange={(e) => setAlgorithm(e.target.value)}
          >
            <option value={Algorithms.MINIMAX}>Minimax Search</option>
            <option value={Algorithms.MONTE_CARLO}>Monte Carlo Search</option>
          </Form.Select>
        </FloatingLabel>
        <Button className="button" variant={started ? "danger" : "primary"} type="submit">
          {started ? "Stop Game" : "Start Game"}
        </Button>
      </Form>
    </div>
  );
};

export default Drawer;
