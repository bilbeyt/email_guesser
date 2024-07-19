import axios from "axios";
import React, { useState } from "react";
import Alert from "react-bootstrap/Alert";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Navbar from "react-bootstrap/Navbar";
import Spinner from "react-bootstrap/Spinner";

interface EmailResponse {
  email: string;
}

function App() {
  const [fullName, setFullName] = useState("");
  const [domain, setDomain] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const [email, setEmail] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const url = new URL(process.env.REACT_APP_API_URL || "");
    const params = { fullname: fullName, domain: domain };
    url.search = new URLSearchParams(params).toString();
    setIsLoading(true);
    setEmail("");
    setError("");
    axios
      .get(url.toString(), {
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      })
      .then(async (response) => {
        setEmail((response.data as EmailResponse).email);
        setIsLoading(false);
      })
      .catch((error) => {
        if (error.response) {
          setError(error.response.data.detail);
          setIsLoading(false);
        }
      });
  };

  const form = (
    <Form onSubmit={(e) => handleSubmit(e)}>
      <Form.Group className="mb-3">
        <Form.Label>Full name</Form.Label>
        <Form.Control
          id="fullname-input"
          value={fullName}
          type="text"
          placeholder="Enter fullname"
          onChange={(e) => {
            setFullName(e.currentTarget.value);
            setError("");
            setEmail("");
          }}
        />
      </Form.Group>

      <Form.Group className="mb-3">
        <Form.Label>Domain</Form.Label>
        <Form.Control
          id="domain-input"
          type="text"
          value={domain}
          placeholder="Enter domain"
          onChange={(e) => {
            setDomain(e.currentTarget.value);
            setError("");
            setEmail("");
          }}
        />
      </Form.Group>
      <Button className="mb-3" id="submit-btn" variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );

  const spinner = (
    <Spinner animation="border" role="status" id="spinner">
      <span className="visually-hidden">Loading...</span>
    </Spinner>
  );

  let result = (
    <Alert key="success" variant="success" id="success-alert">
      Email found for {fullName} and {domain}: {email}
    </Alert>
  );

  if (error) {
    result = (
      <Alert key="danger" variant="danger" id="error-alert">
        {error}
      </Alert>
    );
  }

  return (
    <>
      <Navbar className="bg-body-tertiary mb-3">
        <Container>
          <Navbar.Brand>Email Guesser</Navbar.Brand>
        </Container>
      </Navbar>
      <Container className="mb-3">
        <h1 className="mb-3">Welcome to Email Guesser!</h1>
        <Card>
          <Card.Body>
            {isLoading ? spinner : form}
            {email || error ? result : ""}
          </Card.Body>
        </Card>
      </Container>
    </>
  );
}

export default App;
