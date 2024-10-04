document.addEventListener('DOMContentLoaded', function () {
    const user = Telegram.WebApp.initDataUnsafe.user;

    if (user) {
        document.getElementById('user-id').textContent = 'User ID: ' + user.id;
        document.getElementById('username').textContent = 'Username: ' + (user.username ? user.username : 'N/A');
        document.getElementById('first-name').textContent = 'First Name: ' + (user.first_name ? user.first_name : 'N/A');
        document.getElementById('last-name').textContent = 'Last Name: ' + (user.last_name ? user.last_name : 'N/A');
    } else {
        document.querySelector('.user-info').innerHTML = '<p>User data is not available.</p>';
    }
});