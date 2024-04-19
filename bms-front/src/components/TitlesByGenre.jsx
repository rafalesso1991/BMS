import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { TextField, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
const TitlesByGenreData = () => {
  const [titlesData, setTitlesData] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
const fetchData = async () => {
    setIsLoading(true);
    setError(null);
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
try {
      const response = await axios.get('http://localhost:8000/titles/');
      setTitlesData(response.data);
    } catch (err) {
      setError(err);
    } finally {
      setIsLoading(false);
    }
  };
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
useEffect(() => {
    fetchData();
  }, []);
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
if (isLoading) {
    return <div>Loading titles data...</div>;
  }
  if (error) {
    return <div>Error: {error.message}</div>;
  }
  if (!titlesData) {
    return <div>No titles data found.</div>;
  }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  const filteredData = titlesData.filter((title) =>
    title.genre.toLowerCase().includes(searchTerm.toLowerCase())
  );
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh' }}>
      <div>
        <TextField
          label="Search by Genre"
          variant="outlined"
          value={searchTerm}
          onChange={handleSearchChange}
          style={{ marginBottom: '20px' }}
        />

        <TableContainer component={Paper}>
          <Table aria-label="titles table">

            <TableHead>
              <TableRow>
              <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>ID</TableCell>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Name</TableCell>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Author</TableCell>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Genre</TableCell>
                <TableCell style={{ backgroundColor: '#008000', color: '#FFFFFF', fontWeight: 'bold' }}>Year</TableCell>
              </TableRow>
            </TableHead>

            <TableBody>
              {filteredData.map((title) => (
                <TableRow key={title.id}>
                    <TableCell>{title.id}</TableCell>
                    <TableCell>{title.name}</TableCell>
                    <TableCell>{title.author}</TableCell>
                    <TableCell>{title.genre}</TableCell>
                    <TableCell>{title.year}</TableCell>
                </TableRow>
              ))}
            </TableBody>

          </Table>
        </TableContainer>

      </div>
    </div>
  );
};

export default TitlesByGenreData;
