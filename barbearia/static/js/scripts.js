// Funções JavaScript adicionais podem ser adicionadas aqui
document.addEventListener('DOMContentLoaded', function() {
  // Inicializa tooltips
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl);
  });
});