# depoAMC

Tugas 2 - Pemrograman Berbasis Platform - Kelas D

> **depoAMC** adalah aplikasi pengelolaan penyimpanan berbagai macam bahan dan perlengkapan yang diperlukan untuk proyek konstruksi, renovasi, perbaikan, atau pembangunan properti. 

## 👷🪓🪚 **Laman** 🚜⛏️🦺🔨
https://depoamc.adaptable.app/main/

## **Implementasi Aplikasi**
* ### Membuat proyek Django
Pertama, saya membuat direktori dan menyiapkan *dependencies* pada `requirements.txt` untuk menyiapkan proyek Django.

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
Model adalah bagian yang berhubungan dengan _database_. Pada berkas `models.py` di direktori `main`, saya mendefinisikan model sederhana baru dengan kode berikut ini.
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
Langkah terakhir, saya melakukan *deploy* ke Adaptable dengan memilih `Python App Template` sebagai *template deployment* dan `PostgreSQL` sebagai *database type* yang akan digunakan. Pilih versi Python dengan versi lokal dan masukan _command_ `python manage.py && gunicorn DepoAMC.wsgi` pada `Start Command`.

## **Bagan**
![](image/bagan.jpg)

Ketika *web browser* menerima permintaan HTTP aplikasi `main` dari pengguna, terjadi URL *mapping* oleh `urls.py`. Setelah _mapping_ selesai dan ditemukan, fungsi pada `views.py` dipanggil sesuai dengan permintaan URL nya. Setelah itu, HTTP *request* ini akan dikembalikan oleh *view* menjadi HTTP *response* berupa HTML *page*. Dalam pengembalian ini, `views.py` akan mengakses data yang dibutuhkan dari `models.py` dan data tersebut ditampilkan menggunakan template `main.html`.

## **Virtual Environment**
Virtual Environment digunakan untuk memisahkan *packages* dan *dependencies* yang berbeda antar proyek dalam satu perangkat yang sama. Misalkan ketika ada dua proyek yang menggunakan versi Python yang berbeda. Dengan _virtual environment_, versi yang berbeda ini tidak saling mempengaruhi kedua proyek satu sama lain.

Kita bisa saja membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*. Akan tetapi, dapat terjadi risiko konflik *dependencies* antar satu proyek dengan proyek lainnya sehingga proyek yang bangun akan menjadi kacau.

## **MVC, MVT, dan MVVM**
Django menggunakan pola arsitektur MVT (Model-View-Template). Terdapat pola-pola lain seperti MVC dan MVVM.

Model: Mengelola data.

View:  Menerima input dan menampilkan informasi kepada pengguna.

#### 1. MVC (Model-View-Controller)
![Sumber: GeeksforGeeks](https://media.geeksforgeeks.org/wp-content/uploads/20201002214740/MVCSchema.png)

Controller: Berinteraksi dengan menghubungkan Model dan View sebagai pengatur *app flow* dan pengelola permintaan pengguna.

#### 2. MVT (Model-View-Template)
![Sumber: javaTpoint](https://www.javatpoint.com/django/images/django-mvt-based-control-flow.png)

Template: Mengatur tampilan HTML dan menggunakan data dari Model.

#### 3. MVVM (Model-View-Viewmodel)
![Sumber: GeeksforGeeks](https://media.geeksforgeeks.org/wp-content/uploads/20201002215007/MVVMSchema.png)

Viewmodel: Mengelola interaksi dan penghubung antara Model dan View serta mengubah data dari Model ke format yang dapat ditampilkan oleh View.

Perbedaan ketiga pola ini yaitu:

|                                          MVC                                          |                                               MVT                                                |                                                                          MVVM                                                                           |
|:-------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                            Input diterima oleh Controller                             |                                     Input diterima oleh View                                     |                                                                Input diterima oleh View                                                                 |
|                       View dan Controller berelasi many-to-many                       |                              View dan Template berelasi one-to-one                               |                                                         View dan Viewmodel berelasi one-to-many                                                         |
| View tidak memiliki referensi ke Controller (panah satu arah dari Controller ke View) | View menyimpan referensi ke Template dan Template bekerja jika dipicu dari View (panah dua arah) | View tidak memiliki referensi ke Model dan sebaliknya. Viewmodel lah yang bertugas menghubungkan View dan Model. Dari sinilah nama Viewmodel digunakan. |

## Referensi
GeeksforGeeks: [Difference Between MVC, MVP and MVVM Architecture Pattern in Android](https://www.geeksforgeeks.org/difference-between-mvc-mvp-and-mvvm-architecture-pattern-in-android/)

Tomy's Blog: [MVC, MVP and MVVM](https://tomyrhymond.wordpress.com/2011/09/16/mvc-mvp-and-mvvm/)

javaTpoint: [Django MVT](https://www.javatpoint.com/django-mvt)