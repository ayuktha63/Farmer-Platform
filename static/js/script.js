function toggleMenu() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('expanded');
}
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#farmer-login-form');
    const errorMessage = document.querySelector('#error-message');

    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent form from submitting

        const username = document.querySelector('#username').value;
        const password = document.querySelector('#password').value;

        // Perform validation (example)
        if (username === 'farmer' && password === 'farmer') {
            form.submit(); // Submit the form if valid
        } else {
            errorMessage.textContent = 'Invalid username or password';
        }
    });
});
