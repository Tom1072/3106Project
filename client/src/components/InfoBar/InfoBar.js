import { Navbar } from "react-bootstrap";
import { BsGithub } from "react-icons/bs";
// import { Container } from 'react-dom';
import "./InfoBar.css";

const InfoBar = () => {
  return (
    <Navbar className="nav-container">
      <Navbar.Brand className="title" href="/">COMP 3106 Project</Navbar.Brand>
      <Navbar.Collapse className="justify-content-end">
        <a
          href="https://github.com/Tom1072/3106Project"
          target="_blank"
          rel="noreferrer"
        >
          <BsGithub className="icon" />
        </a>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default InfoBar;
