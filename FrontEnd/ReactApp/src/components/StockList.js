// StockList.js
import React from 'react';

function StockList({ data, numStocksToShow }) {
  // Filter the data array based on the desired number of stocks to show
  const stocksToShow = data.slice(0, numStocksToShow);

  return (
    <div>
      <h2>Stock Analysis</h2>
      <table style={{ borderCollapse: 'collapse', width: '100%' }}>
        <thead>
          <tr>
            <th style={{ border: '1px solid #ddd', padding: '8px', backgroundColor: '#f2f2f2' }}>Ticker Symbol</th>
            <th style={{ border: '1px solid #ddd', padding: '8px', backgroundColor: '#f2f2f2' }}>Distance from SMA</th>
          </tr>
        </thead>
        <tbody>
          {stocksToShow.map(stock => (
            <tr key={stock.symbol}>
              <td style={{ border: '1px solid #ddd', padding: '8px' }}>{stock.symbol}</td>
              <td style={{ border: '1px solid #ddd', padding: '8px', color: stock.change > 0 ? 'green' : 'red' }}>{stock.change}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default StockList;
