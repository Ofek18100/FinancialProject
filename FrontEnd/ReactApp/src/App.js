import React, { useState } from 'react';
import './App.css';
import StockList from './components/StockList'; // Import the StockList component
import FilterBar from './components/FilterBar'; // Import the FilterBar component
import UpdateDBButton from './components/UpdateDBButton'; // Import the UpdateDBButton component

function App() {
  const [stockData, setStockData] = useState(null);
  const [numStocksToShow, setNumStocksToShow] = useState(10); // Initialize with default value

  const handleDownload = (tickerSymbol) => {
    let url = 'http://localhost:5001/as-json';
    if (tickerSymbol) {
      url = `http://localhost:5001/as-json/${tickerSymbol}`;
    }

    fetch(url)
      .then(response => response.json())
      .then(data => {
        console.log('Received data:', data); // Log received data
        // Transform the array of arrays into an array of objects
        const transformedData = data.map(item => ({
          symbol: item[0],
          change: item[1]
        }));
        setStockData(transformedData);
      })
      .catch(error => console.error('Error fetching data:', error));
  };

  return (
    <div className="App">
      <div className="update-db-button">
        <UpdateDBButton />
      </div>
      <h1>Stock Analytics</h1>
      <FilterBar onDownload={handleDownload} onStocksToShowChange={setNumStocksToShow} />
      {stockData && <StockList data={stockData} numStocksToShow={numStocksToShow} />} {/* Render StockList component */}
      {/* Render the table here if needed */}
    </div>
  );
}

export default App;
