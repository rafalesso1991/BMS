import ReactDOM from "react-dom/client";
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import StockMarketData from './StockMarketData';
import './App.css';
import About from './About'; // Your newly created component
import Layout from "./Layout";
import NoPage from "./NoPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route path="stock" element={<StockMarketData />}/>
          <Route path="about" element={<About />} /> 
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

export default App;


