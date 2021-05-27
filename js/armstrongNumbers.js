
exports.findArmstrongNumbers = function(arr) {
  let copyArray = arr.slice()
  let armstrongNumbers = []
  let powerVar = ''
  
  function seperateDigits(index) {
  
   let intialIndexValue = index
   
   let indexStr = index.toString();
   let indexArr= indexStr.split('')

   let indexArrInt = []
   let indexArrIntPowered = []

   for (i=0;i<indexArr.length;i++) {
    indexArrInt.push(Number(indexArr[i]))
   }
   let powerVar = indexArrInt.length

   let sum = 0

   for (x=0;x<indexArrInt.length;x++) {
    indexArrIntPowered.push(indexArrInt[x] ** powerVar)
    let quotient = (indexArrInt[x] ** powerVar)
    sum += quotient
   }

   if (sum == intialIndexValue) {
     return true
   } else {
     return false
   }
   
  }
  for (n=0;n<arr.length;n++) {
    if (seperateDigits(arr[n]) == true) {
    armstrongNumbers.push(arr[n])
    } else {
    }
  }

  return armstrongNumbers
}