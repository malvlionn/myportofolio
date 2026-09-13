Nama : Malvin Lionard

NPM : 2506591753

Kelas : PBP F

### Tugas 1

1. Ya, saya menggunakan beberapa dari elemen semantik HTML5 tersebut, yaitu:
- `<section>` untuk membagi section/seksi utamanya, misalnya profile, awards, dan education
- `<article>` untuk membungkus/wrap setiap bagian tersendiri, misalnya cards pada section Awards, cards untuk Academic Journey, dan Research Project. Alasannya adalah karena setiap bagiannya independen dan bisa dipisahkan/didistribusikan masing-masing.
- Di dalam setiap `<article>`, saya menggunakan `<header>` untuk menampung bagian-bagian judul, lalu `<time datetime="...">` sebagai representasi waktu. Selain itu, screenshot dari research project dibungkus dalam `<figure>` dan `<figcaption>`. Dengan begini, accessibility tree menjadi lebih jelas, navigasi landmark bagi pengguna juga lebih jelas, memaksimalkan algoritma mesin pencari atau SEO, dan mencegah penulisan yang terlalu berantakan/menumpuk.

2. Tantangan tata letak yang saya alami ketika mengatur responsiveness CSS adalah:
- Ketika saya membuat halaman/tampilan untuk bagian Awards, terutama pada penyusunan cardsnya. Jika menggunakan desktop view, kartunya akan terlihat atas-bawah bergantian melewati bagian tengah dengan grid 3x2. Akan tetapi, ketika saya mencoba untuk mengecilkan ukurannya ke ukuran HP, lebarnya menjadi terbatas, garisnya sempat memotong kartu, dan layoutnya menjadi rentan mengalami horizontal overflow.
- Untuk bagian Education, bagian card untuk Universitas Indonesia pada awalnya dirancang agar teksnya rata kanan/mirror dengan bagian Kolese Kanisius. Walaupun begitu, ketika dicek dengan ukuran HP, saya merasa kurang nyaman dan readabilitynya menjadi kurang bagus.

Untuk proses evaluasinya, pada bagian breakpoint mobile, tata letak untuk multikolomnya saya ubah agar menjadi tumpukan satu kolom saja/Flexbox vertikal. Lalu, sumbu di bagian Awards diubah dari yang awalnya garis horizontal di tengah menjadi garis vertikal di kiri, lalu garis konektor yang muncul di desktop dimatikan. Teks di bagian card UI juga dibuat ke kiri dan posisi logonya disesuaikan dengan card Kolese Kanisius agar lebih enak dibaca di HP. Terakhir, untuk tampilan di HP, elemen-elemen dekorasinya saya sederhanakan dan ukuran-ukurannya disesuaikan agar tetap mudah dibaca, dan ramah touchscreen.

3. Pastinya ada beberapa batasan karena webnya masih static web, yaitu konten atau isi dari websitenya masih kaku/hardcoded. Akibatnya, kalau saya ingin mengganti data tersebut, saya harus mengubah file htmlnya secara manual, melakukan commit lagi, dan melakukan push. Selain itu, orang yang membuka web saya tidak dapat berinteraksi secara aktif. Terakhir, batasan yang saya rasakan adalah struktur visualnya, baik di html maupun css, masih tercampur dengan data portofolionya. Untuk ke depannya, fungsionalitas dinamis yang saya ingin pelajari dan persiapkan adalah:
- Model-Driven Architecture, yaitu dengan membangun skema database relasional untuk bagian Education dan Awards yang menyimpan atribut-atribut spesifiknya.
- Dynamic Rendering lewat DTL (Django Template Language), yang menggantikan duplikasi tag-tag statis dengan menggunakan {% for loop %}, agar file htmlnya menjadi lebih ringkas.
- Content Management System, yang membantu melakukan CRUD (Create, Read, Update, Delete) pada portofolio secara cepat dan aman.
- Query Filtering dan Sorting, untuk menghubungkan URL dengan query ORM agar pengunjung bisa berinteraksi dengan web.

---

### AI Disclosure & Critical Reflection

* **Model/Tools yang Digunakan:** Google Gemini (Advanced/Flash)

---

#### 1. Cakupan Penggunaan & Contoh Prompt Reflektif

