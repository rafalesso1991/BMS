import React, { useState } from 'react';
import useAuth from '../hooks/useAuth';
import { Button, Modal, TextField }  from '@mui/material';
import axios from 'axios';

const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Regular expression for email format

export const LoginBtn = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const { auth, setAuth, setToken } = useAuth();

  const handleOpen = () => setIsOpen(true);
  const handleClose = () => setIsOpen(false);

  const validateEmail = (email) => {
    setErrorMessage('');
    return EMAIL_REGEX.test(email);
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    if (!validateEmail(email)) {
      setErrorMessage('Invalid email format');
      return;
    }

    try {
      const response = await axios({
        method: 'POST',
        url: 'http://localhost:8000/auth/token',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: new URLSearchParams({ 'username': email, 'password': password }).toString()
      });
      const accessToken = response?.data?.access_token;
      if (response.data.success) {
        setToken(response.data.access_token)
        setAuth({ email, password, accessToken });
        setEmail('');
        setPassword('');
        handleClose();
      } else {
        console.error('Invalid email or password');
      }
    } catch (error) {
      console.error(error);
      setErrorMessage('Invalid email or password');
    }

  };

  const handleLogout = () => {
    setAuth(false);
    setEmail('');
    setPassword('');
  };

  const buttonText = auth ? 'Logout' : 'Login';

  return (
    <>
      <Button variant = "contained" color = "primary" onClick = { auth ? handleLogout : handleOpen }>
        { buttonText }
      </Button>
      <Modal open = { isOpen }
             onClose = { handleClose }
             style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            } }>
        <div style={{ display: 'flex', flexDirection: 'column', padding: 20 }}>
          <TextField
            type = "email"
            id = "email"
            label = "Email"
            autoComplete="off"
            variant = "outlined"
            value = { email }
            onChange = { (e) => setEmail(e.target.value) }
            required
          />
          {errorMessage && <p className="error-message">{errorMessage}</p>}
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
