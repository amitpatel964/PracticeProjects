"use strict"

// All of the HTML elements
const numberButtons = document.querySelectorAll('[data-number]');
const operationButtons = document.querySelectorAll('[data-operation]');
const equalsButton = document.querySelector('[data-equals]');
const deleteButton = document.querySelector('[data-delete]');
const allClearButton = document.querySelector('[data-all-clear]');
const previousOperandTextElement = document.querySelector('[data-previous-operand]');
const currentOperandTextElement = document.querySelector('[data-current-operand]');
const calculator = new Calculator(previousOperandTextElement, currentOperandTextElement);

class Calculator {
  constructor(previousOperandTextElement, currentOperandTextElement) {
    this.previousOperandTextElement = previousOperandTextElement;
    this.currentOperandTextElement = currentOperandTextElement;
    this.clear();
  }
}

// Clears the screen and any current inputs
function clear() {
  this.currentOperand = '';
  this.previousOperand = '';
  this.operation = null;
}

function remove() {
}

// Appends a number on the display
function appendNumber(number) {
  if (number === '.' && this.currentOperand.includes('.')) {
    return;
  }

  this.currentOperand = this.currentOperand.toString() + number.toString();
}

// Checks to see which operation was chosen
function chooseOperation(operation) {
  if (this.currentOperand === '') {
    return;
  }
  if (this.previousOperand !== '') {
    this.compute();
  }
  this.operation = operation;
  this.previousOperand = this.currentOperand;
  this.currentOperand = '';
}

// compute() {
// }

// Updates the number on the display
function updateDisplay() {
  this.currentOperandTextElement.innerText = this.currentOperand;
}

// When a number button is pressed, the corresponding methods are called
numberButtons.forEach(button => {
  button.addEventListener('click', () => {
    calculator.appendNumber(button.innerText);
    calculator.updateDisplay();
  })
})

// When an operation button is pressed, the corresponding methods are called
operationButtons.forEach(button => {
  button.addEventListener('click', () => {
    calculator.chooseOperation(button.innerText);
    calculator.updateDisplay();
  })
})

// Equals button is pressed
equalsButton.addEventListener('click', button => {
  calculator.compute()
  calculator.updateDisplay()
})