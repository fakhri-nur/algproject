from PyQt5.QtCore import QTime

win_x, win_y = 100, 100
win_width, win_height = 1000, 600

txt_hello = 'Selamat datang di program deteksi status kesehatan!'
txt_next = 'Mulai'
txt_instruction = ('Aplikasi ini memungkinkan Anda menggunakan tes Rufier untuk melakukan diagnosis awal kesehatan Anda.\n'
                   'Tes Rufier adalah serangkaian latihan fisik yang dirancang untuk menilai kinerja jantung Anda selama aktivitas fisik.\n'
                   'Subjek berbaring dalam posisi telentang selama 5 menit dan mengukur denyut nadi selama 15 detik;\n'
                   'kemudian, dalam waktu 45 detik, subjek melakukan 30 squat.\n'
                   'Ketika latihan selesai, subjek berbaring dan denyut nadinya diukur lagi untuk 15 detik pertama\n'
                   'dan kemudian untuk 15 detik terakhir dari menit pertama periode pemulihan.\n'
                   'Penting! Jika Anda merasa tidak enak badan selama tes (pusing,\n'
                   'tinnitus, sesak napas, dll.), hentikan tes dan konsultasikan dengan dokter.')
txt_title = 'Kesehatan'
txt_name = 'Masukkan nama lengkap Anda:'
txt_hintname = "Nama lengkap"
txt_hintage = "0"
txt_test1 = 'Berbaring telentang dan ambil denyut nadi Anda selama 15 detik. Klik tombol "Mulai tes pertama" untuk memulai timer.\nCatat hasilnya di kolom yang sesuai.'
txt_test2 = 'Lakukan 30 squat dalam 45 detik. Untuk melakukan ini, klik tombol "Mulai melakukan squat"\nuntuk memulai penghitung squat.'
txt_test3 = 'Berbaring telentang dan ambil denyut nadi Anda selama 15 detik pertama dari menit, kemudian untuk 15 detik terakhir dari menit.\nTekan tombol "Mulai tes akhir" untuk memulai timer.\nDetik yang harus diukur ditunjukkan dengan warna hijau dan detik yang tidak boleh diukur ditunjukkan dengan warna hitam. Catat hasilnya di kolom yang sesuai.'
txt_sendresults = 'Kirim hasil'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Mulai tes pertama'
txt_starttest2 = 'Mulai melakukan squat'
txt_starttest3 = 'Mulai tes akhir'
time = QTime(0, 0, 15)
txt_timer = time.toString("hh:mm:ss")
txt_age = 'Usia penuh:'
txt_finalwin = 'Hasil'
txt_index = 'Indeks Roufier: '
txt_workheart = 'Kinerja jantung: '
txt_res1 = "rendah. Segera temui dokter Anda!"
txt_res2 = "memuaskan. Temui dokter Anda!"
txt_res3 = "rata-rata. Mungkin perlu menemui dokter untuk diperiksa."
txt_res4 = "di atas rata-rata"
txt_res5 = "tinggi"
