import React from "react";
import { AppBar, Toolbar, Button } from "@mui/material";
import useAuth from '../hooks/useAuth';
import { Link } from "react-router-dom";
import { LoginBtn }  from "../components/LoginBtn";

const NavBar = () => {

  const { auth } = useAuth();

  return (
    <div>
      <AppBar>
        <Toolbar>
          <Button component = { Link } to = "/home" color="inherit">Home</Button>
          <Button component = { Link } to = "/users" color="inherit">Users</Button>
          {auth && (
            <Button component = { Link } to = "/books" color="inherit">Books</Button>
          )}
          {auth && (
            <Button component = { Link } to = "/myBooks" color="inherit">MyBooks</Button>
          )}
          <Button component = { Link } to = "/stock" color="inherit">Stock</Button>
          <LoginBtn />
          
        </Toolbar>

      </AppBar>

    </div>
  )
  };
  
  export default NavBar;