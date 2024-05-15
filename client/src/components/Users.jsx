import React, { useState, useEffect } from 'react';
import useAuth from "../hooks/useAuth";
import axios from 'axios';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

const UsersData = () => {

  const { token } = useAuth();
  const [users, setUsers] = useState([]);

  useEffect(() => {
    let isMounted = true;
    const controller = new AbortController(); // Clase d JS q se utiliza con useEffect() p / cancelar solicitudes asincrónicas

    const getUsers = async () => {
      await axios.get('http://localhost:8000/users/', { headers: { 'Authorization': 'Bearer ' + token } })
      .then(response => {
        isMounted && setUsers(response.data);
      })
    }

    getUsers();

    return () => {
        isMounted = false;
        controller.abort();
    }
  }, [token]);

  return (

    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh' }}>
      <div>
        <TableContainer component={Paper}>
          <Table aria-label="users table">
            <TableHead>
              <TableRow>
                <TableCell style={{ backgroundColor: '#FF0000', color: '#FFFFFF', fontWeight: 'bold' }}>ID</TableCell>
                <TableCell style={{ backgroundColor: '#FF0000', color: '#FFFFFF', fontWeight: 'bold' }}>Username</TableCell>
                <TableCell style={{ backgroundColor: '#FF0000', color: '#FFFFFF', fontWeight: 'bold' }}>Email</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {users.map((user) => (
                <TableRow key={user.id}>
                  <TableCell>{user.id}</TableCell>
                  <TableCell>{user.username}</TableCell>
                  <TableCell>{user.email}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
    </div>

  );

};

export default UsersData;
