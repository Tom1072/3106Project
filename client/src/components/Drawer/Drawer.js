import "./Drawer.css";
import { Algorithms } from "../../assets/constants";
import { Dropdown } from "react-bootstrap";

const Drawer = () => {
  const handleSelectAlgorithm = (selection) => {
    if (selection === Algorithms.MINIMAX)
      console.log("Selected Minimax Search");
    else if (selection === Algorithms.MONTE_CARLO)
      console.log("Selected Monte-Carlo Search");
  }

  return (
    <div className="drawer">
      <Dropdown show onSelect={handleSelectAlgorithm}>
        <Dropdown.Header>Search Algorithm</Dropdown.Header>
        <Dropdown.Item eventKey={Algorithms.MINIMAX}>Minimax Search</Dropdown.Item>
        <Dropdown.Item eventKey={Algorithms.MONTE_CARLO}>Monte Carlo Search</Dropdown.Item>
      </Dropdown>
    </div>
  );
};

export default Drawer;
