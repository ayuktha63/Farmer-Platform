document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('retailer-login-form');
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        fetch(form.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                username: username,
                password: password
            })
        })
        .then(response => {
            if (response.ok) {
                window.location.href = '/retailer_dashboard'; // Redirect on successful login
            } else {
                return response.text();
            }
        })
        .then(error => {
            errorMessage.textContent = error || 'An error occurred during login.';
        })
        .catch(error => {
            errorMessage.textContent = 'An error occurred during login.';
        });
    });
});
