from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .scraper import get_news
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
import csv
import datetime

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    if request.method == 'POST':
        api_key = '02fb8889dda649939204a277d49190f1'
        category = request.POST.get('category')
        search_query = request.POST.get('search_query')
        article_data = get_news(api_key, category=category,search_query=search_query)
    else:
        # Default to general category
        api_key = '02fb8889dda649939204a277d49190f1'
        category = ''
        article_data = get_news(api_key, category=category)
    export_to_csv(article_data)
    # Pass the data to the template
    return render(request, 'news.html', {'article_data': article_data, 'category': category})

def export_to_csv(article_data):
    try:
        with open('articles.csv', 'r', newline='', encoding='utf-8') as csvfile:
            fieldnames = next(csv.reader(csvfile))
            csvfile.seek(0)
            lines = csvfile.readlines()
            total_articles = len(lines) - 1  # subtract 1 for the header row
    except (FileNotFoundError, csv.Error):
        fieldnames = ['id', 'title', 'summary', 'img_url', 'source_url', 'source_name', 'created_at']
        with open('articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            total_articles = 0

    with open('articles.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        for i, article in enumerate(article_data):
            row = {'id': total_articles + i + 1}
            for fieldname in fieldnames[1:]:
                row[fieldname] = article.get(fieldname, '')
            row['created_at'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
            writer.writerow(row)







'''def export_to_csv(article_data):
    with open('articles.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'summary', 'img_url', 'source_url', 'source_name', 'created_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:  # if file is empty
            writer.writeheader()
        for i, article in enumerate(article_data):
            row = {'id': i + 1}
            for fieldname in fieldnames[1:]:
                row[fieldname] = article.get(fieldname, '')
            row['created_at'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
            writer.writerow(row)'''


'''def export_to_csv(article_data):
    with open('articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'summary', 'img_url', 'source_url', 'source_name', 'created_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i, article in enumerate(article_data):
            row = {'id': i + 1}
            for fieldname in fieldnames[1:]:
                row[fieldname] = article.get(fieldname, '')
            row['created_at'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
            writer.writerow(row)'''



'''def export_to_csv(article_data):
    with open('articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'summary', 'img_url', 'source_url', 'source_name', 'created_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i, article in enumerate(article_data):
            row = {'id': i + 1}
            for fieldname in fieldnames[1:]:
                row[fieldname] = article.get(fieldname, '')
            writer.writerow(row)'''

'''def export_to_csv(article_data):
    with open('articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'summary', 'img_url', 'source_url', 'source_name', 'created_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for article in article_data:
            row = {}
            for fieldname in fieldnames:
                row[fieldname] = article.get(fieldname, '')  # provide a default value of '' for any missing key
            writer.writerow(row)'''

'''from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .scraper import get_news
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    if request.method == 'POST':
        api_key = '867c7153fcb343d09a392e9a7548e172'
        category = request.POST.get('category')
        article_data = get_news(api_key, category=category)
    else:
        # Default to business category
        api_key = '867c7153fcb343d09a392e9a7548e172'
        category = 'business'
        article_data = get_news(api_key, category=category)

    # Pass the data to the template
    return render(request, 'news.html', {'article_data': article_data, 'category': category})'''






