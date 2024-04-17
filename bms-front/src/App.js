import ReactDOM from "react-dom/client";
import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import './App.css';
import { AppRouter } from "./AppRouter";

function App() {
  return (
    <BrowserRouter>
      <AppRouter />
    </BrowserRouter>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

export default App;
