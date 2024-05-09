import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import useAuth from "../hooks/useAuth";

const UsersData = () => {

  const { token } = useAuth();
  const [users, setUsers] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;
    const controller = new AbortController();

    const getUsers = async () => {
      try {
        const response = await axios({
          method: 'GET',
          url: 'http://localhost:8000/users/',
          headers: {'Authorization': 'Bearer ' + token},
          });
        setUsers(response.data);
        console.log(response.data);
        isMounted && setUsers(response.data);
      } catch (err) {
        setError(err);
      } finally {
        setIsLoading(false);
      }
    }

    getUsers();

    return () => {
        isMounted = false;
        controller.abort();
    }
  }, [token]);

  if (isLoading) {
    return <div>Loading users data...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (!users) {
    return <div>No users data found.</div>;
  }

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
