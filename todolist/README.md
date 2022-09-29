Tugas 4
Muhammad Tarreq Maulana - PBP B
Link menuju web aplikasi: https://katalogdisplay.herokuapp.com/todolist

**Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?**

{% csrf_token %} pada elemen "form" adalah Cross Site Request Forgery adalah proteksi yang digunakan unntuk menghindari CSRF attack sehingga keamanan dari user yang melakukan request ke web aplikasi dapat terjamin dengan menambahkan 1 baris syntax tersebut.

**Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?**

kita dapat membuat elemen form secara manual tanpa menggunakan generator seperti {{ form.as_table }} karena ada implementasi lain untuk membuat form tanpa menggunakan {{form.as.table}} sebagai generatornya

**Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**
Alur data dari submisi yang dilakukan oleh pengguna terjadi ketika pengguna memberikan informasi contohnya ketika register, login, dan menambahkan task. Sebelum pengguna bisa login,  pertama-tama pengguna harus melakukan registrasi akun terlebih dahulu dengan mengisi HTML form dengan membuat username dan password, yang kemudian akan disimpan di database secara cukup aman karena sudah ada proteksi dari Cross Site Request Forgery yang digunakan untuk meningkatkan keamanan data user ketika melakukan request ke web aplikasi. Kemudian, ketika pengguna menambahkan todolist, pengguna juga diminta untuk mengisi form terkait judul dan deskripsi tugas yang ingin ditambahkan. Ketika melihat apa saja tugas yang ada/sudah ditambahkan, request ke database dilakukan untuk kemudian dikembalikan file html yang dapat ditampilkan ke pengguna

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
Langkah pertama dalam implementasi checklist di atas adalah melakukan start app baru yang akan membuat folder baru yang berisi beberapa file untuk kemudian diimplementasi. Kita perlu membuat sebuah class pada models.py yang berisi variabel apa saja dan jenisnya yang akan ada pada web aplikasi, setelah membuat model, perlu dilakukan makemigrations dan migrate untuk mengirim informasi models tersebut ke django. Kemudian, kita membuat serangkaian fungsi pada views.py untuk melakukan operasi-operasi seperti login, logout, tambah todolist, update status, dan hapus todolist. Setelah itu, perlu juga dilakukan implementasi 'jalur' pada urls.py. Jalur di urls.py akan memanggil fungsi yang bersesuaian pada views.py, dan untuk menampilkan isi konten ke user, perlu dibuat file-file html pada folder templates yang berisikan iterasi dan tampilan fungsi dari models.py dan views.py yang sudah dibuat

