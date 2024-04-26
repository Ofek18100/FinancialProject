// UpdateDBButton.js
import React, { useState, useEffect } from 'react';

function UpdateDBButton() {
  const [lastUpdateTime, setLastUpdateTime] = useState(null);

  // Fetch the last update time when the component mounts
  useEffect(() => {
    fetchLastUpdateTime();
  }, []);

  // Function to fetch the last update time from the server
  const fetchLastUpdateTime = () => {
    fetch('http://localhost:5555/last-update-time')
      .then(response => response.json())
      .then(data => setLastUpdateTime(data.lastUpdateTime))
      .catch(error => console.error('Error fetching last update time:', error));
  };

  // Function to handle updating the database
  const handleUpdateDB = () => {
    fetch('http://localhost:5555/update-db')
      .then(response => {
        if (response.ok) {
          // If update successful, fetch and display the new last update time
          fetchLastUpdateTime();
        } else {
          console.error('Error updating database:', response.statusText);
        }
      })
      .catch(error => console.error('Error updating database:', error));
  };

  return (
    <div className="update-db-button">
      <button onClick={handleUpdateDB}>Update DB</button>
      {lastUpdateTime && (
        <p>Last update: {new Date(lastUpdateTime).toLocaleString()}</p>
      )}
    </div>
  );
}

export default UpdateDBButton;
