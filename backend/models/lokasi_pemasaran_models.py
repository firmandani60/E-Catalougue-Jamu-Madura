from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LokasiPemasaran(db.Model): 
    __tablename__ = "lokasi_pemasaran"

    id_lokasi_pemasaran = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    nama_lokasi_pemasaran = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id_lokasi_pemasaran": self.id_lokasi_pemasaran,
            "nama_lokasi_pemasaran": self.nama_lokasi_pemasaran
        }