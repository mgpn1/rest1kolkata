document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    // Form validation function
    function validateForm() {
        let isValid = true;
        const name = document.getElementById('name');
        const email = document.getElementById('email');
        const subject = document.getElementById('subject');
        const message = document.getElementById('message');

        // Name validation
        if (name.value.trim() === '') {
            showError(name, 'Please enter your name');
            isValid = false;
        } else if (name.value.length < 2) {
            showError(name, 'Name must be at least 2 characters long');
            isValid = false;
        } else {
            clearError(name);
        }

        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email.value.trim() === '') {
            showError(email, 'Please enter your email');
            isValid = false;
        } else if (!emailRegex.test(email.value)) {
            showError(email, 'Please enter a valid email address');
            isValid = false;
        } else {
            clearError(email);
        }

        // Subject validation
        if (subject.value.trim() === '') {
            showError(subject, 'Please enter a subject');
            isValid = false;
        } else if (subject.value.length < 5) {
            showError(subject, 'Subject must be at least 5 characters long');
            isValid = false;
        } else {
            clearError(subject);
        }

        // Message validation
        if (message.value.trim() === '') {
            showError(message, 'Please enter your message');
            isValid = false;
        } else if (message.value.length < 10) {
            showError(message, 'Message must be at least 10 characters long');
            isValid = false;
        } else {
            clearError(message);
        }

        return isValid;
    }

    // Show error message
    function showError(input, message) {
        const formGroup = input.parentElement;
        const error = formGroup.querySelector('.error-message') || document.createElement('div');
        error.className = 'error-message';
        error.textContent = message;
        if (!formGroup.querySelector('.error-message')) {
            formGroup.appendChild(error);
        }
        input.classList.add('error');
    }

    // Clear error message
    function clearError(input) {
        const formGroup = input.parentElement;
        const error = formGroup.querySelector('.error-message');
        if (error) {
            formGroup.removeChild(error);
        }
        input.classList.remove('error');
    }

    // Show success message
    function showSuccessMessage() {
        const successMessage = document.createElement('div');
        successMessage.className = 'success-message';
        successMessage.textContent = 'Thank you for your message! We will get back to you soon.';
        contactForm.appendChild(successMessage);

        // Remove success message after 5 seconds
        setTimeout(() => {
            successMessage.remove();
        }, 5000);
    }

    // Handle form submission
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();

        if (validateForm()) {
            // Simulate API call
            const submitButton = contactForm.querySelector('button[type="submit"]');
            submitButton.disabled = true;
            submitButton.textContent = 'Sending...';

            // Simulate API delay
            setTimeout(() => {
                showSuccessMessage();
                contactForm.reset();
                submitButton.disabled = false;
                submitButton.textContent = 'Send Message';
            }, 1500);
        }
    });

    // Real-time validation
    const inputs = contactForm.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            validateForm();
        });
    });

    // Add smooth scrolling for map section
    const mapSection = document.querySelector('.map-section');
    if (mapSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, {
            threshold: 0.1
        });

        observer.observe(mapSection);
    }
}); 