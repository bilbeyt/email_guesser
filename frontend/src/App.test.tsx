import "@testing-library/jest-dom";

import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import axios from "axios";
import MockAdapter from "axios-mock-adapter";
import React from "react";

import App from "./App";

process.env.REACT_APP_API_URL = "http://localhost:8000/api/email/guess";

describe("guesser", () => {
  it("successful email retrieval", async () => {
    render(<App />);
    const adapter = new MockAdapter(axios);
    const mockData = { data: { email: "jdoe@babbel.com" } };
    adapter
      .onGet(process.env.REACT_APP_API_URL + "?fullname=Jane+Doe&domain=babbel.com")
      .reply(200, mockData);

    userEvent.type(screen.getByPlaceholderText("Enter domain"), "babbel.com");
    userEvent.type(screen.getByPlaceholderText("Enter fullname"), "Jane Doe");
    userEvent.click(screen.getByText("Submit"));
    expect(screen.getByRole("status")).toBeVisible();
    setTimeout(() => {
      expect(
        screen.getByText("Email found for Jane Doe and babbel.com: jdoe@babbel.com"),
      ).toBeVisible();
    }, 1000);
  });

  it("failed email retrieval", async () => {
    render(<App />);
    const adapter = new MockAdapter(axios);
    const mockData = { data: { detail: "Email can not be guessed" } };
    adapter
      .onGet(process.env.REACT_APP_API_URL + "?fullname=Jane+Doe&domain=babbel.com")
      .reply(400, mockData);

    userEvent.type(screen.getByPlaceholderText("Enter domain"), "babbel.com");
    userEvent.type(screen.getByPlaceholderText("Enter fullname"), "Jane Doe");
    userEvent.click(screen.getByText("Submit"));
    expect(screen.getByRole("status")).toBeVisible();
    setTimeout(() => {
      expect(screen.getByText("Email can not be guessed")).toBeVisible();
    }, 1000);
  });
});
