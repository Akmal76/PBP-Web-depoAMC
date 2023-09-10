# depoAMC

Tugas 2 - Pemrograman Berbasis Platform - Kelas D

> **depoAMC** adalah aplikasi pengelolaan penyimpanan berbagai macam bahan dan perlengkapan yang diperlukan untuk proyek konstruksi, renovasi, perbaikan, atau pembangunan properti. 

## 👷🪓🪚 **Laman** 🚜⛏️🦺🔨
https://depoamc.adaptable.app/main/

## **Implementasi Aplikasi**
* ### Membuat proyek Django
Pertama, saya membuat direktori dan menyiapkan *dependencies* pada `requirements.txt` untuk menyiapakan proyek Django.

Berikut adalah isi dari berkas `requirements.txt`.
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
Install *dependencies* tersebut dengan perintah `pip install -r requirements.txt` pada *virtual environment*. Setelah itu, proyek dibuat dengan menjalankan perintah `django-admin startproject depoAMC .` dan mengunggahnya ke repositori GitHub baru.

* ### Membuat aplikasi `main`
Pada direktori `depoAMC`, aktifkan *virtual environment* dan membuat aplikasi baru bernama `main` dengan perintah `python manage.py startapp main`. Daftarkan `main` ke dalam proyek dengan menambahkan `'main'` pada variabel `INSTALLED_APPS` yang berada di berkas `settings.py`.
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```

* ### Membuat model aplikasi `main`
Pada berkas `models.py` di direktori `main`, saya mendefinisikan model sederhana baru dengan kode berikut ini.
```python
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```
Tidak lupa untuk melakukan migrasi model dengan perintah `python manage.py makemigrations` dan menerapkannya ke *database* lokal dengan perintah `python manage.py migrate`.

* ### Membuat dan Menghubungkan Fungsi `views.py` dengan Template
Akan dilakukan *rendering* tampilan HTML dengan menggunakan data yang diberikan. Pada berkas `views.py` tambahkan `import render` dan fungsi `show_main` untuk menampilkan halaman `main.html` dengan kode dibawah ini.
```python
from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Akmal Ramadhan',
        'class': 'PBP - D'
    }

    return render(request, "main.html", context)
```
Pada `main.html`, saya meletakkan variabel yang dapat digantikan oleh data yang telah diambil dari model seperti dibawah ini.
```python
<p><b>Nama: </b>{{ name }}</p>
<p><b>Kelas: </b>{{ class }}</p>
```

* ### Melakukan *routing* aplikasi `main`
Untuk mengatur URL pada aplikasi `main`, saya membuat berkas `urls.py` pada aplikasi `main` yang berisikan kode berikut ini.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
Agar URL proyek (`depoAMC`) dapat mengimpor URL aplikasi (`main`)
, maka pada berkas `urls.py` di `depoAMC` saya tambahkan fungsi `include` dari `django.urls` dan menambahkan URL ke tampilan `main` di dalam variabel `urlpatterns`.
```python
...
from django.urls import path, include
...

urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
Dengan begitu, saya dapat melihat halaman `main` dengan perintah `python manage.py runserver` di [http://localhost:8000/main/](http://localhost:8000/main/)

* ### Melakukan *deployment* ke Adaptable
Langkah terakhir, saya melakukan *deploy* ke Adaptable dengan memilih `Python App Template` sebagai *template deployment* dan `PostgreSQL` sebagai *database type* yang akan digunakan.

## **Bagan**

## **Virtual Environment**

## **MVC, MVT, dan MVVM**

