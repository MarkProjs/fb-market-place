from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
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
        return render(request, self.template_name, {'msg': message_form})

    def post(self, request, *args, **kwargs):
        msg_form = SendMessage(request.POST)
        if msg_form.is_valid():
            receiver_name = msg_form.cleaned_data.get('receiver')
            receiver = User.objects.get(username=receiver_name)
            msg_body = msg_form.cleaned_data.get('message')
            Message.objects.create(sender=request.user, receiver=receiver, message=msg_body)
            messages.success(request, f'Message sent to {receiver}')
        return render(request, self.template_name, {'msg_form': msg_form})


def inbox(request):
    context = {
        'view_message': Message.objects.all().filter(receiver__username__contains=request.user)
    }
    return render(request, 'web_messaging/inbox.html', context)
# class MessageListView(ListView):
#     model = Message
#     template_name = 'web_messaging/inbox.html'


