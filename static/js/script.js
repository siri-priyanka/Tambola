const numbers = ['4', '67', '76', '40', '70', '20', '57', '5', '58', '89',
'12', '66', '8', '19', '56', '47', '23', '26', '17', '68',
'83', '78', '27', '1', '42', '30', '29', '45', '22', '10']; // Example numbers
const container = document.querySelector('.spiral-container');

let currentIndex = 0;

function addNumberToSpiral() {
    const numberElement = document.createElement('div');
    numberElement.classList.add('number');
    numberElement.innerText = numbers[currentIndex];
    numberElement.style.animationDelay = `${currentIndex * 1}s`; // Add delay for each number
    container.appendChild(numberElement);

    currentIndex = (currentIndex + 1) % numbers.length;
}

// Add a number every 2 seconds (for example)
setInterval(addNumberToSpiral, 2000);