// Define the target word
const targetWord = word;
let remainingAttempts = 6;

// Initialize display
let wordDisplay = "";
for (let i = 0; i < targetWord.length; i++) {
    wordDisplay += "-";
}
document.getElementById("word-display").textContent = wordDisplay;

// Function to check user's guess
function checkGuess() {
    const guess = document.getElementById("guess-input").value.toLowerCase();
    if (guess.length !== targetWord.length) {
        alert("Please enter a " + targetWord.length + "-letter word.");
        return;
    }

    let feedback = "";
    for (let i = 0; i < targetWord.length; i++) {
        if (guess[i] === targetWord[i]) {
            feedback += "O";
        } else if (targetWord.includes(guess[i])) {
            feedback += "X";
        } else {
            feedback += "-";
        }
    }
    
    const feedbackParagraph = document.createElement("p");
    feedbackParagraph.textContent = feedback;
    document.getElementById("wordle-container").appendChild(feedbackParagraph);


    if (feedback === "OOOOO") {
        alert("Congratulations! You've guessed the word!");
    } else {
        remainingAttempts--;
        if (remainingAttempts === 0) {
            alert("You've run out of attempts. The word was: " + targetWord);
        } else {
            alert("Incorrect guess. You have " + remainingAttempts + " attempts left.");
        }
    }
}
