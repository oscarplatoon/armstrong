// How can you make this more scalable and reusable later?

findArmstrongNumbers = function(x) {
//  findArmstrongNumbers = function(x) {
  let armstrongArr = [];
  for (let i = 0; i < x.length; i++) {
    if (isArmstrong(x[i])) {
      armstrongArr.push(x[i]);
    }
  }
  return armstrongArr;
};

function isArmstrong(n) {
  let num = n.toString().split("");
  let sum = 0;
  for (let i = 0; i < num.length; i++) {
    sum += Math.pow(num[i], num.length);
  }
  return sum === n;
};


module.exports = findArmstrongNumbers;