Saya memanfaatkan AI bukan untuk menghasilkan kode secara mentah dan instan tanpa pemahaman, melainkan sebagai rekan diskusi untuk membedah konsep arsitektur HTML, alur kerja Git, serta mendiagnosis kesalahan (*debugging/troubleshooting*) tata letak CSS.

Beberapa contoh interaksi spesifik yang berfokus pada konsep dan pemecahan masalah:

1. **Evaluasi Struktur Semantik & Rubrik Penilaian:**
> *"pada langkah 1, itu banyak div yang keliatannya menumpuk itu sebenernya gapapa kah? gimana cara untuk mempersingkat dan mengoptimalkan div bertumpuk ini?"*


* **Tujuan:** Menguji apakah rancangan awal markup berpotensi memicu *div soup* dan memastikan struktur dokumen benar-benar memanfaatkan elemen semantik HTML5 seperti `<article>`, `<header>`, dan `<time>` agar sesuai standar penilaian.


2. **Pemahaman Logika Git & Best Practice Version Control:**
> *"jelaskan konsep git add dan commit, terutama untuk bagian branching dan conventional commitsnya."*


* **Tujuan:** Memahami perbedaan mendasar antara men-stage berkas secara selektif per fitur (*atomic commit*) dibandingkan men-stage seluruh direktori kerja, kapan waktu yang tepat mengikutsertakan aset gambar baru bersamaan dengan berkas HTML, memahami cara kerja branching di GitHub commits, serta aturan penulisan conventional commits.


3. **Diferensiasi Environment Remote Git (Origin vs PWS):**
> *"jelaskan perbedaan antara push origin dan push pws, lalu jelaskan juga kondisi-kondisi ketika kita melakukan keduanya jika berada dalam suatu branch tertentu."*


* **Tujuan:** Memahami perbedaan peran arsitektur antara remote repository kolaboratif/versi kode (origin di GitHub) dengan server live deployment (pws), serta memahami alur bahwa branch fitur yang belum matang tidak boleh langsung dikirim ke server produksi PWS.


4. **Penyesuaian Hierarki Visual dan Aksentuasi:**
> *"gimana konsep styling di css untuk atribut dari bordernya, bagian yang mana yang perlu saya tambahkan/ubah?"*


* **Tujuan:** Mengetahui *selector* CSS yang tepat untuk memberikan pembeda visual (*gold border*) khusus pada kartu pencapaian juara pertama tanpa merusak efek transisi kartu lainnya.

---

#### 2. Analisis Kritis Keterbatasan AI & Intervensi Mandiri

* **Mendeteksi dan Memangkas *Div Soup*:**
Pada beberapa rekomendasi kode awal, AI cenderung membuat pembungkus `<div>` berlapis demi kemudahan Flexbox. Saya menyadari hal ini dan mengarahkan ulang agar elemen-elemen tersebut digantikan oleh tag semantik HTML5 (`<header>`, `<figure>`, `<time>`, `<article>`) agar sesuai dengan rubrik.
* **Mengoreksi Formula CSS yang Rapuh:**
Solusi awal AI menggunakan pendekatan *padding* kaku (`calc(260px + 12px)`) untuk membagi posisi atas-bawah section Awards. Pendekatan ini ketika saya coba malah menyebabkan kartu bertabrakan saat tinggi konten berubah. Saya kemudian merombak sistemnya menggunakan **CSS Grid 2-Baris (`1fr 1fr`)** agar sumbu timeline otomatis terkunci di 50%.
* **Menyelesaikan *Class Mismatch* Secara Mandiri:**
Ketika layout timeline sempat patah, AI mengabaikan inkonsistensi penamaan (HTML menggunakan `horizontal-timeline`, sedangkan CSS menargetkan `.timeline-horizontal`). Saya merevisi nama kelas tersebut, serta memastikan seluruh *media query* untuk layar seluler (< 600px) bertransisi mulus dari alur zig-zag ke timeline yang vertikal satu kolom tanpa menimbulkan *horizontal scrolling*.


### Tugas 2

