import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import {AuthContext} from '../App';

const BooksData = () => {
  const [booksData, setBooksData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const context = useContext(AuthContext);

  const fetchData = async () => {
    setIsLoading(true);
    setError(null);


    try {
      const response = await axios({
        method: 'GET',
        url: 'http://localhost:8000/books/',
        headers: {'Authorization': 'Bearer ' + context.token}
      });
      setBooksData(response.data);
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
    return <div>Loading books data...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (!booksData) {
    return <div>No books data found.</div>;
  }

  // Display fetched JSON data here (replace with your desired formatting)
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh' }}>
      <div>
        <TableContainer component={Paper}>
          <Table aria-label="books table">
            <TableHead>
              <TableRow>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>ID</TableCell>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Title</TableCell>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Description</TableCell>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>owner</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {booksData.map((book) => (
                <TableRow key={book.id}>
                  <TableCell>{book.id}</TableCell>
                  <TableCell>{book.title}</TableCell>
                  <TableCell>{book.description}</TableCell>
                  <TableCell>{book.owner}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
    </div>
  );
};

export default BooksData;