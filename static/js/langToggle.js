document.addEventListener('DOMContentLoaded', function() {
    var checkbox = document.querySelector('#language-toggle');
    checkbox.addEventListener('change', function() {
        var checked = this.checked;
        toggleLanguage(checked ? 'en' : 'it');
    });

    // Inizializza la lingua in base alla posizione del toggle all'avvio
    toggleLanguage(checkbox.checked ? 'en' : 'it');
});

function toggleLanguage(lang) {
    // Nascondi tutti i contenuti per la lingua non selezionata
    var langElements = document.querySelectorAll('.form-name, .control-label, p, .form2-name, input, .send_button');
    langElements.forEach(function(element) {
        if (element.id.indexOf(lang) === -1) {
            element.style.display = 'none';
        } else {
            element.style.display = 'block';
        }
    });
}
