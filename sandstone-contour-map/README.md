# 🗺️ Sandstone Contour Map

Aplikasi berbasis Python untuk membuat **peta kontur bawah permukaan sandstone** berdasarkan data sumur yang disimpan dalam file Excel.

Program menghasilkan visualisasi:

* **Top of Sandstone Map**
* **Bottom of Sandstone Map**
* **Sandstone Thickness**
* **3D Sandstone Surface**

Aplikasi menggunakan interpolasi spasial untuk mengubah data titik sumur menjadi permukaan kontur.

---

## 📌 Fitur

### 1. Import Data Excel

Program dapat membaca file `.xlsx` dengan format:

| No Sumur | Koordinat |   Top | Bottom |
| -------- | --------- | ----: | -----: |
| 1        | 396, 778  | -4400 |  -4510 |
| 2        | 1318, 584 | -4395 |  -4490 |
| 3        | 1911, 340 | -4400 |  -4520 |

Kolom yang diperlukan:

* `No Sumur`
* `Koordinat`
* `Top`
* `Bottom`

Koordinat akan otomatis dipisahkan menjadi:

```text
Koordinat = X, Y

Contoh:
396, 778

X = 396
Y = 778
```

---

## 📊 Output

### Top Sandstone

Menampilkan kontur berdasarkan nilai `Top`.

```text
TOP OF SANDSTONE
        ↓
     Interpolasi
        ↓
   Contour Map
```

### Bottom Sandstone

Menampilkan kontur berdasarkan nilai `Bottom`.

```text
BOTTOM OF SANDSTONE
        ↓
      Interpolasi
        ↓
    Contour Map
```

### Sandstone Thickness

Ketebalan sandstone dihitung dari:

```text
Thickness = |Top - Bottom|
```

Contoh:

```text
Top    = -4400
Bottom = -4510

Thickness = |-4400 - (-4510)|
          = 110
```

### 3D Visualization

Program juga menyediakan visualisasi permukaan Top dan Bottom dalam bentuk 3D menggunakan Plotly.

Visualisasi dapat:

* Diputar
* Di-zoom
* Dipindahkan
* Dilihat dari berbagai sudut

---

## 🛠️ Teknologi

Project ini menggunakan:

| Library    | Fungsi                          |
| ---------- | ------------------------------- |
| Python     | Bahasa pemrograman              |
| Pandas     | Membaca dan mengolah data Excel |
| NumPy      | Pengolahan data numerik         |
| SciPy      | Interpolasi spasial             |
| Matplotlib | Membuat peta kontur             |
| OpenPyXL   | Membaca file Excel              |
| Plotly     | Visualisasi 3D                  |
| Streamlit  | Antarmuka aplikasi              |

---

## 📂 Struktur Project

```text
sandstone-contour-map/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── interpolation.py
│   ├── contour_map.py
│   └── visualization_3d.py
│
├── sample/
│   └── sandstone_data.xlsx
│
└── output/
    ├── top_sandstone.png
    └── bottom_sandstone.png
```

---

