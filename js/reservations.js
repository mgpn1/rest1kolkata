document.addEventListener('DOMContentLoaded', () => {
    const bookingForm = document.getElementById('bookingForm');
    const dateInput = document.getElementById('date');
    const timeInput = document.getElementById('time');
    const guestsInput = document.getElementById('guests');

    // Set minimum date to today
    const today = new Date().toISOString().split('T')[0];
    dateInput.min = today;

    // Set maximum date to 30 days from today
    const maxDate = new Date();
    maxDate.setDate(maxDate.getDate() + 30);
    dateInput.max = maxDate.toISOString().split('T')[0];

    // Form validation
    function validateForm() {
        let isValid = true;
        const formData = new FormData(bookingForm);

        // Name validation
        const name = formData.get('name');
        if (name.length < 2) {
            showError('name', 'Please enter a valid name');
            isValid = false;
        } else {
            clearError('name');
        }

        // Email validation
        const email = formData.get('email');
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            showError('email', 'Please enter a valid email address');
            isValid = false;
        } else {
            clearError('email');
        }

        // Phone validation
        const phone = formData.get('phone');
        const phoneRegex = /^[0-9]{10}$/;
        if (!phoneRegex.test(phone)) {
            showError('phone', 'Please enter a valid 10-digit phone number');
            isValid = false;
        } else {
            clearError('phone');
        }

        // Date validation
        const date = new Date(formData.get('date'));
        if (date < new Date(today)) {
            showError('date', 'Please select a valid date');
            isValid = false;
        } else {
            clearError('date');
        }

        // Time validation
        const time = formData.get('time');
        if (!time) {
            showError('time', 'Please select a time');
            isValid = false;
        } else {
            clearError('time');
        }

        // Guests validation
        const guests = formData.get('guests');
        if (!guests) {
            showError('guests', 'Please select number of guests');
            isValid = false;
        } else {
            clearError('guests');
        }

        return isValid;
    }

    // Show error message
    function showError(fieldId, message) {
        const field = document.getElementById(fieldId);
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = message;
        
        // Remove existing error message if any
        clearError(fieldId);
        
        field.parentNode.appendChild(errorDiv);
        field.classList.add('error');
    }

    // Clear error message
    function clearError(fieldId) {
        const field = document.getElementById(fieldId);
        const errorDiv = field.parentNode.querySelector('.error-message');
        if (errorDiv) {
            errorDiv.remove();
        }
        field.classList.remove('error');
    }

    // Handle form submission
    bookingForm.addEventListener('submit', (e) => {
        e.preventDefault();

        if (validateForm()) {
            const formData = new FormData(bookingForm);
            const bookingData = Object.fromEntries(formData.entries());

            // Show loading state
            const submitButton = bookingForm.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            submitButton.textContent = 'Processing...';
            submitButton.disabled = true;

            // Simulate API call (replace with actual API endpoint)
            setTimeout(() => {
                // Show success message
                showSuccessMessage();
                
                // Reset form
                bookingForm.reset();
                
                // Reset button state
                submitButton.textContent = originalText;
                submitButton.disabled = false;
            }, 1500);
        }
    });

    // Show success message
    function showSuccessMessage() {
        const successDiv = document.createElement('div');
        successDiv.className = 'success-message';
        successDiv.innerHTML = `
            <i class="fas fa-check-circle"></i>
            <h3>Reservation Successful!</h3>
            <p>Thank you for choosing Spice Heritage. We'll send you a confirmation email shortly.</p>
        `;

        // Remove existing success message if any
        const existingSuccess = document.querySelector('.success-message');
        if (existingSuccess) {
            existingSuccess.remove();
        }

        // Add success message
        bookingForm.parentNode.insertBefore(successDiv, bookingForm);

        // Remove success message after 5 seconds
        setTimeout(() => {
            successDiv.remove();
        }, 5000);
    }

    // Add input event listeners for real-time validation
    const inputs = bookingForm.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.addEventListener('input', () => {
            validateForm();
        });
    });
}); 