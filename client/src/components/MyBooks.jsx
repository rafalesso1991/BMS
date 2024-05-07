import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import useAuth from "../hooks/useAuth";

const BooksData = () => {

  const { token } = useAuth();
  const [books, setBooks] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;
    const controller = new AbortController();

    const getBooks = async () => {
      try {
        const response = await axios({
          method: 'GET',
          url: 'http://localhost:8000/books/my_books',
          headers: {'Authorization': 'Bearer ' + token}
        });
        setBooks(response.data);
        console.log(response.data);
        isMounted && setBooks(response.data);
      } catch (err) {
        setError(err);
      } finally {
        setIsLoading(false);
      }
    }

    getBooks();

    return () => {
      isMounted = false
      controller.abort();
    }
  }, []);

  if (isLoading) {
    return <div>Loading books data...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (!books) {
    return <div>No books data found.</div>;
  }

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
              {books.map((book) => (
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
