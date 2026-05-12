# Import db dari file model yang sudah ada (misal kabupaten)
from models.kabupaten_models import db 

class Jamu(db.Model):
    __tablename__ = "jamu"

    id_jamu = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_jamu = db.Column(db.String(255), nullable=False)
    khasiat = db.Column(db.Text)
    kandungan = db.Column(db.Text)
    aturan_minum = db.Column(db.Text)
    efek_samping = db.Column(db.Text)

    # FK - Nyambung ke tabel lain
    id_jenis = db.Column(db.Integer, db.ForeignKey('jenis.id_jenis'))
    id_produsen = db.Column(db.Integer, db.ForeignKey('produsen.id_produsen'))
    id_lokasi_produksi = db.Column(db.Integer, db.ForeignKey('lokasi_produksi.id_lokasi_produksi'))
    id_kabupaten = db.Column(db.Integer, db.ForeignKey('kabupaten.id_kabupaten'))
    id_perizinan = db.Column(db.Integer, db.ForeignKey('perizinan.id_perizinan'))
    id_lokasi_pemasaran = db.Column(db.Integer, db.ForeignKey('lokasi_pemasaran.id_lokasi_pemasaran'))

    # Hubungan Relasi biar bisa manggil nama (bukan cuma ID)
    jenis_rel = db.relationship('JenisJamu', backref='jamu_list', lazy=True)
    produsen_rel = db.relationship('Produsen', backref='jamu_list', lazy=True)
    lokasi_produksi_rel = db.relationship('LokasiProduksi', backref='jamu_list', lazy=True)
    kabupaten_rel = db.relationship('Kabupaten', backref='jamu_list', lazy=True)
    perizinan_rel = db.relationship('Perizinan', backref='jamu_list', lazy=True)
    lokasi_pemasaran_rel = db.relationship('LokasiPemasaran', backref='jamu_list', lazy=True)

    def to_dict(self):
        return {
            "id_jamu": self.id_jamu,
            "nama_jamu": self.nama_jamu,
            "khasiat": self.khasiat,
            "kandungan": self.kandungan,
            "aturan_minum": self.aturan_minum,
            "efek_samping": self.efek_samping,
            
            "id_jenis": self.id_jenis,
            "id_produsen": self.id_produsen,
            "id_lokasi_produksi": self.id_lokasi_produksi,
            "id_kabupaten": self.id_kabupaten,
            "id_perizinan": self.id_perizinan,
            "id_lokasi_pemasaran": self.id_lokasi_pemasaran,

            # Ambil datanya kalau relasinya ada (biar gak error NoneType)
            "nama_jenis": self.jenis_rel.nama_jenis if self.jenis_rel else None,
            "nama_produsen": self.produsen_rel.nama_produsen if self.produsen_rel else None,
            "nama_lokasi_produksi": self.lokasi_produksi_rel.nama_lokasi_produksi if self.lokasi_produksi_rel else None,
            "nama_kabupaten": self.kabupaten_rel.nama_kabupaten if self.kabupaten_rel else None,
            "nama_perizinan": self.perizinan_rel.nama_perizinan if self.perizinan_rel else None,
            "nama_lokasi_pemasaran": self.lokasi_pemasaran_rel.nama_lokasi_pemasaran if self.lokasi_pemasaran_rel else None
        }