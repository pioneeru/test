
// test_vulnerability.js
function executeInput(userInput) {
    // CodeQL will flag this as a code injection risk 
    eval(userInput); 
}

alert("testing scan vulnerability");