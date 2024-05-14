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
          <Button component = { Link } to = "/" color = "inherit">Home</Button>
          {auth && (<Button component = { Link } to = "/users" color = "inherit">Users</Button>)}
          {auth && (<Button component = { Link } to = "/books" color = "inherit">Books</Button>)}
          {auth && (<Button component = { Link } to = "/myBooks" color = "inherit">My Books</Button>)}
          <LoginBtn />
          
        </Toolbar>

      </AppBar>

    </div>
  )
  };
  
  export default NavBar;