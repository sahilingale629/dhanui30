var fso = new ActiveXObject("Scripting.FileSystemObject"); // File system object for file operations
var AmiBroker = new ActiveXObject("Broker.Application"); // Create AmiBroker app object

// File paths
var sourceFile = "Z:\\ASCII\\all_symbols_data.csv";
var destinationFile = "D:\\Kaustubh\\Python\\Subra\\all_symbols_data.csv";

// Function to copy the CSV file from source to destination
function copyCSVFile() {
  WScript.echo("Checking if source file exists..."); // Debug message
  if (fso.FileExists(sourceFile)) {
    WScript.echo("Source file exists, copying to destination..."); // Debug message
    fso.CopyFile(sourceFile, destinationFile, true); // true = overwrite if exists
    WScript.echo("File copied from Z: to D: drive successfully.");
  } else {
    WScript.echo("Source file does not exist: " + sourceFile);
  }
}

// Function to update AmiBroker data
function updateAmiBrokerData() {
  WScript.echo("Checking database path..."); // Debug message
  if (
    AmiBroker.DatabasePath ==
    "C:\\Program Files (x86)\\AmiBroker\\Databases\\PS"
  ) {
    WScript.echo("Updating AB data in progress");

    // Import the CSV data from the destination path
    //AmiBroker.Import(0, destinationFile, "Subra1.format");
    AmiBroker.Import(0, destinationFile, "mint1.format");
    WScript.echo("Updating AB data completed");

    // Refresh AmiBroker
    AmiBroker.RefreshAll();
  } else {
    WScript.echo(
      "Database path does not match. Current path: " + AmiBroker.DatabasePath
    );
  }
}

// Function to copy the file and update AmiBroker in sequence
function updateData() {
  copyCSVFile(); // First, copy the CSV file
  updateAmiBrokerData(); // Then, update AmiBroker with the copied file
}

// Run the updateData function every 30 seconds in a loop
while (true) {
  updateData();
  WScript.Sleep(3000); // Wait for 30 seconds before the next update
}
