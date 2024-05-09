import React, { useState } from 'react';
import useAuth from '../hooks/useAuth';
import { Button, Modal, TextField }  from '@mui/material';
import axios from 'axios';

export const LoginBtn = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const { auth, setAuth, setToken } = useAuth();

  const handleOpen = () => setIsOpen(true);
  const handleClose = () => setIsOpen(false);

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await axios({
        method: 'POST',
        url: 'http://localhost:8000/auth/token',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: new URLSearchParams({ 'username': username, 'password': password }).toString()
      });
      const accessToken = response?.data?.access_token;
      if (response.data.success) {
        setToken(response.data.access_token)
        setAuth({ username, password, accessToken });
        setUsername('');
        setPassword('');
        handleClose();
      } else {
        console.error('Invalid email or password');
      }
    } catch (error) {
      console.error(error);
    }

  };

  const handleLogout = () => {
    setAuth(false);
    localStorage.removeItem('authUser');
    setUsername('');
    setPassword('');
  };

  const buttonText = auth ? 'Logout' : 'Login';

  return (
    <>
      <Button variant = "contained" color = "primary" onClick = { auth ? handleLogout : handleOpen }>
        { buttonText }
      </Button>
      <Modal open = { isOpen } onClose = { handleClose }>
        <div style={{ display: 'flex', flexDirection: 'column', padding: 20 }}>
          <TextField
            type = "text"
            id = "username"
            label = "Username"
            autoComplete="off"
            variant = "outlined"
            value = { username }
            onChange = { (e) => setUsername(e.target.value) }
            required
          />
          <TextField
            type = "password"
            id = "password"
            label = "Password"
            variant = "outlined"
            value = { password }
            onChange = { (e) => setPassword(e.target.value) }
            required
          />
          <Button variant="contained" color="primary" onClick = { handleLogin }>
            Submit
          </Button>
        </div>
      </Modal>
    </>
  );
};

export default LoginBtn;
