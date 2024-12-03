// Import day.js and timezone plugin: npm install dayjs dayjs-plugin-timezone
const dayjs = require("dayjs");
const timezone = require("dayjs/plugin/timezone");
const utc = require("dayjs/plugin/utc");

dayjs.extend(utc);
dayjs.extend(timezone);

function convertEpochToIST(epochTime) {
  // Convert epoch to IST
  return dayjs.unix(epochTime).tz("Asia/Kolkata").format("YYYYMMDD HH:mm:ss");
}

// Example usage
const epochTime = 1732722757; // Replace with your epoch timestamp
console.log("IST Date and Time:", convertEpochToIST(epochTime));
