document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.alert-dismissible');
    if (alerts.length > 0) {
        setTimeout(function () {
            alerts.forEach(function (alert) {
                const closeButton = alert.querySelector('.btn-close');
                if (closeButton) closeButton.click();
            });
        }, 5000);
    }
});