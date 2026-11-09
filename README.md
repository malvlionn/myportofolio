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

---

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

Saya memanfaatkan AI bukan untuk menghasilkan kode secara instan tanpa pemahaman, melainkan sebagai rekan diskusi untuk membedah arsitektur Model-View-Template (MVT), menyusun skenario unit test, serta memastikan kepatuhan alur kerja *version control* terhadap *best practices*.

Beberapa contoh interaksi spesifik yang berfokus pada konsep dan pemecahan masalah:

1. **Pemindahan Komponen Statis ke Model MVT:**
> *"Kalau bagian Awards di halaman utama mau saya pisah jadi halaman tersendiri pakai pola MVT, rancangan modelnya yang pas gimana ya biar styling kartu dan highlight juaranya tetap sinkron sama CSS yang udah ada?"*
* **Tujuan:** Menentukan atribut dan tipe data yang tepat untuk model `Award` (seperti field boolean untuk status juara dan tanggal) agar data dinamis dari database dapat langsung dipetakan ke struktur layout CSS yang sudah ada.

2. **Pengaturan Alur dan Batasan Commit Git:**
> *"Bantu breakdown alur commit Git yang ideal untuk tugas MVT ini dong. File apa aja yang perlu di-stage duluan dan kapan momen yang tepat buat commit biar riwayatnya rapi bertahap dan gak numpuk di akhir?"*
* **Tujuan:** Memahami penerapan *atomic commit* dengan memisahkan progres kerja per lapisan fungsional (migrasi model &rarr; views dan urls &rarr; template dan navigasi &rarr; pengujian unit test).

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
Ketika mengimplementasikan pengujian di `main/tests.py`, script pengujian sempat mengalami kegagalan impor modul akibat galat indentasi pada fungsi test *empty state*, serta kesalahan ketik pemanggilan fungsi `reserve()` yang seharusnya `reverse()`. Saya meninjau pesan *traceback* terminal secara mandiri, memperbaiki indentasi 4 spasi standar PEP 8, menghapus karakter spasi tersembunyi (*non-breaking space*), dan mengoreksi sintaks `reverse()` sehingga seluruh rangkaian unit test lulus dengan status `OK`.
* **Menghindari Pola *Monolithic Commit*:**
AI awalnya menyajikan seluruh berkas modifikasi secara bersamaan dalam satu panduan besar yang berisiko mendorong pembuatan satu commit tunggal di akhir. Saya secara aktif memecah pengerjaan menjadi tahapan terpisah, memverifikasi fungsionalitas per bagian (migrasi database, routing view, template DTL, unit testing), dan melakukan commit atomik secara bertahap sebelum melakukan push akhir ke GitHub dan PWS.

---

### Tugas 3

