document.addEventListener('DOMContentLoaded', function() {
    const copyButtons = document.querySelectorAll('.copy-email-btn');

    copyButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            const email = this.getAttribute('data-email');

            if (navigator.clipboard && window.isSecureContext) {
                navigator.clipboard.writeText(email).then(function() {
                    showAlert('Электронная почта скопирована в буфер обмена!', 'success');
                }, function(err) {
                    showAlert('Не удалось скопировать: ' + err, 'error');
                });
            } else {
                const tempInput = document.createElement('input');
                tempInput.value = email;
                document.body.appendChild(tempInput);
                tempInput.select();
                tempInput.setSelectionRange(0, 99999);

                try {
                    const successful = document.execCommand('copy');
                    if (successful) {
                        showAlert('Электронная почта скопирована в буфер обмена!', 'success');
                    } else {
                        showAlert('Не удалось скопировать. Пожалуйста, попробуйте вручную.', 'error');
                    }
                } catch (err) {
                    showAlert('Ошибка при копировании: ' + err, 'error');
                }

                document.body.removeChild(tempInput);
            }
        });
    });

    function showAlert(message, type) {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type === 'success' ? 'success' : 'error'}`;
        alertDiv.role = 'alert';
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="close" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        `;

        // Стили для уведомления
        alertDiv.style.padding = '15px';
        alertDiv.style.margin = '10px 0';
        alertDiv.style.border = '1px solid transparent';
        alertDiv.style.borderRadius = '4px';
        alertDiv.style.position = 'relative';
        alertDiv.style.backgroundColor = type === 'success' ? '#d4edda' : '#f8d7da';
        alertDiv.style.borderColor = type === 'success' ? '#c3e6cb' : '#f5c6cb';
        alertDiv.style.color = type === 'success' ? '#155724' : '#721c24';

        alertDiv.querySelector('.close').addEventListener('click', function() {
            alertDiv.remove();
        });

        const container = document.querySelector('.breadcrumbs');
        if (container) {
            container.insertAdjacentElement('afterend', alertDiv);
        } else {
            document.body.insertAdjacentElement('afterbegin', alertDiv);
        }

        setTimeout(function() {
            alertDiv.remove();
        }, 5000);
    }
});
