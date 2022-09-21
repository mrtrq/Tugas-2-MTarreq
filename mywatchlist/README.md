**Jelaskan perbedaan antara JSON, XML, dan HTML!**

JSON(JavaScript Object Notation) adalah format/bentuk data dan merupakan 'turunan' dari bahasa JavaScript. JSON bersifat sebagai bahasa yang idependen untuk menampilkan data. Objektif dari JSON pada awalnya adalah untuk menyimpan data secara terstruktur sehingga bisa digunakan JavaScript. Saat ini, JSON menjadi populer dan digunakan di berbagai aplikasi contohnya megirim data untuk web API.
XML(Extensible Markup Language) adalah bahasa yang mempunyai tujuan untuk menyimpan data dengan mengedepankan ***simplicity & usability***, bukan untuk menampilkannya, sementara HTML(Hypertext Markup Language) adalah bahasa ***markup*** yang digunakan untuk menyusun struktur web dan menampilkan kontennya. Terdapat fitur untuk menampilkan konten menggunakan tag sebagai elemennya, dan karakter dalam tag sebagai kontennya.

***Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?***

Kita memerlukan ***data delivery*** karena dalam mengimplementasi platform, jika file data menjadi satu dengan file yang mengatur susunan halaman pada platform, kode akan menjadi tidak efisien seiring data menjadi semakin besar sehingga untuk membawa data untuk ditampilkan tersebut dibutuhkan suatu medium untuk membuat menyimpan dan mengantarkan data tersebut secara aman dan fungsional.

***Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas***

Cara saya mengimplementasi checklist pada tugas ini adalah dengan langkah-langkah berikut:
1. Membuat project baru dengan nama mywatchlist, kemudian membuat class pada models.py untuk mendefinisikan nama variabel dan jenis tipe data yang akan digunakan
2. Menambahkan aplikasi tersebut ke INSTALLED_APPS di settings.py pada folder project_django
3. Menambahkan jalur url ke mywatchlist pada urls.py pada project_django untuk 'reroute' jalur ke folder mywatchlist
4. Membuat file html, file json berisi data yang akan ditampilkan, dan fungsi pada views.py dan menambahkan jalur menuju link yang menampilan data dengan format xml/json di urls.py
5. Membuat tests.py dan mendeploy app ke heroku agar dapat diakses secara publik