function submitForm() {
    const form = document.getElementById("contactForm");
    form.submit();
}

// Set the value of the hidden input in the message form to the selected contact
document.querySelectorAll('input[name="chat_friend"]').forEach((element) => {
element.addEventListener('click', function() {
    document.getElementById('chat_friend_input').value = this.value;
});
});

function checkEmpty() {
    const message = document.getElementById("message_input").value.trim();
    if (message === '') {
        alert('You cannot enter only spaces');
        return false;
    }
    return true;
}