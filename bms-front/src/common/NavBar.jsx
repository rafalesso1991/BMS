import React from "react";
import { AppBar, Toolbar, Button } from "@mui/material";
import { Link } from "react-router-dom";
import LoginButton from "../components/LoginButton";

const RouterLayout = () => {

    return (
      <div>
        <AppBar>
          <Toolbar>
            <Button component={Link} to="/" color="inherit">Home</Button>
            <Button component={Link} to="/about" color="inherit">About</Button>
            <Button component={Link} to="/users" color="inherit">Users</Button>
            <Button component={Link} to="/titles" color="inherit">Titles</Button>
            <Button component={Link} to="/titles/by_name" color="inherit">By Name</Button>
            <Button component={Link} to="/titles/by_author" color="inherit">By Author</Button>
            <Button component={Link} to="/titles/by_genre" color="inherit">By Genre</Button>
            <Button component={Link} to="/titles/by_year" color="inherit">By Year</Button>
            <Button component={Link} to="/stock" color="inherit">Stock</Button>
            <LoginButton />
            
          </Toolbar>
        </AppBar>

      </div>
    )
  };
  
  export default RouterLayout;