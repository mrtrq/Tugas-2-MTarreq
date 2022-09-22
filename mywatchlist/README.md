**Jelaskan perbedaan antara JSON, XML, dan HTML!**

JSON(JavaScript Object Notation) adalah format/bentuk data dan merupakan 'turunan' dari bahasa JavaScript. JSON bersifat sebagai bahasa yang idependen untuk menampilkan data. Objektif dari JSON pada awalnya adalah untuk menyimpan data secara terstruktur sehingga bisa digunakan JavaScript. Saat ini, JSON menjadi populer dan digunakan di berbagai aplikasi contohnya megirim data untuk web API.
XML(Extensible Markup Language) adalah bahasa yang mempunyai tujuan untuk menyimpan data dengan mengedepankan ***simplicity & usability***, bukan untuk menampilkannya, sementara HTML(Hypertext Markup Language) adalah bahasa ***markup*** yang digunakan untuk menyusun struktur web dan menampilkan kontennya. Terdapat fitur untuk menampilkan konten menggunakan tag sebagai elemennya, dan karakter dalam tag sebagai kontennya.

reference: https://www.geeksforgeeks.org/difference-between-json-and-xml/

***Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?***

Kita memerlukan ***data delivery*** dalam mengimplementasi platform karena jika data disimpan pada file yang sama dengan file yang mengatur susunan halaman/layout/tampilan pada platform, kode akan menjadi tidak beraturan dan tercampur, dan seiring data menjadi semakin besar, kebutuhan untuk sebuah ***data delivery*** menjadi penting sehingga data dapat dibawa dalam sebuah paket file. Jadi, dibutuhkan suatu medium yang dapat diandalkan untuk membuat, menyimpan dan mengantarkan data tersebut secara aman dan fungsional.

***Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas***

Cara saya mengimplementasi checklist pada tugas ini adalah dengan langkah-langkah berikut:
1. Membuat project baru dengan nama mywatchlist, kemudian membuat class pada models.py untuk mendefinisikan nama variabel dan jenis tipe data yang akan digunakan
2. Menambahkan aplikasi tersebut ke INSTALLED_APPS di settings.py pada folder project_django
3. Menambahkan jalur url ke mywatchlist pada urls.py pada project_django untuk 'reroute' jalur ke folder mywatchlist
4. Membuat file html, file json berisi data yang akan ditampilkan, dan fungsi pada views.py dan menambahkan jalur menuju link yang menampilan data dengan format xml/json di urls.py
5. Membuat tests.py yang mengembalikan respon HTTP 200 OK dan mendeploy app ke heroku agar dapat diakses secara publik


**Screenshot postman**

html:
<img width="1440" alt="html" src="https://user-images.githubusercontent.com/69755166/191655641-73edfb0c-9a52-4a83-89e8-cb41989ac08a.png">

xml:
<img width="1440" alt="xml" src="https://user-images.githubusercontent.com/69755166/191655719-d923996a-84df-4184-8b87-c1cf4c2e0197.png">

json:
<img width="1440" alt="json" src="https://user-images.githubusercontent.com/69755166/191655786-ed8c2e69-1042-4039-a094-a2f343da70d6.png">
