class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks
        self.jadwal = []
        self.ruangan = None
        self.dosen_pengampu = None

    def tambah_jadwal(self, jadwal):
        self.jadwal.append(jadwal)

    def set_ruangan(self, ruangan):
        self.ruangan = ruangan

    def set_dosen_pengampu(self, dosen):
        self.dosen_pengampu = dosen


class Dosen:
    def __init__(self, nidn, nama):
        self.nidn = nidn
        self.nama = nama
        self.mata_kuliah_diampu = []

    def tambah_mata_kuliah_diampu(self, mata_kuliah):
        self.mata_kuliah_diampu.append(mata_kuliah)


class Jadwal:
    def __init__(self, hari, jam_mulai, jam_selesai):
        self.hari = hari
        self.jam_mulai = jam_mulai
        self.jam_selesai = jam_selesai


class Ruangan:
    def __init__(self, nomor):
        self.nomor = nomor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.mata_kuliah_terdaftar = []
        self.total_sks_terambil = 0

    def daftar_mata_kuliah(self, mata_kuliah):
        if self.total_sks_terambil + mata_kuliah.sks <= 24:
            self.mata_kuliah_terdaftar.append(mata_kuliah)
            self.total_sks_terambil += mata_kuliah.sks

    def set_nilai(self, mata_kuliah, nilai):
        for mk in self.mata_kuliah_terdaftar:
            if mk.kode == mata_kuliah.kode:
                mk.nilai = nilai
                break


# Membuat objek MataKuliah
matkul1 = MataKuliah("MK001", "Pemweb", 3)
matkul2 = MataKuliah("MK002", "Embedded System", 3)
matkul3 = MataKuliah("MK003", "PBO", 4)

# Membuat objek Jadwal
jadwal1 = Jadwal("Senin", "08:00", "10:00")
jadwal2 = Jadwal("Selasa", "10:00", "12:00")
jadwal3 = Jadwal("Rabu", "13:00", "16:00")

# Membuat objek Ruangan
ruangan1 = Ruangan("A101")
ruangan2 = Ruangan("B201")
ruangan3 = Ruangan("C301")

# Menambahkan jadwal dan ruangan ke mata kuliah
matkul1.tambah_jadwal(jadwal1)
matkul1.set_ruangan(ruangan1)

matkul2.tambah_jadwal(jadwal2)
matkul2.set_ruangan(ruangan2)

matkul3.tambah_jadwal(jadwal3)
matkul3.set_ruangan(ruangan3)

# Membuat objek Dosen
dosen1 = Dosen("001", "Pak Raden Arum")
dosen2 = Dosen("002", "Pak Mona Arif Muda")
dosen3 = Dosen("003", "Pak Puput Budi Wintoro")

# Menambahkan mata kuliah yang diajar oleh dosen
dosen1.tambah_mata_kuliah_diampu(matkul1)
dosen2.tambah_mata_kuliah_diampu(matkul2)
dosen3.tambah_mata_kuliah_diampu(matkul3)

# Membuat objek Mahasiswa
mahasiswa1 = Mahasiswa("2215061007", "Tegar")
mahasiswa2 = Mahasiswa("2215061023", "Pascal")
mahasiswa3 = Mahasiswa("2215061135", "Arnest")

# Mahasiswa mendaftar mata kuliah
mahasiswa1.daftar_mata_kuliah(matkul1)
mahasiswa1.daftar_mata_kuliah(matkul3)

mahasiswa2.daftar_mata_kuliah(matkul1)
mahasiswa2.daftar_mata_kuliah(matkul2)

mahasiswa3.daftar_mata_kuliah(matkul1)
mahasiswa3.daftar_mata_kuliah(matkul2)
mahasiswa3.daftar_mata_kuliah(matkul3)

# Dosen memberikan nilai kepada mahasiswa
mahasiswa1.set_nilai(matkul1, "A")
mahasiswa1.set_nilai(matkul3, "B+")

mahasiswa2.set_nilai(matkul1, "A-")
mahasiswa2.set_nilai(matkul2, "A")

mahasiswa3.set_nilai(matkul1, "A-")
mahasiswa3.set_nilai(matkul2, "B+")
mahasiswa3.set_nilai(matkul3, "B")

# Output
print("Daftar Mata Kuliah:")
for mk in [matkul1, matkul2, matkul3]:
    print("Kode:", mk.kode)
    print("Nama:", mk.nama)
    print("SKS:", mk.sks)
    print("Jadwal:")
    if len(mk.jadwal) > 0:
        for jadwal in mk.jadwal:
            print(f"- Hari: {jadwal.hari}, Jam: {jadwal.jam_mulai}-{jadwal.jam_selesai}")
    else:
        print("-")
    print("Ruangan:", mk.ruangan.nomor if mk.ruangan else "-")
    if mk.dosen_pengampu:
        print("Dosen Pengampu:", mk.dosen_pengampu.nama)
    print()

print("Daftar Mahasiswa:")
for mhs in [mahasiswa1, mahasiswa2, mahasiswa3]:
    print("NIM:", mhs.nim)
    print("Nama:", mhs.nama)
    print("Mata Kuliah Terdaftar:")
    if len(mhs.mata_kuliah_terdaftar) > 0:
        for mk in mhs.mata_kuliah_terdaftar:
            print("- Kode:", mk.kode)
            print("  Nama:", mk.nama)
            print("  SKS:", mk.sks)
            print("  Nilai:", mk.nilai if mk.nilai else "-")
    else:
        print("-")
    print("Total SKS Terambil:", mhs.total_sks_terambil)
    print()