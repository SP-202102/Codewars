
function greet(name){
    console.log('hello ' + name);
}

function square(number){
    return number * number;
}


let myNumber = 3
let myName = "Tim"
greet(myName);
myName = "uschi";
greet(myName.toUpperCase());


console.log('square of ' + myNumber + ':' +square(myNumber));