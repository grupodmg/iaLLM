const chatContainer = document.getElementById('chat-container');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');

function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    const bubble = document.createElement('div');
    bubble.className = `bubble ${sender}`;
    bubble.textContent = text;
    messageDiv.appendChild(bubble);
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = userInput.value.trim();
    if (!message) return;
    addMessage(message, 'user');
    userInput.value = '';
    addMessage('Optimus Prime está pensando...', 'ai');
    try {
        const response = await fetch('http://127.0.0.1:8000/ai-chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });
        const data = await response.json();
        // Elimina el mensaje de "pensando"
        chatContainer.removeChild(chatContainer.lastChild);
        addMessage(data.response || 'Respuesta no disponible.', 'ai');
    } catch (err) {
        chatContainer.removeChild(chatContainer.lastChild);
        addMessage('Error al conectar con Cybertron. Intenta de nuevo.', 'ai');
    }
});
