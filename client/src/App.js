import { BrowserRouter } from 'react-router-dom';
import { AppRouter } from "./AppRouter";
import { AuthProvider } from './context/AuthContext';
import React from 'react';
import './App.css';

export default function App() {

  const [token, setToken] = React.useState(null);

  const value = {'token': token, 'setToken': setToken}
  console.log(token)
  return (
    <BrowserRouter>
      <AuthProvider value={value}>      
        <AppRouter />
      </AuthProvider>
    </BrowserRouter>
  );
}
