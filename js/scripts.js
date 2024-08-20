const addressForm = document.querySelector("#address-form");
const cepInput = document.querySelector("#cep");
const addressInput = document.querySelector("#address");
const cityInput = document.querySelector("#city");
const neighborhoodInput = document.querySelector("#neighborhood");
const regionInput = document.querySelector("#region");
const formInputs = document.querySelectorAll("[data-input]"); // Use querySelectorAll para pegar todos os inputs com data-input

const closeButton = document.querySelector("#close-message");

// Validate cep Input
cepInput.addEventListener("keypress", (e) => {
    const onlyNumbers = /[0-9]/;
    const key = String.fromCharCode(e.keyCode);


    // Check if the key is a number
    if (!onlyNumbers.test(key)) {
        e.preventDefault(); // Prevent input if it's not a number
        return;
    }
});

cepInput.addEventListener("keyup", (e) => {
    const inputValue = e.target.value;

    if(inputValue.length ===8){
        getAddress(inputValue)
    }
});
const getAddress = async (cep) => {
    console.log(cep);
}