## 💻 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/USERNAME/sandstone-contour-map.git
```

Masuk ke folder project:

```bash
cd sandstone-contour-map
```

---

### 2. Membuat Virtual Environment

Disarankan menggunakan virtual environment agar library project tidak bercampur dengan Python system.

Windows:

```powershell
python -m venv .venv
```

Aktifkan:

```powershell
.venv\Scripts\activate
```

Jika menggunakan PowerShell dan muncul masalah permission, dapat menggunakan:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Kemudian aktifkan kembali:

```powershell
.venv\Scripts\activate
```

Jika berhasil, terminal biasanya akan menampilkan:

```text
(.venv) PS C:\...\sandstone-contour-map>
```

---

### 3. Install Dependencies

Pastikan terminal berada di folder project.

Kemudian:

```powershell
python -m pip install -r requirements.txt
```

Jika menggunakan launcher `py`:

```powershell
py -m pip install -r requirements.txt
```

---

## ▶️ Menjalankan Aplikasi

Gunakan:

```powershell
python -m streamlit run app.py
```

Alternatif:

```powershell
py -m streamlit run app.py
```

Setelah berhasil dijalankan, Streamlit akan memberikan alamat lokal pada terminal.

Contohnya:

```text
Local URL: http://localhost:8501
```

Buka alamat tersebut menggunakan browser.

---

## 📄 Format Data Excel

File Excel harus memiliki empat kolom utama:

```text
No Sumur
Koordinat
Top
Bottom
```

Contoh:

| No Sumur | Koordinat |   Top | Bottom |
| -------: | --------- | ----: | -----: |
|        1 | 396, 778  | -4400 |  -4510 |
|        2 | 1318, 584 | -4395 |  -4490 |
|        3 | 1911, 340 | -4400 |  -4520 |
|        4 | 2555, 713 | -4280 |  -4390 |
|        5 | 1788, 892 | -4200 |  -4320 |

### Ketentuan Koordinat

Format koordinat:

```text
X, Y
```

Contoh:

```text
396, 778
```

Program akan mengubahnya menjadi:

```text
X = 396
Y = 778
```

---

## 🔬 Interpolasi

Data sumur memiliki posisi yang tidak teratur atau **scattered points**.

Oleh karena itu, program menggunakan interpolasi spasial dari `scipy.interpolate`.

Metode yang tersedia:

### Linear

```text
linear
```

Merupakan metode default dan direkomendasikan untuk penggunaan awal.

### Cubic

```text
cubic
```

Menghasilkan permukaan yang lebih halus, tetapi dapat menghasilkan bentuk yang kurang stabil apabila jumlah titik data sedikit.

### Nearest

```text
nearest
```

Menggunakan nilai dari titik terdekat.

---

## 🎛️ Pengaturan

Aplikasi menyediakan beberapa parameter:

### Resolusi Interpolasi

Menentukan jumlah grid yang digunakan untuk membuat permukaan.

Contoh:

```text
100 × 100
300 × 300
500 × 500
```

Semakin tinggi resolusi, semakin detail permukaan yang dihasilkan, tetapi proses komputasi juga semakin berat.

### Metode Interpolasi

Pilihan:

```text
Linear
Cubic
Nearest
```

### Interval Kontur

Menentukan jarak antar garis kontur.

Contoh:

```text
10
25
50
100
```

---

## 🖼️ Resolusi Peta

Output peta dirancang menggunakan ukuran:

```text
Width  : 3508 px
Height : 2480 px
```

Rasio:

```text
3508 : 2480
≈ 1.414 : 1
```

Ukuran tersebut digunakan untuk menghasilkan peta dengan format landscape dan resolusi tinggi.

---

## 📐 Data Contoh

Project menggunakan data 21 titik sumur sebagai data pengujian.

Rentang koordinat:

```text
X minimum = 396
X maksimum = 3158

Y minimum = 340
Y maksimum = 2140
```

Data digunakan untuk menguji:

* Parsing koordinat
* Interpolasi
* Top contour
* Bottom contour
* Thickness
* 3D surface

---

## ⚠️ Catatan Interpolasi

Program hanya melakukan interpolasi pada area yang didukung oleh persebaran titik sumur.

Area yang berada di luar persebaran data dapat menghasilkan nilai kosong (`NaN`).

Hal ini dilakukan untuk menghindari **extrapolation** yang dapat menghasilkan interpretasi permukaan yang tidak didukung oleh data sumur.

Dengan kata lain:

```text
        ●
    ●       ●
  ●    AREA    ●
  ● INTERPOLASI●
    ●       ●
        ●
```

Area yang tidak memiliki dukungan titik data tidak dipaksakan memiliki nilai.

---

## 🚀 Pengembangan Selanjutnya

Fitur yang dapat ditambahkan:

* [ ] Thickness Map
* [ ] Export PNG 3508 × 2480
* [ ] Export PDF
* [ ] Export SVG
* [ ] Interactive 2D Map
* [ ] Interactive 3D Map
* [ ] North Arrow
* [ ] Scale Bar
* [ ] Legend
* [ ] Well Symbol
* [ ] Custom Color Scale
* [ ] Contour Interval otomatis
* [ ] Input koordinat X dan Y terpisah
* [ ] Support CSV
* [ ] Cross Section
* [ ] Well-to-well correlation
* [ ] Top-Bottom thickness visualization
* [ ] Struktur bawah permukaan dalam 3D

---

## 🎯 Tujuan Project

Project ini dibuat untuk memvisualisasikan data kedalaman sandstone dari beberapa titik sumur menjadi peta kontur bawah permukaan.

Tujuan utamanya adalah menggabungkan:

```text
Data Sumur
     ↓
Pengolahan Data
     ↓
Interpolasi Spasial
     ↓
Visualisasi 2D
     ↓
Visualisasi 3D
```

Project ini juga menjadi latihan penerapan:

* Python
* Data Processing
* Spatial Interpolation
* Data Visualization
* Subsurface Mapping
* 3D Visualization

---

## 👨‍💻 Author

**[Kagome]**

Project Informatika / Data Visualization

---

## 📜 License

Project ini dibuat untuk tujuan pembelajaran dan pengembangan.
