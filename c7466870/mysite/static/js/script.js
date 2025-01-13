// Search Button Toggle Functionality

document.querySelector('#burger').addEventListener('click', () => {
    console.log('Burger icon clicked'); // Debug message
    document.querySelector('#nav-links').classList.toggle('is-active');
});


