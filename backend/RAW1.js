const fs = require("fs"); // Use Node.js fs module for file operations
const path = require("path");

// File paths
const sourceFile = "./output/websocket_data.csv";
const destinationFile = "./output/ami_websocket_data.csv";

// Function to copy the CSV file from source to destination
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

// Placeholder for AmiBroker update (you need a Node.js wrapper for AmiBroker if required)
function updateAmiBrokerData() {
  console.log(
    "AmiBroker update is not implemented in Node.js, but this is where you can do it."
  );
  // Implement AmiBroker data update logic here if you have a Node.js interface with AmiBroker
}

// Function to copy the file and update AmiBroker in sequence
function updateData() {
  copyCSVFile(); // First, copy the CSV file
  updateAmiBrokerData(); // Then, update AmiBroker with the copied file
}

// Run the updateData function every 30 seconds in a loop
setInterval(updateData, 3000); // 30-second interval
