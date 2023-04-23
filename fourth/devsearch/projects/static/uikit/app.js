let alertWrapper = document.querySelector('.alert');
let alertClose = document.querySelector('.alert__close');

if (alertWrapper) {
  alertClose.addEventListener('click', () => 
    alertWrapper.style.display = 'none'
)}


const openModal = document.querySelector('.openModal');
const closeModal = document.querySelector('.closeModal');
const modal = document.querySelector('.modal');

    openModal.addEventListener('click', () => {
    modal.showModal()
})
    closeModal.addEventListener('click', () => {
    modal.close()
})

    modal.addEventListener('click', (e) => {
    console.log(e.target)
    if(e.target === modal) modal.close()
    })