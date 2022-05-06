from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .models import Message
from .forms import SendMessage
from django.contrib import messages


# Create your views here.
class MessageView(CreateView):
    msg_form = SendMessage
    success_url = reverse_lazy('web_message_home')
    template_name = 'web_messaging/send_messenger.html'

    def get(self, request, *args, **kwargs):
        message_form = SendMessage()
        return render(request, self.template_name, {'msg':message_form})

    def post(self, request, *args, **kwargs):
        msg_form = SendMessage(request.POST)
        receiver = msg_form.cleaned_data.get('receiver')
        msg_body = msg_for.cleaned_data.get('body')
        Message.objects.create(sender=request.user.username, receiver=receiver, msg_body=msg_body)
        messages.success(request, f'Message sent to {receiver}')
        return render(request, self.template_name, {'msg_form': msg_form})
