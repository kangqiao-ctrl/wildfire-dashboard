import React from 'react';
import MapView from './components/MapView';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="app-header">
        <h1>Wildfire Alert Dashboard</h1>
        <p>Real-time monitoring of potential wildfire threats</p>
      </header>
      <main className="app-main">
        <MapView />
      </main>
    </div>
  );
}

export default App;
