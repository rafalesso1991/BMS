import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

const AuthContext = createContext({
  user: null,
  setUser: () => {},
  isAuthenticated: false,
  setIsAuthenticated: () => {},
  token: null,
  setToken: (a) => a,
  login: () => {},
  logout: () => {},
});

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [token, setToken] = useState('token')

  useEffect(  () => {
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
      setIsAuthenticated(true);
    }
  }, []);

  const login = async (username, password) => {
    try {
      const response = await axios({
        method: 'POST',
        url: 'http://localhost:8000/auth/token',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: new URLSearchParams({ 'username': username, 'password': password }).toString()
    });
      if (response.data.success) {
        console.log(response)
        setUser(response.data.user);
        setIsAuthenticated(true);
        setToken(response.data.access_token)
        localStorage.setItem('myToken', response.data.access_token);
        console.log("SE GUARDO EL TOKEN?: " + token)
        console.log("SE GUARDO EL USER?: " + user)

        localStorage.setItem('user', JSON.stringify(response.data.user));
      } else {
        console.error('Login failed:', response);
      }
    } catch (error) {
      console.error('Login error:', error);
    }
  };

  const logout = () => {
    setUser(null);
    setIsAuthenticated(false);
    localStorage.removeItem('user');
  };

  const value = {
    user,
    setUser,
    isAuthenticated,
    setIsAuthenticated,
    login,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export { AuthContext, AuthProvider };