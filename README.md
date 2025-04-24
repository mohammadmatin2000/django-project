# 📰 Django-Project

This project is a dynamic news portal web application built with **Django** and styled using **Bootstrap** and **Owl Carousel**. It utilizes a clean, responsive HTML5 template originally designed by [FreeHTML5.co](https://freehtml5.co).

## 🌐 Live Preview

> [View Demo](#) – *(Insert link if hosted)*

## 📁 Project Structure

- **index.html** – Homepage template showing featured articles, trending topics, and news sliders.
- **Django Template Tags** – Custom tags like `{% tags %}`, `{% popular %}`, and `{% blog_tags %}` for dynamic rendering.
- **Static Files** – CSS, JS, images handled using Django’s `{% static %}` template tag.

## 🚀 Features

- Dynamic display of featured news articles.
- Trending & video news carousels.
- Pagination for news articles.
- Article previews with titles, publish dates, and author info.
- Mobile-friendly responsive layout.
- Integrated YouTube video embedding.

## 🔧 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/24-news-portal.git
   cd 24-news-portal
   ```
   
   ```bash
   pip install -r requirements.txt
   ```
   
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
   
   ```bash
   http://127.0.0.1:8000/
   ```

  