1. Alasan kita menggunakan `ModelForm` pada Django daripada membuat form HTML secara manual adalah:
- Prinsip DRY (Don't Repeat Yourself): `ModelForm` secara otomatis membaca skema kolom, tipe data, batasan `max_length`, serta pilihan `choices` dari `models.py` dan langsung memetakannya ke elemen input formulir tanpa perlu menulis ulang tag HTML secara manual.
- Validasi dan Sanitasi Data Otomatis: Saat memanggil `form.is_valid()`, Django akan membersihkan data masukan (data cleaning) serta memvalidasi kesesuaian format data. Jika data tidak valid, pesan kesalahan terstruktur langsung disediakan lewat `form.errors`.
- Kemudahan Pengikatan Data (Two-Way Binding): Untuk proses update, `ModelForm` mendukung parameter `instance` (seperti `ExperienceForm(request.POST or None, instance=experience)`) yang otomatis mengisi form dengan data lama dan menyimpannya langsung ke database via `form.save()` tanpa perlu mengambil nilai manual lewat `request.POST.get(...)`.

Kewajiban menambahkan `{% csrf_token %}` pada form ditujukan untuk:
- Proteksi Serangan CSRF (Cross-Site Request Forgery): Mencegah situs berbahaya pihak ketiga mengeksploitasi cookie sesi aktif milik pengguna di browser untuk mengirimkan aksi manipulatif (POST, PUT, DELETE) ke server tanpa otorisasi sadar dari pengguna.
- Validasi Integritas Sesi: Tag `{% csrf_token %}` menyisipkan input tersembunyi (hidden token) berbasis kriptografi yang unik untuk setiap sesi form. Middleware `CsrfViewMiddleware` akan memvalidasi kecocokan token payload dengan cookie pengguna. Jika tidak cocok atau absen, request langsung ditolak dengan kode status HTTP 403 Forbidden.

2. JSON lebih disukai dibandingkan XML dalam pengembangan web modern karena:
- Ukuran Data Ringkas (Lightweight): Format pasangan key-value pada JSON tidak memerlukan tag penutup repetitif seperti XML (`<item>nilai</item>`) sehingga ukuran transmisi data jauh lebih kecil dan hemat bandwidth jaringan.
- Dukungan Native pada JavaScript: JSON merupakan representasi objek intrinsik JavaScript yang dapat langsung di-parse menggunakan fungsi bawaan `JSON.parse()` dan `JSON.stringify()` tanpa membutuhkan pustaka XML DOM Parser eksternal.
- Representasi Tipe Data Alami: JSON mendukung tipe data primitif secara langsung (string, number, boolean, array, object, null), tapi XML memperlakukan seluruh nilainya sebagai teks sehingga membutuhkan konversi tipe data manual di sisi klien.
- Standar Ekosistem Web dan Mobile: Arsitektur modern seperti RESTful API, Single Page Applications (SPA), dan aplikasi mobile menjadikan JSON sebagai format pertukaran data standar.

3. Alur view saat mengembalikan data portofolio dalam format JSON adalah:
- Klien mengirimkan permintaan HTTP GET ke endpoint data (misalnya `/api/experience/` atau melalui view `show_experience`).
- Pola rute di `main/urls.py` memetakan URL tersebut dan memanggil fungsi view `get_experience_json`.
- ORM Django mengeksekusi `Experience.objects.all()` untuk mengambil rekaman data dari tabel database SQLite dalam bentuk objek `QuerySet`.
- Fungsi `serializers.serialize('json', experiences)` membaca seluruh atribut dan metadata dari objek model, lalu mengonversinya menjadi string berformat JSON.
- String JSON dibungkus ke dalam objek `HttpResponse` dengan header `content_type="application/json"` dan dikembalikan sebagai HTTP Response dengan status 200 OK.
- Pada fungsi `show_experience`, string JSON tersebut dideserialisasi kembali menggunakan `serializers.deserialize('json', ...)`, diekstrak atribut `.object`-nya, lalu dikirimkan ke context template untuk dirender menjadi antarmuka HTML.

Alasan diperlukannya proses serialisasi pada model Django:
- Objek model Django (`QuerySet` atau instance model) adalah struktur data internal Python yang kompleks di dalam memori (in-memory objects) yang menyimpan referensi pointer, metode internal ORM, dan metadata relasional yang tidak dapat dibaca atau dikirimkan langsung melalui protokol teks HTTP.
- Serialisasi diperlukan untuk menerjemahkan objek internal tersebut menjadi aliran data teks terstandarisasi (seperti JSON) agar dapat ditransmisikan melintasi jaringan internet dan dipahami oleh berbagai aplikasi peramban maupun klien eksternal.

---

### AI Disclosure & Critical Reflection

* **Model/Tools yang Digunakan:** Google Gemini

---

#### 1. Cakupan Penggunaan & Contoh Prompt Reflektif

Saya memanfaatkan AI bukan untuk menghasilkan kode jadi secara instan tanpa pemahaman, melainkan sebagai rekan diskusi untuk membedah arsitektur `ModelForm`, memastikan alur serialisasi dan deserialisasi data JSON berjalan tepat sesuai pola MVC/MVT, serta mendiagnosis kendala tata letak CSS pada komponen antarmuka dinamis.

Beberapa contoh interaksi spesifik yang berfokus pada konsep dan pemecahan masalah:

1. **Konfigurasi Form Widget dan Integritas Skema Database:**
> *"Di model Experience kan ended_at tipenya DateTimeField, tapi saya maunya user cukup milih bulan sama tahun doang tanpa perlu input hari atau jam. Bisa gak dibuat lewat widget form aja biar skema database di models.py gak perlu diubah atau migrasi ulang?"*
* **Tujuan:** Mengetahui cara mengatur representasi input antarmuka (`<input type="month">`) dengan *custom parser* `input_formats` pada `ModelForm` tanpa harus merombak skema kolom database yang sudah ada.

2. **Penegakan Pemisahan Kode (*Separation of Concerns*):**
> *"Di template form sama modal ini, beberapa styling tombol dan flexbox-nya masih nempel di inline HTML. Gimana cara refactor yang paling clean ke style.css biar struktur markup-nya bener-bener bersih dan patuh sama prinsip separation of concerns?"*
* **Tujuan:** Mengeliminasi seluruh atribut `style="..."` di berkas template HTML dan memindahkannya menjadi kelas CSS utilitas yang modular pada berkas `style.css` eksternal.

3. **Troubleshooting Tata Letak Kartu dan Komponen Tombol:**
> *"Saya udah pasang tombol Ubah sama modal Hapus di kartu Experience, tapi posisinya berantakan. Tombol hapusnya malah turun ke baris baru dan tinggi kartunya gak sinkron pas kontennya beda panjang. Kira-kira letak constraint CSS yang miss di mana ya biar layout tombolnya sejajar di dasar kartu?"*
* **Tujuan:** Mendiagnosis dampak elemen blok pembungkus `<p>` pada tombol modal yang memicu *line break*, serta menerapkan struktur *flexbox column* dengan `justify-content: space-between` agar tombol aksi selalu terkunci simetris di dasar kartu.

4. **Penerapan *Atomic Commits* pada Alur Git:**
> *"Biar riwayat commit di Git keliatan bertahap dan gak numpuk jadi satu commit di akhir, checkpoint apa aja yang ideal per lapisannya (dari forms, view logic/routing, template refactoring, sampe UI form)? Tolong bikinin breakdown commit atomik pake konvensi conventional commits."*
* **Tujuan:** Merancang pembagian batas *commit* kerja yang logis per fitur fungsional agar riwayat repositori mencerminkan proses pengembangan inkremental yang terstruktur.

---

#### 2. Analisis Kritis Keterbatasan AI & Intervensi Mandiri

* **Mengoreksi Format Input Tanggal agar Tidak Merusak Basis Data:**
Ketika meminta input waktu yang hanya mencakup bulan dan tahun pada model `Experience`, saran umum awal menyarankan konversi field model menjadi `CharField` yang menuntut migrasi database ulang. Saya mengintervensi dengan mempertahankan model `DateTimeField` yang ada, lalu secara mandiri mengonfigurasi form menggunakan widget `DateInput(format="%Y-%m", attrs={"type": "month"})` dan menambahkan `input_formats=["%Y-%m"]` pada form field. Pendekatan ini menjaga konsistensi database sekaligus membatasi input pengguna hanya pada level bulan dan tahun.
* **Membersihkan *Inline CSS* dan Memperbaiki Perilaku Komponen Modal:**
Rancangan awal keluaran AI sempat menyisipkan banyak atribut `style=""` pada elemen formulir serta membungkus tombol hapus di dalam tag `<p class="card-actions-wrapper">`. Hal ini menyebabkan tombol "Hapus" terdorong ke bawah tombol "Ubah". Saya mengoreksi hal ini dengan menghapus seluruh inline style, mengganti tag pembungkus tombol menjadi `div.btn-inline`, serta mendefinisikan kelas CSS utilitas (`.experience-toolbar`, `.experience-card-item`, `.card-actions-row`) di `style.css` agar posisi tombol sejajar rapi di sudut kanan bawah.
* **Memperbaiki Ekstraksi Objek Hasil Deserialisasi JSON:**
Saat menerapkan deserialisasi data JSON di view `show_experience`, AI sempat mereferensikan queryset secara langsung. Mengingat bahwa `serializers.deserialize()` mengembalikan generator `DeserializedObject`, saya melakukan penyesuaian melalui *list comprehension* `[item.object for item in deserialized_data]` agar pemanggilan metode model seperti `get_category_display` dan properti `is_ongoing` di template tetap berfungsi normal tanpa error.
* **Menghapus Duplikasi Routing pada Proyek:**
Saya mengaudit konfigurasi URL di `portofolio/urls.py` dan mendeteksi adanya rute ganda untuk `experience/` dan `awards/` yang didefinisikan di luar `main.urls`. Saya merapikan berkas tersebut secara manual agar delegasi routing terpusat bersih ke modul aplikasi `main`.

---

### Tugas 4

### AI Disclosure

Pada pengerjaan Tugas 4 ini, saya tidak menggunakan perangkat Generative AI (seperti Google Gemini, ChatGPT, Claude, GitHub Copilot, maupun model bahasa besar lainnya) untuk menghasilkan kode, merancang arsitektur logika, ataupun menyelesaikan permasalahan teknis. Seluruh baris kode backend, penyesuaian template, pengelolaan hak akses, dan konfigurasi basis data diselesaikan secara mandiri melalui materi perkuliahan. Saya mengerjakan Tugas 4 ini mengikuti Tutorial 4 yang ada di website PBP.

---

### Tugas 5

1. Debouncing adalah teknik optimasi pemrograman yang menunda pemanggilan suatu fungsi (misalnya pemanggilan `fetch()` ke endpoint pencarian) sampai jeda waktu tertentu berlalu tanpa ada pemicu (*event*) baru dari pengguna. Jika pengguna memicu *event* kembali sebelum jeda waktu tersebut habis, *timer* yang sedang berjalan akan dibatalkan (`clearTimeout`) dan dihitung ulang dari awal.

Teknik ini sangat penting diterapkan pada fitur pencarian berbasis AJAX karena:
- Mencegah *Request Flooding*: Tanpa debouncing, setiap karakter yang diketikkan pengguna pada *event* `input` akan langsung menembakkan satu HTTP *request* ke server. Mengetikkan kata dengan 10 karakter berarti mengirimkan 10 permintaan jaringan secara beruntun.
- Mengurangi Beban Komputasi Server dan Basis Data: Operasi pencarian teks di backend (seperti pencarian `icontains` pada Django ORM) memakan sumber daya komputasi yang cukup intensif. Debouncing memastikan server hanya memproses *query* saat pengguna benar-benar sudah berhenti mengetik.
- Mencegah Terjadinya *Race Conditions* (*Stale Data*): Karena adanya variasi latensi jaringan, *request* pencarian awal yang berisi sedikit karakter bisa saja selesai lebih lambat dibandingkan *request* akhir. Tanpa debouncing dan kontrol pembatalan (seperti `AbortController`), respons usang berpotensi menimpa data yang lebih baru di antarmuka web sehingga hasil pencarian menjadi tidak akurat.

2. Fungsi dari penggunaan `await` ketika menggunakan `fetch()` adalah untuk menunda atau menjeda (*pause*) eksekusi baris kode berikutnya di dalam fungsi `async` secara non-blocking sampai *Promise* yang dikembalikan oleh `fetch()` selesai diproses (*resolved*) dan menghasilkan objek `Response` yang sesungguhnya.

Hal yang akan terjadi jika kita tidak menggunakan `await` adalah:
- Variabel yang menampung pemanggilan tersebut tidak akan berisi data atau objek respons HTTP, melainkan objek *Promise* dengan status pending (`Promise { <pending> }`).
- Ketika kode mencoba mengakses properti atau metode respons (seperti `response.ok` atau `response.json()`), peramban akan melempar *runtime error* (misalnya `TypeError: response.json is not a function` atau mengembalikan `undefined`).
- Baris kode untuk manipulasi DOM dan perakitan kartu HTML akan langsung dieksekusi sebelum data dari jaringan diterima oleh browser, sehingga perakitan kartu gagal dan data tidak akan pernah tampil di halaman.

3. Serangan Cross-Site Scripting (XSS) adalah kerentanan keamanan web di mana penyerang berhasil menyisipkan skrip berbahaya (umumnya JavaScript) ke dalam halaman web yang kemudian dieksekusi oleh peramban pengguna lain. Serangan ini dapat dimanfaatkan penyerang untuk membaca cookie sesi, mencuri token CSRF, melakukan aksi manipulatif atas nama pengguna yang sedang masuk, hingga merusak tampilan antarmuka web (*defacement*).

Data yang ditampilkan melalui AJAX/JavaScript jauh lebih rentan terhadap serangan ini dibandingkan data yang ditampilkan langsung melalui template Django karena:
- Peniadaan Fitur *Auto-Escaping* Bawaan Django: Saat menggunakan *server-side template rendering* biasa (seperti `{{ experience.title }}`), mesin template Django secara otomatis mengubah karakter-karakter khusus HTML (`<`, `>`, `&`, `"`, `'`) menjadi entitas HTML (`&lt;`, `&gt;`, dll.) sehingga kode berbahaya selalu dirender sebagai teks biasa.
- Penyisipan Langsung ke DOM via `innerHTML`: Pada alur AJAX, data JSON yang diterima sering dirakit ke dalam *template literal* JavaScript lalu dipasang ke elemen DOM menggunakan properti `.innerHTML`. Peramban secara inheren mengurai string tersebut sebagai kode markup aktif, sehingga jika data mengandung tag HTML atau event handler seperti `<img src="x" onerror="alert('XSS!')">`, skrip tersebut akan langsung dieksekusi oleh peramban.

Oleh karena itu, pada implementasi AJAX diperlukan sistem pertahanan berlapis (*defense-in-depth*), yaitu melakukan *escaping* manual pada setiap nilai teks di sisi klien (menggunakan fungsi pembantu `escapeHtml`) serta membersihkan tag berbahaya di sisi server menggunakan `strip_tags` pada metode `clean_<field>()` di Django Form.

---

### AI Disclosure & Critical Reflection

* **Model/Tools yang Digunakan:** Google Gemini

---

#### 1. Cakupan Penggunaan & Contoh Prompt Reflektif

Saya memanfaatkan AI bukan untuk menghasilkan kode secara instan tanpa pemahaman, melainkan sebagai rekan diskusi untuk membedah arsitektur interaktivitas JavaScript, merancang penanganan form asinkron berbasis Fetch API, serta mengevaluasi celah keamanan *Cross-Site Scripting* (XSS) pada manipulasi DOM dinamis.

Beberapa contoh interaksi spesifik yang berfokus pada konsep dan pemecahan masalah:

1. **Sinkronisasi Filter Dropdown dan Debouncing Pencarian AJAX:**
> *"Di halaman Experience kan ada dropdown kategori sama input pencarian teks. Gimana arsitektur JavaScript yang ideal biar pas user ngetik pencarian atau milih kategori, datanya sama-sama di-fetch lewat satu endpoint AJAX tanpa saling menimpa query parameter satu sama lain?"*
* **Tujuan:** Menemukan pola perancangan *event handling* yang bersih menggunakan objek `URLSearchParams`, mengintegrasikan *event listener* `input` dan `change` ke dalam satu fungsi terpusat, serta menerapkan *debouncing* (300 ms) yang efisien.

2. **Strategi Pertahanan Berlapis (*Defense-in-Depth*) terhadap Serangan XSS:**
> *"Kenapa fungsi strip_tags di clean_title Django Form dibilang belum cukup buat ngejamin keamanan XSS sepenuhnya pas kita render data lewat innerHTML di JavaScript? Kenapa kita masih wajib bikin fungsi escapeHtml manual di sisi client?"*
* **Tujuan:** Memahami secara mendalam perbedaan antara pembersihan data masuk (*input sanitization*) di backend dengan *output escaping* saat perakitan string DOM di peramban, serta potensi lolosnya karakter seperti tanda kutip pada atribut HTML jika *escaping* klien diabaikan.

3. **Penanganan Validasi Error AJAX dan Integrasi Toast:**
> *"Kalau form di modal ditolak sama server gara-gara validasi Django gagal atau CSRF token bermasalah, gimana cara JavaScript nangkep pesan error dari JsonResponse status 400 atau 403 terus nampilin pesannya langsung ke komponen toast tanpa reload halaman?"*
* **Tujuan:** Memahami parsing struktur respons `form.errors.get_json_data()` dari Django menjadi deretan pesan kesalahan yang mudah dibaca pengguna melalui pemanggilan fungsi `showToast` bertipe `error`.

4. **Penerapan *Milestone-Based Conventional Commits*:**
> *"Bantu breakdown alur commit Git yang ideal untuk migrasi halaman statis ke AJAX penuh dong, biar commit-nya gak numpuk di akhir dan rapi per lapisan (backend, modal/CSS, frontend AJAX/XSS, dan dokumentasi) pake conventional commits."*
* **Tujuan:** Menjaga kepatuhan *version control best practices* dengan membagi pekerjaan menjadi unit-unit perubahan atomik yang logis dan deskriptif.

---

#### 2. Analisis Kritis Keterbatasan AI & Intervensi Mandiri

* **Mendiagnosis dan Mengoreksi Bug *Null Reference* pada Skrip DOM:**
Pada kode awal `experience.html`, ditemukan kesalahan berupa pemanggilan `document.getElementById('search-input')` dan penambahan *event listener*, padahal elemen input tersebut belum ada di markup template lama. Hal ini menyebabkan galat `TypeError: Cannot read properties of null (reading 'addEventListener')` di konsol peramban yang mematikan seluruh eksekusi JavaScript. Saya mengintervensi dengan merestrukturisasi markup *toolbar* di `experience.html`, menambahkan elemen input pencarian teks dan tombol reset yang sesuai, serta memastikan semua elemen DOM yang ditargetkan benar-benar ada sebelum diikat dengan *event listener*.
* **Mengoreksi Inkonsistensi Penamaan Atribut Model (`project_url` vs `thumbnail`):**
Ketika menghasilkan skrip perakitan kartu di JavaScript, AI cenderung meniru persis atribut dari Tutorial 5 dengan memanggil `experience.project_url`. Padahal pada skema model `Experience` yang saya bangun di Tugas 3, atribut tautan media dinamai `thumbnail`. Saya mengoreksi pemetaan field JSON di `views.py` dan perakitan tautan di `buildExperienceCardElement()` agar merujuk pada `experience.thumbnail`, sehingga kartu menampilkan tautan dokumentasi dengan benar dan terhindar dari nilai `undefined`.
* **Mengintegrasikan Pencarian Teks, Filter Kategori, dan Tombol Reset Secara Terpadu:**
AI awalnya menyarankan penanganan terpisah antara filter form submit biasa dan pencarian teks AJAX. Saya mengintervensi dengan merombak alur tersebut menjadi fungsi terpadu `triggerFilter()`. Fungsi ini menggabungkan nilai pencarian teks dan pilihan kategori ke dalam `URLSearchParams`, mengontrol pembatalan request lama via `AbortController`, serta secara dinamis mengatur visibilitas tombol "Reset" sesuai status input pengguna.
* **Menerapkan *Milestone Commit* Bertahap:**
Menyadari kecenderungan saran AI yang menyajikan seluruh berkas secara serentak sehingga berisiko memicu *monolithic commit*, saya secara disiplin membagi proses pengerjaan menjadi empat *milestone* commit terpisah (`feat(backend)`, `feat(ui)`, `feat(frontend)`, dan `docs`) untuk memastikan riwayat pengembangan pada repositori Git tertata secara profesional.

### Tugas 6

1. REST (Representational State Transfer) adalah gaya arsitektur perancangan web API yang memperlakukan data sebagai *resource* yang dapat diidentifikasi secara unik menggunakan URI (Uniform Resource Identifier), memanfaatkan metode HTTP standar (GET, POST, PUT, PATCH, DELETE) untuk menyatakan tindakan operasi, serta bersifat *stateless* di mana server tidak menyimpan status interaksi klien antar-request.

Alasan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful adalah:
- JSON hanyalah Format Data (Representation Format): Mengembalikan format JSON hanyalah representasi data yang ditransmisikan. Sebuah API baru dapat dikategorikan RESTful jika mematuhi kaidah arsitektur REST, yaitu penamaan endpoint yang berorientasi pada kata benda resource (misalnya `/api/v1/awards/`, bukan kata kerja seperti `/api/v1/awards/get-all/` atau `/create-award/`), serta tindakan manipulasi data sepenuhnya diatur oleh HTTP Verbs.
- Penggunaan Status Kode HTTP Semantik: API RESTful menggunakan kode status HTTP secara disiplin untuk merefleksikan hasil operasi (seperti 200 OK untuk pembacaan, 201 Created untuk penambahan, 204 No Content untuk penghapusan tanpa body, 400 Bad Request untuk kesalahan validasi input, 403 Forbidden untuk penolakan hak akses, dan 404 Not Found saat resource tidak ditemukan). Mengembalikan status 200 OK tetapi menyisipkan pesan error di dalam body JSON bukanlah praktik RESTful.
- Negosiasi Konten (Content Negotiation): API RESTful mendukung penyesuaian format representasi berdasarkan header `Accept` yang dikirimkan klien, misalnya merender Browsable API HTML untuk peramban dan JSON mentah ketika diminta oleh skrip AJAX.

Perbedaan PUT dan PATCH beserta contoh penggunaannya:
- PUT (Full Replacement / Idempoten): Mengganti seluruh representasi resource target dengan representasi baru yang dikirimkan klien secara utuh. Klien wajib mengirimkan seluruh atribut field yang diperlukan model. Jika ada field opsional yang tidak disertakan, field tersebut akan dikosongkan atau diatur ke nilai default.
  - *Contoh Penggunaan:* Saat melakukan sinkronisasi data penghargaan dari sistem eksternal secara komprehensif, di mana seluruh field (`title`, `issuer`, `tier`, `date`, `description`, `certificate_url`, `is_winner`) dikirimkan secara serentak untuk menimpa rekaman yang ada di basis data.
- PATCH (Partial Update): Hanya memperbarui sebagian atribut tertentu pada resource tanpa memengaruhi atribut lainnya yang tidak disertakan dalam payload request.
  - *Contoh Penggunaan:* Ketika pengguna dengan peran Editor hanya ingin memperbaiki kesalahan ketik pada judul penghargaan melalui modal edit ringan dengan mengirimkan payload `{"title": "Judul Baru"}`, sementara deskripsi, penyelenggara, dan tautan sertifikat lama tetap dipertahankan oleh server.

2. Peran serializer pada Django REST Framework adalah sebagai penerjemah dan validator dua arah (*two-way pipeline*) antara tipe data kompleks model Django dengan representasi data terstruktur yang siap dikirimkan melalui jaringan (seperti JSON):
- Serialisasi (Model Instance / QuerySet &rarr; Python Primitives / JSON): Mengubah objek model basis data ke dalam tipe data bawaan Python (dictionary, list) yang kemudian diproses oleh renderer DRF menjadi format JSON untuk dikirimkan sebagai HTTP Response.
- Deserialisasi dan Validasi Data (JSON Input &rarr; Validated Data / Model Instance): Mengambil data masukan mentah dari request klien, memvalidasi kesesuaian tipe data dan batasan field, menjalankan sanitasi kustom melalui method `validate_<field>` (seperti pembersihan tag HTML via `strip_tags`), serta menyimpannya langsung ke database via `.save()`.

Keuntungan menggunakan serializer dibandingkan merakit dictionary secara manual dengan `JsonResponse` (Tutorial 05):
- Validasi Input Deklaratif dan Terpusat: Serializer secara otomatis memvalidasi tipe data, format URL, nilai null, serta menghasilkan pesan kesalahan yang terstruktur per field (`serializers.ValidationError`) tanpa perlu menulis pengecekan `if-else` manual yang repetitif di dalam view.
- Penanganan Field Dinamis dan Read-Only: Mendukung `SerializerMethodField` untuk field kalkulasi dinamis (seperti `star_count` dan `is_starred` berbasis user yang sedang masuk), sekaligus mengunci atribut sensitif melalui `read_only_fields` agar tidak dapat dimanipulasi oleh payload request klien.
- Pemisahan Tanggung Jawab (*Separation of Concerns*): Logika representasi dan validasi data terisolasi di dalam `serializers.py`, sehingga fungsi view di `api_views.py` tetap bersih, ramping, dan hanya berfokus pada alur kontrol HTTP serta penegakan hak akses.

3. Perbedaan autentikasi dan otorisasi pada Django REST Framework:
- Autentikasi (Authentication): Proses untuk memverifikasi dan membuktikan identitas pengguna yang membuat request (*"Siapa Anda?"*). Pada DRF, `SessionAuthentication` memeriksa cookie session Django untuk mengidentifikasi akun pengguna dan mengisi objek `request.user`.
- Otorisasi (Authorization / Permissions): Proses penentuan apakah pengguna yang telah teridentifikasi memiliki hak yang sah untuk menjalankan tindakan tertentu (*"Apa yang boleh Anda lakukan?"*). Hal ini ditentukan oleh kelas permission (seperti `IsPortfolioOwnerOrEditorOrReadOnly`).

Alasan hak akses harus diperiksa dengan permission class di server, bukan hanya dengan menyembunyikan tombol di template:
- Keamanan Sisi Klien Bersifat Kosmetik: Menyembunyikan tombol tambah, ubah, atau hapus di antarmuka HTML hanyalah peningkatan pengalaman visual bagi pengguna (*UX*), bukan perlindungan keamanan.
- Kerentanan Manipulasi Request Langsung: Penyerang atau pengguna biasa dapat dengan mudah mengirimkan request HTTP `POST`, `PUT`, `PATCH`, atau `DELETE` langsung ke endpoint API menggunakan alat seperti cURL, Postman, Fetch API via DevTools Console, atau skrip eksternal tanpa melalui tombol antarmuka web.
- Penegakan Integritas Data di Tingkat Server: Permission class bertindak sebagai gerbang pengaman di lapisan backend. Jika pemeriksaan izin tidak ditegakkan di server, siapa pun yang mengetahui ID suatu objek dapat menghapus atau memodifikasi database secara ilegal.

4. Permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai `SessionAuthentication` karena:
- Mekanisme Cookie Otomatis: `SessionAuthentication` memanfaatkan cookie sesi (`sessionid`) yang disimpan di peramban. Ketika peramban mengirimkan request ke domain web kita, peramban secara otomatis akan menyertakan cookie tersebut, bahkan jika request dipicu oleh situs jahat pihak ketiga (*cross-site*).
- Pencegahan Eksploitasi CSRF: Tanpa validasi token CSRF, situs berbahaya dapat memalsukan aksi berbahaya (seperti mengirim request `DELETE` untuk menghapus penghargaan) atas nama pengguna yang sedang masuk. Header `X-CSRFToken` memastikan bahwa request yang mengubah basis data benar-benar berasal dari antarmuka situs kita sendiri (*same-origin proof*).

Alasan test yang memakai `force_authenticate` tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan:
- `force_authenticate(user=user)` adalah utilitas pengujian internal DRF yang bekerja dengan cara langsung menyuntikkan objek pengguna ke `request.user` pada level framework pengujian.
- Pemanggilan ini secara eksplisit **melewati (*bypasses*)** seluruh siklus penanganan autentikasi peramban yang sebenarnya, termasuk parsing cookie sesi dan evaluasi middleware `CsrfViewMiddleware`.
- Akibatnya, pengujian yang hanya memakai `force_authenticate` tidak pernah mengeksekusi logika pemeriksaan token CSRF. Untuk memverifikasi bahwa perlindungan CSRF berfungsi sebagaimana mestinya di dunia nyata, pengujian harus menggunakan `APIClient(enforce_csrf_checks=True)` yang dipadukan dengan `client.login()`, lalu menguji penolakan (403 Forbidden) saat token absen serta penerimaan (201/200) saat token `X-CSRFToken` disertakan.

---

### AI Disclosure & Critical Reflection

* **Model/Tools yang Digunakan:** Google Gemini

---

#### 1. Cakupan Penggunaan & Contoh Prompt Reflektif

Saya memanfaatkan AI bukan untuk menghasilkan kode secara instan tanpa pemahaman, melainkan sebagai rekan diskusi untuk membedah arsitektur Django REST Framework, merancang hierarki hak akses berbasis peran pada API endpoint, serta memecahkan kendala teknis (*debugging*) pada validasi serializer dan suite pengujian otomatis.

Beberapa contoh interaksi spesifik yang berfokus pada konsep dan pemecahan masalah:

1. **Perancangan Serializer dan Pembersihan Tag HTML:**
> *"Di AwardSerializer kan ada validasi teks pakai strip_tags buat field title sama description kayak clean_<field> di form sebelumnya. Gimana cara bikin serializer yang otomatis ngitung jumlah star sama status star user aktif, tapi field itu terkunci read-only biar gak bisa dipalsukan klien?"*
* **Tujuan:** Memahami penggunaan `SerializerMethodField` yang membaca relasi `starred_by` dengan memanfaatkan `self.context.get('request')`, serta mengonfigurasi `read_only_fields` pada Meta serializer untuk mencegah eksploitasi data.

2. **Penegakan Hak Akses Multi-Peran (4 Peran):**
> *"Gimana cara menerapkan permission class IsPortfolioOwnerOrEditorOrReadOnly di API endpoint Awards biar pengunjung biasa cuma bisa baca, user login bisa star, Editor cuma bisa PUT/PATCH, dan Superuser bisa CRUD lengkap?"*
* **Tujuan:** Memastikan pemisahan logika permission berbasis method HTTP (`SAFE_METHODS` vs mutasi data) dan keanggotaan grup (`Editor`) di tingkat server, bukan sekadar menyembunyikan tombol di template.

3. **Diagnosa Kegagalan Test Validasi Sanitasi:**
> *"Di test_validation APITestCase, kenapa assertion error dapet status 201 Created padahal ekspektasinya 400 Bad Request pas ngirim payload script alert? Bagian mana yang keliru dari fungsi strip_tags bawaan Django?"*
* **Tujuan:** Mendiagnosis karakteristik kerja fungsi `strip_tags()` Django yang hanya membuang pembungkus tag tetapi mempertahankan isi teks anak dari elemen berpasangan, sehingga memahami mengapa pengujian sanitasi harus menggunakan void tag seperti `<img>`.

4. **Integrasi AJAX In-Place Modal vs Halaman Terpisah:**
> *"Di tugas diminta fitur update data via PUT/PATCH, opsinya bisa bikin modal edit baru atau ubah form update_award.html lama. Dari sisi arsitektur SPA dan rubrik penilaian interaktivitas, pendekatan mana yang lebih optimal dan gimana cara binding datanya via Fetch API?"*
* **Tujuan:** Mengevaluasi trade-off desain UX antara manipulasi DOM in-place menggunakan popover modal edit terpisah dengan pengalihan halaman konvensional, demi mencapai pengalaman *zero page reload*.

---

#### 2. Analisis Kritis Keterbatasan AI & Intervensi Mandiri

* **Mengoreksi Payload Pengujian XSS pada `test_validation`:**
Saat merancang pengujian validasi masukan di `main/tests_api.py`, kode awal AI menyertakan payload `{"title": "<script>alert(1)</script>"}` dengan asumsi server akan mengembalikan status 400 Bad Request. Faktanya, fungsi `strip_tags()` bawaan Django menyisakan string `'alert(1)'` sehingga serializer menganggap input tersebut valid dan menghasilkan status 201 Created. Saya menganalisis masalah ini, memahami perilakunya, dan mengintervensi dengan mengganti payload uji menjadi void element `<img src="x" onerror="alert(1)">`. Dengan begitu, tag terhapus seutuhnya menjadi string kosong, memicu validasi serializer secara tepat, dan membuat seluruh unit test lulus dengan status `OK`.
* **Menangani Normalisasi Input Checkbox Boolean dan URL Kosong:**
Ketika data formulir dikirimkan melalui `FormData` pada modal, nilai checkbox yang dicentang bernilai string `'on'` atau `'true'`, dan field URL yang tidak diisi menghasilkan string kosong `""`. Serializer bawaan sempat melempar galat validasi tipe data URL dan boolean. Saya mengintervensi dengan menambahkan penanganan khusus pada metode `to_internal_value` di `AwardSerializer` untuk mengonversi string kosong menjadi `None` dan memetakan string `'on'` menjadi tipe boolean `True`.
* **Mengimplementasikan Modal Edit In-Place untuk Mencegah Navigasi Halaman:**
Saran awal sempat mempertahankan tombol "Ubah" yang mengarahkan pengguna ke halaman terpisah `update_award.html`. Saya menyadari bahwa berpindah halaman mencederai kenyamanan antarmuka dinamis berbasis AJAX. Saya secara mandiri membuat komponen popover baru `templates/components/award_edit_modal.html`, menghubungkannya dengan event delegation pada kartu penghargaan melalui fungsi `openEditModal()`, dan mengeksekusi request `PATCH` asinkron sehingga seluruh proses pengeditan data berjalan di satu layar tanpa reload dokumen.
* **Menerapkan *Milestone Commit* Atomik yang Rapi:**
Menyadari kecenderungan saran otomatis yang sering menggabungkan seluruh perubahan ke dalam satu langkah besar, saya secara disiplin membagi implementasi menjadi tahapan *atomic commit* berbasis konvensi *Conventional Commits* (`feat(api)`, `test(api)`, `feat(awards)`, `docs`), menjaga riwayat repositori tetap bersih dan mencerminkan progres bertahap sesuai rubrik.