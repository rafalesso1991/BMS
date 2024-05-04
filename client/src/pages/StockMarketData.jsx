import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StockMarketData = () => {
  const [stockData, setStockData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await axios.get('https://rickandmortyapi.com/api/character/176'); // Replace with your API endpoint and key
      setStockData(response.data);
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
    return <div>Loading stock data...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (!stockData) {
    return <div>No stock data found.</div>;
  }

  // Display fetched JSON data here (replace with your desired formatting)
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh' }}>
      <div>
        <h2>Jerry</h2>
        <pre>{JSON.stringify(stockData, null, 2)}</pre>
      </div>
    </div>
  );
};

export default StockMarketData;