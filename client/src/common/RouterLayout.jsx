import React from "react";
import NavBar from "./NavBar"
import { Outlet } from "react-router-dom";

const RouterLayout = () => {
    return (
      <>
        <header>
          <NavBar />
        </header>
        <main>
          <Outlet />
        </main>
      </>
    )
  };
  
  export default RouterLayout;