// FilterBar.js
import React, { useState } from 'react';

function FilterBar({ onDownload, onStocksToShowChange }) {
  const [tickerSymbol, setTickerSymbol] = useState('');

  const handleShow = () => {
    onDownload(tickerSymbol); // Call the onDownload function with ticker symbol
  };

  const handleNumStocksChange = (event) => {
    const numStocksToShow = parseInt(event.target.value); // Parse the selected value to integer
    onStocksToShowChange(numStocksToShow); // Call the onStocksToShowChange function with the selected number
  };

  return (
    <div className="filter-bar">
      <input
        type="text"
        placeholder="Enter ticker symbol"
        value={tickerSymbol}
        onChange={(e) => setTickerSymbol(e.target.value)}
      />
      <button onClick={handleShow}>Show</button>
      <select onChange={handleNumStocksChange}>
        <option value="10">Show 10 stocks</option>
        <option value="20">Show 20 stocks</option>
        <option value="50">Show 50 stocks</option>
      </select>
    </div>
  );
}

export default FilterBar;
