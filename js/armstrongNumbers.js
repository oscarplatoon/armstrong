// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(num) {
    let results = []
    //checking 137 in for loop
    for (let i = 0; i <= num; i++) {
        let numberOfDigits = i.toString().length
        let sum = 0
            //For every digit in 137, raise it to the power to the number of digits and add sum.
            let temp = i;
            while (temp > 0) {
                let remainder = temp % 10;
                sum += remainder ** numberOfDigits;
                // removing last digit from the number
                temp = parseInt(temp / 10);
            }
            if (sum == i) {
                results.push(i)
            }      
}
return results
}



