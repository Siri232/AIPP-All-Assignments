// CodeChef-compatible JavaScript code

function printStudents(students) {
    console.log("Student List:");
    students.forEach(name => console.log(name));
}

const fs = require("fs");

// Read input from STDIN
let input = fs.readFileSync(0, "utf8").trim();

// Convert input into array
let students = input.split(",").map(s => s.trim());

// Call the function
printStudents(students);
