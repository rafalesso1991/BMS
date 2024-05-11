import React from "react";
import { Route, Routes } from "react-router-dom";
import RouterLayout from "./common/RouterLayout";
import Home from "./pages/Home";
import Users from './components/Users';
import Books from './components/Books';
import MyBooks from './components/MyBooks';

export const AppRouter = () => {

    return (
    <Routes>
        <Route path = "/" element = { <RouterLayout/> }>
            <Route path = "*" element = { <Home /> }/>
            <Route path = "users" element = { <Users /> }/>
            <Route path = "books" element = { <Books /> }/>
            <Route path = "myBooks" element = { <MyBooks /> }/>
        </Route>

    </Routes>

    );

};
