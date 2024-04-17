import React from "react";
import { Route, Routes } from "react-router-dom";
import RouterLayout from "./common/RouterLayout";
import Home from "./pages/Home";
import About from './pages/About';
import Marvel from './pages/Marvel';
import StockMarketData from './pages/StockMarketData';

export const AppRouter = () => {
    return (
    <Routes>
        <Route path="/" element={<RouterLayout />}>
            <Route path="*" element={<Home />} />
            <Route path="about" element={<About />} /> 
            <Route path="marvel" element={<Marvel />} /> 
            <Route path="stock" element={<StockMarketData />}/>
        </Route>
    </Routes>
    );
};
