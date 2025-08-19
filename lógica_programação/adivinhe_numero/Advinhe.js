// Generate a Random Number
let y = Math.floor(Math.random() * 10 + 1);

// Counting the number of guesses
// made for correct Guess
let guess = 1;

function advinhar () {

    // Number guessed by user    
    let x = 5

    if (x == y) {
        console.log("CONGRATULATIONS!!! YOU GUESSED IT RIGHT IN "+ guess + " GUESS ");
    }

    /* If guessed number is greater than actual number*/
    else if (x > y) {
        console.log(++guess)
        console.log("OOPS SORRY!! TRY A SMALLER NUMBER");
    }
    else {
        console.log(++guess)
        console.log("OOPS SORRY!! TRY A GREATER NUMBER")
    }
}


advinhar()