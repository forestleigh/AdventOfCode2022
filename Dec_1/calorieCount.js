/*
--- Day 1: Calorie Counting ---
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
*/

// the question says to keep track of which elves has the most calories
// import Node's file reader
const fs = require("fs");
// read contents of the file
const data = fs.readFileSync("./Data.txt", "UTF-8");

// split the contents by new line into array of substrings
// A carriage return (\r) + newline (\n) is best practice
const array = data.split(/\r?\n/);

const calCount = (arrayOfData) => {
  // to parse string into elves and their calorie counts
  // initialize the elf cache, elf count, and max calorie count
  const elves = {};
  let currElf = 1;
  let maxCals = 0;

  arrayOfData.forEach((element) => {
    // if the element is an eplty string, switch to the next elf
    if (!element) currElf++;
    if (elves[currElf]) {
      elves[currElf] = elves[currElf] + Number(element);
    } else {
      elves[currElf] = Number(element);
    }
    maxCals = Math.max(maxCals, elves[currElf]);
  });

  // use filter method in case more than one elf ties for the max calories brought
  const elfWithMaxCals = Object.keys(elves).filter((key) => elves[key] === maxCals);

  return [
    "Elf(s) with most calories: ",
    elfWithMaxCals,
    "max calorie amount: ",
    maxCals,
  ];
};

console.log(calCount(array));

/*
--- Part Two ---
Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
*/

// here we will also keep track of which elves as well as how many cals
const calCount2 = (arrayOfData) => {
  // to parse string into elves and their calorie counts
  // initialize the elf cache, elf count, and max calorie count
  const elves = {};
  let currElf = 1;

  arrayOfData.forEach((element) => {
    // if the element is an eplty string, switch to the next elf
    if (!element) currElf++;
    if (elves[currElf]) {
      elves[currElf] = elves[currElf] + Number(element);
    } else {
      elves[currElf] = Number(element);
    }
  });

  // sort the calories values in accending order
  const calsArray = Object.values(elves).sort((a, b) => a - b);
  // isolate the top 3 values
  const topThree = calsArray.slice(-3);
  // use reduce to add the top 3 values together
  const maxCals = topThree.reduce((a, b) => a + b);

  // use filter method to identify the top 3+ elves by their calorie amounts
  const maxElves = Object.keys(elves).filter(
    (key) =>
      elves[key] === topThree[0] ||
      elves[key] === topThree[1] ||
      elves[key] === topThree[2]
  );

  return [
    "Elves with the most calories: ",
    maxElves,
    "max calorie amount: ",
    maxCals,
  ];
};

console.log(calCount2(array));
