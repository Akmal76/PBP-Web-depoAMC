# depoAMC

**Tugas 3 - Pemrograman Berbasis Platform - Kelas D**

> **depoAMC** adalah aplikasi pengelolaan penyimpanan berbagai macam bahan dan perlengkapan yang diperlukan untuk proyek konstruksi, renovasi, perbaikan, atau pembangunan properti. 

## Perbedaan antara form `POST` dan form `GET` dalam Django
*Form* adalah cara untuk mengambil data dari pengguna. Data tersebut bisa berupa teks maupun *file*. Terdapat dua metode dalam mengirimkan data dari *browser user* yaitu `POST` dan `GET`.

| Perbedaan | `POST` | `GET` |
|:--:|--|--|
|**Tujuan**| Mengambil data dari Django. | Mengirim data ke Django. |
|**Penggunaan**| Melakukan pencarian atau menampilkan data. | Membuat, memperbarui, atau menghapus data. |
|**Cara Kerja**| Ketika pengguna mengisi form GET dan mengirimkannya, data yang dimasukkan ke dalam form akan muncul di URL. | Ketika pengguna mengisi form POST dan mengirimkannya, data yang dimasukkan ke dalam form dikirim sebagai bagian dari permintaan HTTP ke server, tetapi tidak muncul di URL |

## Perbedaan Utama antara XML, JSON, dan HTML dalam Konteks Pengiriman Data
| XML | JSON | HTML |
|--|--|--|
| Digunakan dalam pertukaran data antara sistem yang berbeda dan perlu menggambarkan data yang kompleks dan terstruktur dengan baik | Digunakan dalam pengembangan aplikasi web karena mudah dibaca oleh manusia dan mudah digunakan oleh bahasa pemrograman modern | Digunakan untuk membuat konten web dan menjadikannya dapat diakses oleh *browser* web |

## JSON sebagai Pertukaran Data antara Aplikasi Web Modern
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena kelebihan berikut:
1. Format sintaks ringkas, sederhana, dan mudah dibaca.
2. Didukung oleh banyak bahasa pemrograman sehingga cocok untuk *development* aplikasi web.

## Implementasi *Data Delivery*
### Membuat input `form`
Untuk mendapatkan data baru yang ingin ditampilkan, maka dapat dibuat `form` untuk menerima input.

1. Pertama, membuat berkas `forms.py` pada direktori `main` dan tambahkan kode berikut ini.

```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```

2. Kedua, ubahlah fungsi `show_main` pada `views.py` dengan kode berikut ini.
```python
def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Akmal Ramadhan',
        'class': 'PBP - D',
        'items': items,
    }

    return render(request, "main.html", context)
```

### Menambahkan fungsi pada `views`
Kita bisa melihat atau mengembalikan data yang telah dimasukkan melalui `form`. 

#### Format HTML

1. Untuk menerima data, akan dibuat fungsi baru bernama `create_item` pada `views.py` seperti pada kode berikut ini.
```python
from main.forms import Item

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```

2. Membuat *template* baru untuk tampilan dalam menambahkan *item* baru dengan nama `create_item.html` pada direktori `main/templates`.
```python
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

3. Tampilkan data *item* dalam bentuk tabel dan tambahkan tombol `Add New Item` pada `main.html`.
```python
<table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
        </tr>
    
        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.description}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>
```

---

Untuk format XML dan JSON, saya akan menambahkan *import* `HttpResponse` dan `serializers` pada `views.py` di folder `main`.

#### Format XML
Tambahkan fungsi `show_xml` yang me-*return* `HttpResponse` berisi data yang sudah di-*serialize* menjadi XML.

```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

#### Format JSON
Tambahkan fungsi `show_json` yang me-*return* `HttpResponse` berisi data yang sudah di-*serialize* menjadi JSON.

```python
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

---

Untuk format XML dan JSON *by* ID, dalam pengambilan hasil *query* tambahkan *filter* dengan ID tertentu saja.

### Format XML *by* ID
```python
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

## Format JSON *by* ID
```python
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
---

### Membuat routing URL
Tambahkan kelima *path url* fungsi diatas ke dalam `urlpatterns` pada `urls.py` di folder `main`. Tidak lupa untuk meng-*import*-nya dari `views.py`.

```python
from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),  
]
```

Dengan begitu, input `form` sudah selesai dibuat dan siap digunakan. Jalankan *command* `python manage.py runserver` dan kunjungi <http://localhost:8000>.

## Postman *Screenshot*
Berikut adalah tangkapan layar hasil akses URL melalui Postman untuk tiap kelima URL.
1. HTML
![HTML](image/postman_html.png)
2. XML
![XML](image/postman_xml.png)
3. JSON
![JSON](image/postman_json.png)
4. XML *by* ID
![XML *by* ID](image/postman_xml_1.png)
5. JSON *by* ID
![JSON *by* ID](image/postman_json_1.png)

## Arsip
* [Tugas 2](archive/tugas2.md)