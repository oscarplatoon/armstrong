// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(num) {
  // step 1: loop over numbers from 0 to 999
  // step 2 : split number into digits
  // step 3: cube digits and sum
  // step 4: compare square of sums to number

  let armstrongArray = [];

  for (let i = 0; i < num.length; i++) {
    let numString = i.toString();
    numString = numString.split("")
    let numArray = []

    for (let x in numString) {
      numArray[x] = parseInt(numString[x])
    }

    let sumOfDigits = 0;

    for (let x in numArray) {
      sumOfDigits += numArray[x] ** numArray.length;
    }

    if (i === sumOfDigits) {
      armstrongArray.push(i);
    }
}


  return armstrongArray;

};
