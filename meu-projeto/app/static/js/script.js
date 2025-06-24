function confirmarExclusao(url) {
    if (confirm('Tem certeza que deseja excluir este exame?')) {
        window.location.href = url;
    }
} 