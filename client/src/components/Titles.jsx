import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

const TitlesData = () => {
  const [titlesData, setTitlesData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await axios.get('http://localhost:8000/titles/'); // Replace with your API endpoint and key 
      setTitlesData(response.data);
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
    return <div>Loading titles data...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (!titlesData) {
    return <div>No titles data found.</div>;
  }

  // Display fetched JSON data here (replace with your desired formatting)
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh' }}>
      <div>
        <TableContainer component={Paper}>
          <Table aria-label="titles table">
            <TableHead>
              <TableRow>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>ID</TableCell>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Name</TableCell>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Author</TableCell>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Genre</TableCell>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Year</TableCell>
                {/* Add more table headers for other fields if needed */}
              </TableRow>
            </TableHead>
            <TableBody>
              {titlesData.map((title) => (
                <TableRow key={title.id}>
                  <TableCell>{title.id}</TableCell>
                  <TableCell>{title.name}</TableCell>
                  <TableCell>{title.author}</TableCell>
                  <TableCell>{title.genre}</TableCell>
                  <TableCell>{title.year}</TableCell>
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

export default TitlesData;