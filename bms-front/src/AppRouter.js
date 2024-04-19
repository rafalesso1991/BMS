import React from "react";
import { Route, Routes } from "react-router-dom";
import RouterLayout from "./common/RouterLayout";
import Home from "./pages/Home";
import About from './pages/About';
import Users from './components/Users';
import Titles from './components/Titles';
import TitlesByName from './components/TitlesByName';
import TitlesByAuthor from './components/TitlesByAuthor';
import TitlesByGenre from './components/TitlesByGenre';
import TitlesByYear from './components/TitlesByYear';
import StockMarketData from './pages/StockMarketData';

export const AppRouter = () => {
    return (
    <Routes>
        <Route path="/" element={<RouterLayout />}>
            <Route path="*" element={<Home />} />
            <Route path="about" element={<About />} /> 
            <Route path="users" element={<Users />} /> 
            <Route path="titles" element={<Titles />} /> 
            <Route path="titles/by_name" element={<TitlesByName />} /> 
            <Route path="titles/by_author" element={<TitlesByAuthor />} /> 
            <Route path="titles/by_genre" element={<TitlesByGenre />} /> 
            <Route path="titles/by_year" element={<TitlesByYear />} /> 
            <Route path="stock" element={<StockMarketData />}/>
        </Route>
    </Routes>
    );
};
