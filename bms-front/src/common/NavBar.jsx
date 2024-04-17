import React from "react";
import { AppBar, Toolbar, Button } from "@mui/material";
import { Link } from "react-router-dom";

const RouterLayout = () => {
    return (
      <div>
        <AppBar>
          <Toolbar>
            <Button component={Link} to="/" color="inherit">Home</Button>
            <Button component={Link} to="/about" color="inherit">About</Button>
            <Button component={Link} to="/marvel" color="inherit">Marvel</Button>
            <Button component={Link} to="/stock" color="inherit">Stock</Button>
          </Toolbar>
        </AppBar>

      </div>
    )
  };
  
  export default RouterLayout;