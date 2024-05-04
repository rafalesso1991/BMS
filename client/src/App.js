import { BrowserRouter } from 'react-router-dom';
import { AppRouter } from "./AppRouter";
//import ReactDOM from "react-dom/client";
import React from 'react';
import './App.css';


export const AuthContext = React.createContext();


export function App() {

  const [token, setToken] = React.useState(null);
  //const [isAuthenticated, setIsAuthenticated] = useState(false);

  const value = {'token': token, 'setToken': setToken}
  console.log(token)
  return (
    <AuthContext.Provider value={value}>      
      <BrowserRouter>
        <AppRouter />
      </BrowserRouter>
    </AuthContext.Provider>
  );
}

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(<App />);

