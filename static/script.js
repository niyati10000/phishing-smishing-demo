// Add some realistic behavior
console.log('Facebook clone loaded - EDUCATIONAL USE ONLY');

// Prevent form resubmission warning
if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}

// Add fake typing indicator
document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.style.backgroundColor = '#ffffff';
        });
    });
});