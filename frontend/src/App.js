import React, { useState, useEffect } from "react";
import "./App.css";
import Papa from "papaparse";

function App() {
  const [exch, setExch] = useState("");
  const [histBackFill, setHistBackFill] = useState(false);
  const [timeFrame, setTimeFrame] = useState(1);
  const [timeFrameUnits, setTimeFrameUnits] = useState("min");
  const [fromDate, setFromDate] = useState("");
  const [toDate, setToDate] = useState("");
  const [indicesDate, setIndicesDate] = useState(1);
  const [save, setSave] = useState(false);
  const [load, setLoad] = useState(false);
  const [stopOrders, setStopOrders] = useState(false);
  const [startOrders, setStartOrders] = useState(false);
  const [amiSpd, setAmiSpd] = useState(0.5);
  const [startRTD, setStartRTD] = useState(false);
  const [stopRtd, setStopRtd] = useState(false);
  const [clearAll, setClearAll] = useState(false);
  const [scripts, setScripts] = useState("NIFTY");
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [selectedExchanges, setSelectedExchanges] = useState([]);
  const [exchanges, setExchanges] = useState([]); // State to hold exchanges
  const [nseTokens, setNseTokens] = useState([]); // State to hold NSEtoken data

  const URL = "https://dhanui30-backend.onrender.com";

  useEffect(() => {
    const fetchCSV = async () => {
      try {
        // const response = await fetch("/merged_file.csv"); // Adjust path as needed
        const response = await fetch(`${URL}/merged_file.csv`);

        const csvText = await response.text();

        Papa.parse(csvText, {
          header: true,
          skipEmptyLines: true,
          complete: (result) => {
            const symbols = result.data.map((row) => ({
              symbol: row.Symbol.trim(),
              tradingSymbol: row.Trading_Symbol.trim(),
              token: row.Token.trim(),
              exchange_segment: row.Exchange_Segment.trim(),
            }));
            setExchanges(symbols); // Set exchanges with symbol, trading symbol, and token
          },
        });
      } catch (error) {
        console.error("Error loading CSV:", error);
      }
    };

    fetchCSV();
  }, []);

  const handleLoadAmi = async () => {
    try {
      const response = await fetch(`${URL}/updateAmiBrokerData`, {
        method: "POST",
      });

      if (response.ok) {
        alert("AmiBroker data updated successfully!");
      } else {
        const errorMessage = await response.text();
        alert(`Failed to update AmiBroker data: ${errorMessage}`);
      }
    } catch (error) {
      console.error("Error updating AmiBroker data:", error);
      alert(
        "An error occurred while updating AmiBroker data. Please try again."
      );
    }
  };

  const handleSearch = (e) => {
    setSearchQuery(e.target.value);
    const filteredExchanges = exchanges.filter(
      (exchange) =>
        exchange.symbol.toLowerCase().includes(e.target.value.toLowerCase()) ||
        exchange.tradingSymbol
          .toLowerCase()
          .includes(e.target.value.toLowerCase())
    );
    setSearchResults(filteredExchanges);
  };

  // Handle selection of an exchange symbol
  const handleSelectExchange = (exchange) => {
    if (!selectedExchanges.some((e) => e.symbol === exchange.symbol)) {
      setSelectedExchanges([...selectedExchanges, exchange]);
    }
    setSearchQuery(""); // Clear search input
    setSearchResults([]); // Clear search suggestions
  };

  // Remove an exchange from the selected list
  const removeExchange = (exchangeSymbol) => {
    setSelectedExchanges(
      selectedExchanges.filter((exchange) => exchange.symbol !== exchangeSymbol)
    );
  };

  const toggleHistBackFill = () => {
    setHistBackFill(!histBackFill);
  };

  const handleStartRTD = async () => {
    try {
      // Send a request to the backend to start RTD
      const response = await fetch(`${URL}/startRTD`, {
        method: "POST",
      });

      if (response.ok) {
        alert("RTD started successfully!");
      } else {
        const errorMessage = await response.text();
        alert(`Failed to start RTD: ${errorMessage}`);
      }
    } catch (error) {
      console.error("Error starting RTD:", error);
      alert("Error starting RTD");
    }
  };

  const handleSaveCSV = async () => {
    const dataToSave = selectedExchanges.map((exchange) => ({
      Symbol: exchange.symbol,
      Token: exchange.token,
      Exchange_Segment: exchange.exchange_segment,
    }));

    const csv = Papa.unparse(dataToSave); // Convert the data to CSV format

    // Create a Blob from the CSV data
    const blob = new Blob([csv], { type: "text/csv" });
    const formData = new FormData();
    formData.append("file", blob, "selected_symbols.csv"); // Append the file to the form data

    try {
      // Send the file to the backend
      const response = await fetch(`${URL}/upload`, {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        alert("File uploaded successfully");
      } else {
        alert("Failed to upload file");
      }
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("Error uploading file");
    }
  };

  return (
    <div className="app-container">
      <h1 className="app-title">MINT MASTER</h1>

      <div className="grid-container">
        {/* Exchange Search Input */}
        <div className="grid-item">
          <label>Exchange:</label>
          <input
            type="text"
            value={searchQuery}
            onChange={handleSearch}
            placeholder="Search for an exchange"
            className="search-input"
          />
          {searchResults.length > 0 && (
            <div className="search-results">
              {searchResults.map((result, index) => (
                <div
                  key={index}
                  className="search-item"
                  onClick={() => handleSelectExchange(result)}
                >
                  {result.symbol} - {result.tradingSymbol}
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Selected Symbols */}
        <div className="grid-item selected-box">
          <h3>Selected Symbols</h3>
          {selectedExchanges.length === 0 ? (
            <p>No symbols selected</p>
          ) : (
            <ul>
              {selectedExchanges.map((exchange, index) => (
                <li key={index} onClick={() => removeExchange(exchange.symbol)}>
                  {exchange.symbol} - {exchange.tradingSymbol} - Token:{" "}
                  {exchange.token} - {exchange.exchange_segment}
                  <span className="remove-btn">x</span>{" "}
                  {/* Show Token with the selected symbol */}
                </li>
              ))}
            </ul>
          )}
        </div>

        {/* Hist-Backfill Toggle */}
        <div className="grid-item">
          <button
            className={`toggle-button ${histBackFill ? "active" : ""}`}
            onClick={toggleHistBackFill}
          >
            Hist-Backfill
          </button>
        </div>

        {/* Buttons */}
        <div className="grid-item">
          <button
            className={`action-button ${save ? "active" : ""}`}
            onClick={handleSaveCSV} // Trigger save CSV
          >
            Save
          </button>
        </div>

        {/* Time Frame */}
        <div className="grid-item">
          <label>Time Frame:</label>
          <input
            type="number"
            value={timeFrame}
            onChange={(e) => setTimeFrame(e.target.value)}
          />
          <select
            value={timeFrameUnits}
            onChange={(e) => setTimeFrameUnits(e.target.value)}
          >
            <option value="min">min</option>
            <option value="hr">hr</option>
          </select>
        </div>

        {/* Date Range */}
        <div className="grid-item">
          <label>From Date:</label>
          <input
            type="date"
            value={fromDate}
            onChange={(e) => setFromDate(e.target.value)}
          />
        </div>

        <div className="grid-item">
          <label>To Date:</label>
          <input
            type="date"
            value={toDate}
            onChange={(e) => setToDate(e.target.value)}
          />
        </div>

        {/* Indices Date */}
        <div className="grid-item">
          <label>Indices Date:</label>
          <input
            type="number"
            value={indicesDate}
            onChange={(e) => setIndicesDate(e.target.value)}
          />
        </div>

        {/* Buttons */}
        <div className="grid-item">
          <button
            className={`action-button ${load ? "active" : ""}`}
            onClick={handleLoadAmi}
          >
            Load Ami
          </button>
        </div>

        <div className="grid-item">
          <button
            className={`action-button ${save ? "active" : ""}`}
            onClick={() => setSave(!save)}
          >
            Save
          </button>
        </div>

        <div className="grid-item">
          <button
            className={`action-button ${stopOrders ? "active" : ""}`}
            onClick={() => setStopOrders(!stopOrders)}
          >
            Stop Orders
          </button>
        </div>

        <div className="grid-item">
          <button
            className={`action-button ${startOrders ? "active" : ""}`}
            onClick={() => setStartOrders(!startOrders)}
          >
            Start Orders
          </button>
        </div>

        <div className="grid-item">
          <button
            className={`action-button ${startRTD ? "active" : ""}`}
            onClick={handleStartRTD}
          >
            Start RTD
          </button>
        </div>

        <div className="grid-item">
          <button
            className={`action-button ${stopRtd ? "active" : ""}`}
            onClick={() => setStopRtd(!stopRtd)}
          >
            Stop RTD
          </button>
        </div>

        <div className="grid-item">
          <button
            className={`action-button ${clearAll ? "active" : ""}`}
            onClick={() => setClearAll(!clearAll)}
          >
            Clear All
          </button>
        </div>

        {/* AmiSpd */}
        <div className="grid-item">
          <label>AmiSpd:</label>
          <input
            type="number"
            value={amiSpd}
            onChange={(e) => setAmiSpd(e.target.value)}
          />
        </div>

        {/* Scripts */}
        <div className="grid-item">
          <label>Scripts:</label>
          <input
            type="text"
            value={scripts}
            onChange={(e) => setScripts(e.target.value)}
          />
        </div>
      </div>
    </div>
  );
}

export default App;
