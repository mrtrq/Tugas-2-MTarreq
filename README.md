Muhammad Tarreq Maulana
2106750704
PBP B
Tugas 2

Membuat sebuah README.md yang berisi link menuju aplikasi Heroku yang sudah kamu deploy serta jawaban dari beberapa pertanyaan berikut:
Link menuju aplikasi heroku: https://katalogdisplay.herokuapp.com/katalog/


Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;



Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment adalah 'tempat' yang digunakan untuk menjalankan sebuah project dengan memberikan lingkungan yang terisolasi dalam ruang lingkup yang ditentukan sehingga dependency/requirements projectnya dapat dijalankan tanpa mengganggu hal-hal lainnya. Tanpa menggunakan virtual environment, aplikasi web berbasis Django tetap bisa dijalankan karena requirements yang dibutuhkan oleh aplikasi dapat diinstall di luar virtual environment. Namun, best practice dalam membuat/mengembangkan aplikasi web adalah menggunakan virtual environment agar lingkungan pengembangan sesuai dengan kebutuhan.


Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Alur implementasinya adalah request yang masuk akan diproses melalui urls.py untuk diteruskan ke views.py. Pada views terdapat fungsi yang telah diimplentasikan untuk memproses permintaan yang masuk. Ketika terdapat operasi yang melibatkan database, views akan memanggil query ke models.py. Models.py berfungsi sebagai jembatan ke database, kemudian database akan mengembalikan hasil dari query tersebut ke views.py. Setelah request selesai diproses seluruhnya, hasilnya akan di pass ke dalam HTML yang sudah dibuat sebelumnya sebagai markup language untuk menampilkan isi konten.  Kemudian, HTML tersebut akan dikembalikan ke pengguna.

