from django.shortcuts import render
from .vigenere import encrypt, decrypt

def vigenere_form(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        key = request.POST.get('key')
        encrypted_text = encrypt(message, key)
        decrypted_text = decrypt(encrypted_text, key)
        return render(request, 'result.html', {'encrypted_text': encrypted_text, 'decrypted_text': decrypted_text})
    return render(request, 'form.html')

