function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', function() {
        const itemID = this.getAttribute('data-id');
        if (confirm('Tem certeza que deseja deletar este item?')) {
            fetch(`${itemID}`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrftoken
                }
            }).then(response => {
                if(response.ok){
                    this.parentElement.parentElement.remove();
                } else {
                    alert('Erro ao deletar o item.');
                }
            });
        } 
    })
});