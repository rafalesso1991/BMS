import React from "react";
import { Route, Routes } from "react-router-dom";
import RouterLayout from "./common/RouterLayout";
import Home from "./pages/Home";
import Users from './components/Users';
import Books from './components/Books';
import MyBooks from './components/MyBooks';
import PrivateRoute from "./utils/PrivateRoute";

export const AppRouter = () => {

    return (
    <Routes>
        <Route path = "/" element = { <RouterLayout/> }>
            <Route path = "/" element = { <Home /> }/>
            <Route element = { <PrivateRoute /> }>
                <Route path = "users" element = { <Users /> }/>
            </Route>
            <Route element = { <PrivateRoute /> }>
                <Route path = "books" element = { <Books /> }/>
            </Route>
            <Route element = { <PrivateRoute /> }>
                <Route path = "myBooks" element = { <MyBooks /> }/>
            </Route>

        </Route>

    </Routes>

    );

};