1. Alur yang terjadi ketika pengguna membuka halaman portofolio baru saya adalah:
- Penerimaan permintaan atau request handling, yaitu ketika pengguna memilih section "Awards" di navbar, permintaan HTTP GET akan dikirim ke server. Lalu, konfigurasi rute utama, yaitu (portofolio/urls.py) menerima permintaan itu dan mengecek bahwa permintaan ini akan ditangani oleh berkas routing aplikasi main.
- Berkas main/urls.py akan mencocokkan path awards/ dengan pola routing yang udah didaftarkan. Nantinya, Django memanggil fungsi show_awards.
- Fungsi view show_awards(request) akan dieksekusi. View ini bertindak sebagai perantara yang bertugas menyiapkan data dengan memanggil QuerySet dari model Award lewat Django ORM.
- Model Award menerjemahkan pemanggilan Award.objects.all() menjadi kueri SQL ke database SQLite lokal. Setelah itu, database akan mengembalikan rekaman data prestasi yang tersimpan, dan mengemasnya dalam bentuk objek Python ke dalam view.
- View akan memasukkan daftar objek tersebut ke kamus context dengan kunci award_list. Fungsi render() akan menggabungkan data context dengan template awards.html. Django Template Language (DTL) memproses perulangan {% for %}, mengecek kondisi {% if %}, atau menampilkan pesan alternatif di bagian {% empty %} kalau datanya kosong.
- Hasil kompilasi template yang bentuknya sudah berupa file HTML statis akan dikirimkan kembali oleh web server ke browser pengguna sebagai HTTP Response dengan kode status "200 OK" untuk ditampilkan ke layar.

2. Menyimpan data portofolio yang baru di dalam model jauh lebih baik daripada menuliskannya secara langsung di dalam template HTML karena:
- Struktur kode akan menjadi lebih bersih karena tanggung jawabnya dipisah dengan jelas. Berkas template HTML murni berfungsi untuk mengatur tampilan visual dan tata letak, lalu untuk urusan data, skema, dan tipe data akan dikelola sepenuhnya oleh model. Hal ini menjawab batasan yang sempat dijelaskan di Tugas 1, yaitu visual dan datanya masih kaku.
- Ketika saya ingin menambahkan data baru atau mengubah data yang sebelumnya ada, saya hanya perlu memodifikasi lewat database tanpa perlu membuka kode HTML sama sekali sehingga saya tidak perlu membuka file HTML, mengubah secara manual, dan melakukan commit serta push lagi.
- Django Model menyediakan validasi tipe data bawaan yang ketat, contohnya UUIDField, CharField, BooleanField, maupun URLField. Hal ini membantu mencegah terjadinya human error dalam pemformatan data daripada penulisan secara manual di HTML.
- Data di dalam model bisa diubah dengan mudah lewat fitur Django ORM, misalnya pengurutan otomatis berdasarkan tanggal yang paling baru, pemfilteran, pencarian, sampai kemudahan jika akan disajikan dalam bentuk API/JSON tanpa mengubah struktur template.

3. Perbedaan fungsi makemigrations dengan migrate pada Django adalah makemigration berfungsi untuk mengecek perubahan yang terjadi di file models.py. Command ini hanya bertugas untuk menyusun berkas rancangan migrasi dalam bentuk script Python di folder migrations/, tapi perubahan ke database belum diterapkan. Di sisi lain, migrate berfungsi untuk mengeksekusi instruksi yang ada di file migrasi yang belum dijalankan ke database. Perintah ini akan menjalankan operasi DDL SQL, misalnya CREATE TABLE, dan mencatat riwayat eksekusi di tabel internal django_migrations. Contoh perubahan model yang mengharuskan saya menjalankan perintah kedua model tersebut adalah ketika saya membuat model Award di dalam models.py. Saya menjalankan instruksi makemigrations agar Django membuat file migrasi baru yang menjelaskan skema tabel main_award dan kolomnya, lalu juga menjalankan instruksi migrate agar tabel-tabel yang tadi sudah dibuat oleh instruksi makemigrations benar-benar dibuat di dalam file SQLite.

---

### AI Disclosure & Critical Reflection

* **Model/Tools yang Digunakan:** Google Gemini

---

#### 1. Cakupan Penggunaan & Contoh Prompt Reflektif

Saya memanfaatkan AI bukan untuk menghasilkan kode secara instan tanpa pemahaman, melainkan sebagai rekan diskusi untuk membedah arsitektur Model-View-Template (MVT), menyusun skenario unit test, serta memastikan kepatuhan alur kerja *version control* terhadap *best practices*[cite: 6].

