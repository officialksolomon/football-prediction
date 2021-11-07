const form = document.querySelector('.login-form')
let formElements
if (form !== null) {
  formElements = form.elements
  
}
const elements = Array.from(formElements)

// add css class to each elements
elements.forEach(elements => elements.classList.add('form-control'))
