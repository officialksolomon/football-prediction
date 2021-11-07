const options = document.querySelectorAll('.team');
const predictionOptions = Array.from(options);

// fill form with innertext
const fillForm = (element) => {
  // console.log(element.parentNode.parentNode);
  let formElements =
    element.parentNode.parentNode.children[1].children[0].elements;
  const predictionInput = formElements[3];
  console.log(predictionInput);
  predictionInput.value = element.innerText;
};
// console.log(option.nextElementSibling);
//
predictionOptions.forEach((element) =>
  element.addEventListener('click', () => {
    fillForm(element);
  })
);

// hide message alert
const hideMessage = () => {
  const message = document.querySelector('.message');
  if (message.style.display !== 'none') {
    message.classList.add('message-hide');
  }
};
setTimeout(hideMessage, 2000);


