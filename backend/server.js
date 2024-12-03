const express = require("express");
const bodyParser = require("body-parser");
const fs = require("fs");
const path = require("path");
const cors = require("cors");
const multer = require("multer");
const csv = require("csv-parser");
const WebSocket = require("ws");
const dayjs = require("dayjs");
const timezone = require("dayjs/plugin/timezone");
const utc = require("dayjs/plugin/utc");
const createCsvWriter = require("csv-writer").createObjectCsvWriter;

const { exec } = require("child_process");

const app = express();
const PORT = 5001;

dayjs.extend(utc);
dayjs.extend(timezone);

const sourceFile = "./output/websocket_data.csv";
const destinationFile = "./output/ami_websocket_data.csv";
const expectedDatabasePath =
  "C:\\Program Files (x86)\\AmiBroker\\Databases\\PS";
const formatFile = "mint1.format";

function copyCSVFile() {
  console.log("Checking if source file exists...");

  // Check if source file exists
  if (fs.existsSync(sourceFile)) {
    console.log("Source file exists, copying to destination...");
    fs.copyFileSync(sourceFile, destinationFile); // Synchronously copy the file
    console.log("File copied from Z: to D: drive successfully.");
  } else {
    console.log("Source file does not exist: " + sourceFile);
  }
}

function updateAmiBrokerData() {
  console.log("Checking database path...");

  // Simulating getting the current database path from AmiBroker
  const currentDatabasePath =
    "C:\\Program Files (x86)\\AmiBroker\\Databases\\PS"; // Replace with actual logic to get the path

  if (currentDatabasePath === expectedDatabasePath) {
    console.log("Updating AB data in progress...");

    // Check if the destination CSV file exists
    if (fs.existsSync(destinationFile)) {
      // Import the CSV file using AmiBroker CLI command (assuming AmiBroker has a CLI tool)
      const importCommand = `AmiBrokerImport --file="${destinationFile}" --format="${formatFile}"`;

      exec(importCommand, (error, stdout, stderr) => {
        if (error) {
          console.error(`Error during import: ${error.message}`);
          return;
        }
        if (stderr) {
          console.error(`stderr: ${stderr}`);
          return;
        }

        console.log(`stdout: ${stdout}`);
        console.log("Updating AB data completed.");

        // Refresh AmiBroker database (assuming this is how it's done via CLI)
        const refreshCommand = "AmiBrokerRefresh"; // Replace with the actual command for refreshing
        exec(refreshCommand, (error, stdout, stderr) => {
          if (error) {
            console.error(`Error during refresh: ${error.message}`);
            return;
          }
          if (stderr) {
            console.error(`stderr: ${stderr}`);
            return;
          }

          console.log("AmiBroker database refreshed.");
        });
      });
    } else {
      console.log(`Error: CSV file not found at ${destinationFile}`);
    }
  } else {
    console.log(
      `Database path does not match. Current path: ${currentDatabasePath}`
    );
  }

  // Implement AmiBroker data update logic here if you have a Node.js interface with AmiBroker
}

// Function to copy the file and update AmiBroker in sequence
function updateData() {
  copyCSVFile(); // First, copy the CSV file
  updateAmiBrokerData(); // Then, update AmiBroker with the copied file
}

const ensureFileHasHeader = (filePath) => {
  // Check if the file exists
  if (!fs.existsSync(filePath)) {
    const header = "date,time,symbol,ltp,lastTradeQuantity,volume\n";
    // Write the header line to the CSV file
    fs.writeFileSync(filePath, header, "utf8");
  }
};

const writeToCSV = (data) => {
  const filePath = "./output/websocket_data.csv";

  // Check if the file is empty before appending data
  const isFileEmpty =
    fs.existsSync(filePath) && fs.readFileSync(filePath, "utf8").length === 0;

  const csvLine = `${data.date},${data.time},${data.symbol},${data.ltpcon},${data.lastTradeQuantity},${data.volume}\n`;

  // Append the data only if the file isn't empty, or create it with the first line
  if (isFileEmpty) {
    fs.writeFileSync(filePath, csvLine, "utf8");
  } else {
    fs.appendFile(filePath, csvLine, (err) => {
      if (err) {
        console.error("Error writing to CSV:", err);
      } else {
        console.log("Data written to CSV successfully");
      }
    });
  }
};

// Ensure the output directory exists
const outputDir = path.join(__dirname, "output");
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}

app.use(cors());

// Middleware to parse JSON
app.use(bodyParser.json());

app.post("/updateAmiBrokerData", (req, res) => {
  try {
    // Logic to update AmiBroker data
    // Example: You might want to call an external service or update data in the database

    // Replace the following with your actual AmiBroker update logic:
    console.log("AmiBroker data update triggered...");
    updateData();

    // Simulate a successful operation
    // You can replace this with actual data processing logic
    // If everything is successful:
    res.status(200).json({ message: "AmiBroker data updated successfully!" });
  } catch (error) {
    // Log the error for debugging purposes
    console.error("Error updating AmiBroker data:", error);

    // Respond with an error message
    res
      .status(500)
      .json({ error: "An error occurred while updating AmiBroker data." });
  }
});

