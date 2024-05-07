import React, { useRef, useState, useEffect } from 'react';
import useAuth from '../hooks/useAuth';
import axios from 'axios';
import { Button, TextField }  from '@mui/material';

// COMPONENT
export const LoginBtn = () => {

  const { setAuth, setToken } = useAuth();
  const [user, setUser] = useState('');
  const [password, setPassword] = useState('');
  const [errMsg, setErrMsg] = useState('');

  const userRef = useRef();
  const errRef = useRef();


  useEffect(() => {
      userRef.current.focus();
  }, [])

  useEffect(() => {
    setErrMsg('');
  }, [user, password, ])


  useEffect(() => {

    const storedUser = localStorage.getItem('authUser');

    if (storedUser) {
      setAuth({ user });
    }

  }, []); // Empty Dependency Array to RUN ONLY on Initial Render

  const handleLogin = async (e) => {
    e.preventDefault();

    try {

      const response = await axios({
        method: 'POST',
        url: 'http://localhost:8000/auth/token',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: new URLSearchParams({ 'username': user, 'password': password }).toString()
      });
      const accessToken = response?.data?.access_token;
      if (response.data.success) {
        setToken(response.data.access_token)
        setAuth({ user, password, accessToken });
        setUser('');
        setPassword('');
        localStorage.setItem('authUser', user); // Store username for persistence
        setErrMsg('');
      } else {
        setErrMsg('Invalid username or password');
      }
    } catch (err) {
      if (!err?.response) {
          setErrMsg('No Server Response');
      } else if (err.response?.status === 400) {
          setErrMsg('Missing Username or Password');
      } else if (err.response?.status === 401) {
          setErrMsg('Unauthorized');
      } else {
          setErrMsg('Login Failed');
      }
      errRef.current.focus();
  }

  };

  /*const handleLogout = () => {
    setAuth(false);
    localStorage.removeItem('authUser');
    setUser('');
    setPassword('');
  };*/

  return (
    <div>

{/*

        <>
          <Button variant = "contained" color = "error" onClick = { handleLogout }>
            Logout
          </Button>
          <p>Welcome: { user }</p>
        </>

  */}

        <>
          <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
          <TextField
            type = "text"
            id = "username"
            ref = { userRef }
            label = "Username"
            autoComplete="off"
            variant = "outlined"
            value = { user }
            onChange = { (e) => setUser(e.target.value) }
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
          <Button variant="contained" onClick = { handleLogin }>
            Login
          </Button>
          {errMsg && <p style={{ color: 'red' }}>{errMsg}</p>}
        </>



    </div>
  );

};

// EXPORT
export default LoginBtn;