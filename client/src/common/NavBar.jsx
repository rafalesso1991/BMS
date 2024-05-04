import React from "react";
import { AppBar, Toolbar, Button } from "@mui/material";
import { Link } from "react-router-dom";
import { LoginButton }  from "../components/LoginButton";

const RouterLayout = () => {

    return (
      <div>
        <AppBar>
          <Toolbar>
            <Button component={Link} to="/home" color="inherit">Home</Button>
            <Button component={Link} to="/users" color="inherit">Users</Button>
            <Button component={Link} to="/books" color="inherit">Books</Button>
            <Button component={Link} to="/myBooks" color="inherit">MyBooks</Button>
            <Button component={Link} to="/stock" color="inherit">Stock</Button>
            <LoginButton />
            
          </Toolbar>
        </AppBar>

      </div>
    )
  };
  
  export default RouterLayout;