// Endpoint to start RTD
app.post("/startRTD", (req, res) => {
  const filePath = "./uploads/selected_symbols.csv"; // Path to the CSV file

  const instrumentList = [];

  // Ensure the file exists
  if (!fs.existsSync(filePath)) {
    return res.status(404).send("CSV file not found in uploads folder");
  }

  fs.createReadStream(filePath)
    .pipe(csv())
    .on("data", (row) => {
      if (Object.values(row).every((value) => value.trim() === "")) {
        return;
      }
      instrumentList.push({
        ExchangeSegment: row.Exchange_Segment,
        SecurityId: row.Token,
        Symbol: row.Symbol,
      });
    })
    .on("end", () => {
      console.log("CSV successfully processed");

      // Start WebSocket connection
      connectWS(instrumentList);

      res.status(200).send("RTD started successfully!");
    })
    .on("error", (error) => {
      console.error("Error processing CSV:", error);
      res.status(500).send("Failed to process CSV");
    });
});

function displaySymbolByToken(token, instrumentList) {
  const result = instrumentList.find(
    (item) => Number(item.SecurityId) == token
  );
  return result?.Symbol;
}

// WebSocket function with CSV writing
function connectWS(instrumentList) {
  const ws = new WebSocket(
    "wss://api-feed.dhan.co?version=2&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzMzMjg0Nzg0LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMzUzMTIwMSJ9.DJhLUIF5EZXYDBQ6LVpF6i3rB41aPEXi8o2DSkxKZ8nt8-PZthRvzSr8HIfdlFwQH61_ZnO1mnbr5mM9eFwZBA&clientId=1103531201&authType=2"
  );

  ws.on("open", () => {
    const requestPayload = {
      RequestCode: 17,
      InstrumentCount: instrumentList.length,
      InstrumentList: instrumentList,
    };
    ws.send(JSON.stringify(requestPayload));
    console.log("WebSocket message sent");
  });

  ws.on("message", (message) => {
    if (!message) {
      console.error("Received undefined data");
      return;
    }

    const binaryData = Buffer.isBuffer(message)
      ? message
      : Buffer.from(message);

    if (binaryData.length < 34) {
      console.error("Received data is too short:", binaryData.length);
      return;
    }

    try {
      const securityID = binaryData.readUInt32LE(4);
      const ltp = binaryData.readFloatLE(8);
      const ltpcon = Math.round(ltp * 100) / 100; // Ensure exactly 2 decimal places

      const lastTradeQuantity = binaryData.readUInt16LE(12);
      const volume = binaryData.readUInt32LE(22);
      const lastTradeTime = binaryData.readUInt32LE(14);

      const adjustedTimestamp = lastTradeTime - 5.5 * 60 * 60; // Subtract 4.5 hours in seconds

      const date = dayjs
        .unix(adjustedTimestamp)

        .tz("Asia/Kolkata")
        .format("YYYYMMDD");
      const time = dayjs
        .unix(adjustedTimestamp)

        .tz("Asia/Kolkata")
        .format("HH:mm:ss");

      const symbol = displaySymbolByToken(securityID, instrumentList);
      console.log("ltp -> ", ltp);
      console.log("ltpcon -> ", ltpcon);
      console.log(
        `Symbol: ${symbol}, LTP: ${ltpcon}, Volume: ${volume}, Date: ${date}, Time: ${time} , LTQ : ${lastTradeQuantity} `
      );

      writeToCSV({
        symbol,
        ltpcon,
        volume,
        date,
        time,
        lastTradeQuantity,
      });
    } catch (error) {
      console.error("Error while parsing binary data:", error);
    }
  });

  ws.on("error", (error) => {
    console.error("WebSocket error:", error);
  });

  ws.on("close", () => {
    console.log("WebSocket connection closed");
  });
}
// Serve the CSV file
app.get("/merged_file.csv", (req, res) => {
  res.sendFile(path.join(__dirname, "merged_file1.csv"));
});

// Set up storage for uploaded files
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "uploads/"); // Directory to save files
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname); // Use original file name
  },
});

const upload = multer({ storage });

// Create uploads directory if it doesn't exist

if (!fs.existsSync("uploads")) {
  fs.mkdirSync("uploads");
}

// Endpoint to handle file uploads
app.post("/upload", upload.single("file"), (req, res) => {
  res.status(200).json({ message: "File uploaded successfully" });
});

app.get("/ami-websocket-data", (req, res) => {
  const filePath = path.join(__dirname, "output", "ami_websocket_data.csv");

  // Check if the file exists
  if (fs.existsSync(filePath)) {
    // Send the file to the client
    res.sendFile(filePath, (err) => {
      if (err) {
        console.error("Error sending file:", err);
        res.status(500).send("Error occurred while sending the file.");
      }
    });
  } else {
    // Send a 404 if the file doesn't exist
    res.status(404).send("File not found.");
  }
});

setInterval(copyCSVFile, 3000);

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
