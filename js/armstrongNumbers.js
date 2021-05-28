// How can you make this more scalable and reusable later?

//exports.findArmstrongNumbers = function(output) {
function findArmstrongNumbers(input) {
    let result = []
    let test = []
    for (var value of input) {
        let eachNumber = []
        eachNumber.push(value.toString())
        
        var addNum = 0
        for (let num of eachNumber) {
            var split = num.split('')
            for (var i of split) {
                addNum += i**split.length
            }
        }
        

        if (value == addNum) {
            result.push(addNum)
        }
    }
    

    return result
};


console.log(findArmstrongNumbers([0]))// === [0]);
console.log(findArmstrongNumbers(Array.from(Array(8).keys())))// == [0, 1, 2, 3, 4, 5, 6, 7]);
console.log(findArmstrongNumbers(Array.from(Array(99).keys())))// == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
console.log(findArmstrongNumbers(Array.from(Array(999).keys())))// == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]);