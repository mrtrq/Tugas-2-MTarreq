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

-----------------------
Tugas 5

Muhammad Tarreq Maulana - PBP B

Link menuju web aplikasi: https://katalogdisplay.herokuapp.com/todolist


**Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**

Perbedaan dari Inline, Internal, dan External CSS adalah ? 

Inline css adalah styling css yang diaplikasikan secara langsung pada bagian yang ingin disylting pada baris yang spesifik.

Internal css adalah pengaplikasian css pada isi internal dari suatu containter, biasanya container `<div>` pada sebuah file HTML.

External css adalah penggunaaan styling css dengan membuat file tersendiri untuk suatu file html yang ingin di styling. Misalkan kita mempunyai file todolit.html, maka untuk melakukan styling css dengan cakupan seluruh file html tersebut, bisa dibuat file todolist.css untuk kemudian diisi dengan syling dan customization pada halaman html tersebut.


Apa saja kelebihan dan kekurangan dari masing-masing style?


**Jelaskan tag HTML5 yang kamu ketahui.**
Beberapa tag HTML 5 yang saya ketahui adalah 

`<!--...-->`	digunakan untuk commenting

`<!DOCTYPE>`	menunjukkan tipe the document

`<div>` sebagai container untuk tag tag lainnya seperti title, heading atau paragraf

`<p>` container untuk teks dengan ukuran yang panjang

`<h5>` bagian dari isi konten

`<abbr>`	untuk abbreviation (singkatan)


**Jelaskan tipe-tipe CSS selector yang kamu ketahui.**
Tipe-tipe CSS selector yang saya ketahui adalah:

.class, digunakan untuk menambahkan styling css ke elemen dengan nama class yang sama

#id, digunakan untuk styling kepada bagian dengan nama id yang sama 
*, untuk semua elemen

.class1.class2, digunakan untuk memilih elemen dalam class dengan nama yang sama