Beberapa contoh interaksi spesifik yang berfokus pada konsep dan pemecahan masalah:

1. **Pemindahan Komponen Statis ke Model MVT:**
> *"Kalau bagian Awards di halaman utama mau saya pisah jadi halaman tersendiri pakai pola MVT, rancangan modelnya yang pas gimana ya biar styling kartu dan highlight juaranya tetap sinkron sama CSS yang udah ada?"*[cite: 2, 5]
* **Tujuan:** Menentukan atribut dan tipe data yang tepat untuk model `Award` (seperti field boolean untuk status juara dan tanggal) agar data dinamis dari database dapat langsung dipetakan ke struktur layout CSS yang sudah ada[cite: 2, 5].

2. **Pengaturan Alur dan Batasan Commit Git:**
> *"Bantu breakdown alur commit Git yang ideal untuk tugas MVT ini dong. File apa aja yang perlu di-stage duluan dan kapan momen yang tepat buat commit biar riwayatnya rapi bertahap dan gak numpuk di akhir?"*
* **Tujuan:** Memahami penerapan *atomic commit* dengan memisahkan progres kerja per lapisan fungsional (migrasi model &rarr; views dan urls &rarr; template dan navigasi &rarr; pengujian unit test)[cite: 3, 4, 6].

3. **Koreksi dan Penyelamatan Histori Commit:**
> *"Kalau ada file yang ketinggalan atau ada kode yang salah di commit terakhir lokal, gimana cara benerinnya tanpa bikin riwayat Git berantakan? Kapan kita pakai git commit --amend dibanding git reset?"*
* **Tujuan:** Mengetahui cara memperbaiki kesalahan commit lokal secara bersih sebelum dipush ke remote repository, serta menghindari risiko deployment error di server PWS akibat perubahan yang belum tuntas.

4. **Penegakan Pemisahan Kode (*Separation of Concerns*):**
> *"Di kode HTML awards yang baru ini, kenapa masih ada atribut style inline di dalam tag-nya? Gimana cara bersihinnya biar rapi dan tampilannya murni manggil class dari file style.css?"*
* **Tujuan:** Menjaga kepatuhan prinsip *Separation of Concerns* dengan menolak penulisan styling langsung di dokumen HTML dan memindahkan aturan CSS ke stylesheet eksternal.

---

#### 2. Analisis Kritis Keterbatasan AI & Intervensi Mandiri

* **Mengeliminasi *Inline Styles* Demi Prinsip *Separation of Concerns*:**
Pada keluaran rancangan awal template `awards.html`, AI menyisipkan beberapa atribut `style="..."` langsung pada tag HTML untuk *spacing* dan ukuran font. Saya mengidentifikasi hal ini sebagai *bad practice* yang mencederai pemisahan kode. Saya mengintervensi dengan menghapus seluruh styling inline tersebut, mempertahankan pemakaian kelas CSS yang sudah ada di proyek, dan memindahkan aturan tata letak tautan sertifikat ke berkas `style.css`.
* **Mendeteksi dan Memperbaiki *Typo* serta *IndentationError* pada Unit Test:**
Ketika mengimplementasikan pengujian di `main/tests.py`, script pengujian sempat mengalami kegagalan impor modul akibat galat indentasi pada fungsi test *empty state*, serta kesalahan ketik pemanggilan fungsi `reserve()` yang seharusnya `reverse()`[cite: 6]. Saya meninjau pesan *traceback* terminal secara mandiri, memperbaiki indentasi 4 spasi standar PEP 8, menghapus karakter spasi tersembunyi (*non-breaking space*), dan mengoreksi sintaks `reverse()` sehingga seluruh rangkaian unit test lulus dengan status `OK`[cite: 6].
* **Menghindari Pola *Monolithic Commit*:**
AI awalnya menyajikan seluruh berkas modifikasi secara bersamaan dalam satu panduan besar yang berisiko mendorong pembuatan satu commit tunggal di akhir. Saya secara aktif memecah pengerjaan menjadi tahapan terpisah, memverifikasi fungsionalitas per bagian (migrasi database, routing view, template DTL, unit testing), dan melakukan commit atomik secara bertahap sebelum melakukan push akhir ke GitHub dan PWS.