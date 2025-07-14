import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [spotPrice, setSpotPrice] = useState(100);
  const [strikePrice, setStrikePrice] = useState(100);
  const [volatility, setVolatility] = useState(0.2);
  const [riskFreeRate, setRiskFreeRate] = useState(0.05);
  const [maturityDate, setMaturityDate] = useState('2025-12-31');
  const [optionType, setOptionType] = useState('call');
  const [price, setPrice] = useState(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post('/hedge/price-option', {
        spot_price: spotPrice,
        strike_price: strikePrice,
        volatility: volatility,
        risk_free_rate: riskFreeRate,
        maturity_date: maturityDate,
        option_type: optionType,
      });
      setPrice(response.data.price);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Financial Hedging System</h1>
      </header>
      <div className="container">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Spot Price</label>
            <input
              type="number"
              value={spotPrice}
              onChange={(e) => setSpotPrice(parseFloat(e.target.value))}
            />
          </div>
          <div className="form-group">
            <label>Strike Price</label>
            <input
              type="number"
              value={strikePrice}
              onChange={(e) => setStrikePrice(parseFloat(e.target.value))}
            />
          </div>
          <div className="form-group">
            <label>Volatility</label>
            <input
              type="number"
              step="0.01"
              value={volatility}
              onChange={(e) => setVolatility(parseFloat(e.target.value))}
            />
          </div>
          <div className="form-group">
            <label>Risk-Free Rate</label>
            <input
              type="number"
              step="0.01"
              value={riskFreeRate}
              onChange={(e) => setRiskFreeRate(parseFloat(e.target.value))}
            />
          </div>
          <div className="form-group">
            <label>Maturity Date</label>
            <input
              type="date"
              value={maturityDate}
              onChange={(e) => setMaturityDate(e.target.value)}
            />
          </div>
          <div className="form-group">
            <label>Option Type</label>
            <select
              value={optionType}
              onChange={(e) => setOptionType(e.target.value)}
            >
              <option value="call">Call</option>
              <option value="put">Put</option>
            </select>
          </div>
          <button type="submit">Price Option</button>
        </form>
        {price && (
          <div className="result">
            <h2>Option Price: {price}</h2>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
