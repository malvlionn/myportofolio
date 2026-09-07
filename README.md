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