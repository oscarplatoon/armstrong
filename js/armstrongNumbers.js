// How can you make this more scalable and reusable later?
// ## Release 0
// Write a program in Python and Javascript to find all Armstrong numbers in the range of `0` and `999`.

// Release 0  


exports.findArmstrongNumbers = function(num) {
  counter = num;
  let resultArray =[]

  while (counter >= 0) {
      // Destructure input num into an array 
      let inputArray = String(counter).split("").map((counter) => {
         return Number(counter)
      });
      
      // this length will be the power to which we raise each digit in our numbers
      let length = inputArray.length

      //catches the squared elements to sum and compare to the base number (counter in this logic)
      let squaredElem = []

      //catches sum of the squared elements to compare to counter
      let total = 0

      //generates the digits raised to the power of the number of digits in the input number
      inputArray.forEach( item => squaredElem.push(item**length))
      
      //loops over the num**length and adds all elements together
      squaredElem.forEach( elem => total+= elem)
      
      // check too see if added (num**length) === counter
      if (total == counter) resultArray.push(total)
      counter--
      
  }
  //return resulting array
  resultArray.sort((a,b) => a-b)
  console.log(resultArray)
  return resultArray
};
