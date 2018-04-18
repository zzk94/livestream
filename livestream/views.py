from django.shortcuts import render , reverse
from livestream.models import chat as chat_model
from livestream.form import chat as chat_form
from django.http import HttpResponseRedirect,HttpResponse
from django.utils import timezone
from datetime import datetime,timedelta
from dateutil import parser
import json
last_update_time = timezone.now()

def update(request):
    global last_update_time
    date_five_min = datetime.now() - timedelta(minutes=15)
    chat_model.objects.filter(time__lt=date_five_min).delete()
    chat_model.objects.filter(username='user').delete()
    if request.method == 'GET':
        context_dict = {}
        context_dict['valid'] = False
        data = chat_model.objects.filter(time__gt=last_update_time).exclude(username=request.user.username)[::-1]

        if(len(data) > 0):
            context_dict['valid'] = True
        for i in range(0,len(data)):
            context_dict_tmp = {}
            context_dict_tmp['username'] = data[i].username
            context_dict_tmp['content'] = data[i].content
            context_dict_tmp['time'] = data[i].time
            context_dict[str(i)] = context_dict_tmp
        context_dict['length_mess'] = len(data)
        last_update_time= timezone.now()
        return HttpResponse(
                json.dumps(context_dict, indent=4, sort_keys=True, default=str),
                content_type="application/json"
        )

def index(request):
    global last_update_time
    if request.method == 'GET':
        context_dict = {}
        form = chat_form()
        data = chat_model.objects.all()

        context_dict['form'] = form
        context_dict['data'] = data[::-1]
        context_dict['username'] = request.user.username
        last_update_time = timezone.localtime()
        return render(request,'livestream/index.html',context_dict)
    else:
        # data=request.POST
        # data['username'] = request.user.username
        # print(request.POST)
        form_from_index = chat_form(request.POST)

        response_data = {}
        if form_from_index.is_valid():

            form = form_from_index.save(commit=True)
            form.username = request.user.username
            # print(form.time)
            form.time = timezone.localtime()
            form.save()

            response_data['time'] = timezone.localtime().strftime("%Y-%m-%d %H:%M:%S %z")
            response_data['content'] = form.content
            response_data['username'] = form.username

        else:
            print("error!!!")

        return HttpResponse(
                json.dumps(response_data, indent=4, sort_keys=True, default=str),
                content_type="application/json"
        )
