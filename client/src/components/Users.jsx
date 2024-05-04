import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import {AuthContext} from '../App';

const UsersData = () => {
  const [usersData, setUsersData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const context = useContext(AuthContext);

  const fetchData = async () => {
    setIsLoading(true);
    setError(null);
  
    
    try {
      const response = await axios({
        method: 'GET',
        url: 'http://localhost:8000/users/',
        headers: {'Authorization': 'Bearer ' + context.token},
        });
      setUsersData(response.data);
    } catch (err) {
      setError(err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  if (isLoading) {
    return <div>Loading users data...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (!usersData) {
    return <div>No users data found.</div>;
  }

  // Display fetched JSON data here (replace with your desired formatting)
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
                {/* Add more table headers for other fields if needed */}
              </TableRow>
            </TableHead>
            <TableBody>
              {usersData.map((user) => (
                <TableRow key={user.id}>
                  <TableCell>{user.id}</TableCell>
                  <TableCell>{user.username}</TableCell>
                  <TableCell>{user.email}</TableCell>
                  {/* Add more table cells for other fields if needed */}
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