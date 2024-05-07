import React, { useContext, useState } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle, TextField} from '@mui/material';
import axios from 'axios';
import useAuth from "../hooks/useAuth";
import { AuthProvider } from './context/AuthContext';

//const AuthContext = createContext();

export const LoginButton = () => {

  const auth = useAuth();
  const [open, setOpen] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);


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
        //setIsAuthenticated(true);
        auth.setToken(response.data.access_token)

      } else {
        console.error('Login failed:', response);
      }
    } catch (error) {
      console.error('Login error:', error);
    }
  };

  const handleClickOpen = () => setOpen(true);
  const handleClose = () => {
    setOpen(false);
    setError(null); // Clear error on close
  };


  const handleLogin = async () => {
    setError(null); // Clear error before attempting login
    try {
      login(username, password)
    } catch (error) {
      console.error('Login error:', error);
      setError('ACA SE CORRE EL ERROR');
    }
  };

  if (false) {
    return <Button variant="contained" color="primary">Profile</Button>;
  }

  return (
    <AuthProvider value="hola">
      <Button variant="contained" color="primary" onClick={handleClickOpen}>
        Login
      </Button>
      <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
        <DialogTitle id="form-dialog-title">Login</DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            label="Username"
            type="text"
            fullWidth
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <TextField
            margin="dense"
            label="Password"
            type="password"
            fullWidth
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          {error && <p style={{ color: 'red' }}>{error}</p>}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleLogin} color="primary">
            Login
          </Button>
        </DialogActions>
      </Dialog>
    </AuthProvider>
  );
};

export default LoginButton;