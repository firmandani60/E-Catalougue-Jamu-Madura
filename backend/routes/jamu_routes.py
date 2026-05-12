from flask import Blueprint, jsonify, request
from models.jamu_models import db, Jamu
from flask_jwt_extended import jwt_required

jamu_bp = Blueprint('jamu', __name__)

@jamu_bp.route('/jamu', methods=['GET'])
@jwt_required()
def get_jamu():
    try:
        data_jamu = Jamu.query.all()
        
        hasil_json = [item.to_dict() for item in data_jamu]

        return jsonify({
            "status": "success",
            "message": "Data Jamu berhasil diambil",
            "data": hasil_json
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# --- 2. INSERT (Tambah Jamu Baru - Banyak Input) ---
@jamu_bp.route('/jamu', methods=['POST'])
@jwt_required()
def tambah_jamu():
    try:
        data = request.json
        
        jamu_baru = Jamu(
            nama_jamu=data.get('nama_jamu'),
            khasiat=data.get('khasiat'),
            kandungan=data.get('kandungan'),
            aturan_minum=data.get('aturan_minum'),
            efek_samping=data.get('efek_samping'),
            
            # Ini nih kumpulan FK-nya Bang
            id_jenis=data.get('id_jenis'),
            id_produsen=data.get('id_produsen'),
            id_lokasi_produksi=data.get('id_lokasi_produksi'),
            id_kabupaten=data.get('id_kabupaten'),
            id_perizinan=data.get('id_perizinan'),
            id_lokasi_pemasaran=data.get('id_lokasi_pemasaran')
        )

        db.session.add(jamu_baru)
        db.session.commit()

        return jsonify({
            "status": "success",
            "message": f"Jamu {jamu_baru.nama_jamu} berhasil didaftarkan!"
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

# --- 3. UPDATE (Edit Jamu) ---
@jamu_bp.route('/jamu/<int:id_edit>', methods=['PUT'])
@jwt_required()
def edit_jamu(id_edit):
    try:
        target = Jamu.query.get(id_edit)
        if not target:
            return jsonify({"status": "error", "message": "Jamu tidak ditemukan"}), 404
        
        data = request.json
        
        # Update field teks
        target.nama_jamu = data.get('nama_jamu', target.nama_jamu)
        target.khasiat = data.get('khasiat', target.khasiat)
        target.kandungan = data.get('kandungan', target.kandungan)
        target.aturan_minum = data.get('aturan_minum', target.aturan_minum)
        target.efek_samping = data.get('efek_samping', target.efek_samping)
        
        # Update field Foreign Key (ID)
        target.id_jenis = data.get('id_jenis', target.id_jenis)
        target.id_produsen = data.get('id_produsen', target.id_produsen)
        target.id_lokasi_produksi = data.get('id_lokasi_produksi', target.id_lokasi_produksi)
        target.id_kabupaten = data.get('id_kabupaten', target.id_kabupaten)
        target.id_perizinan = data.get('id_perizinan', target.id_perizinan)
        target.id_lokasi_pemasaran = data.get('id_lokasi_pemasaran', target.id_lokasi_pemasaran)

        db.session.commit()
        return jsonify({"status": "success", "message": "Data Jamu berhasil diupdate"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

# --- 4. DELETE ---
@jamu_bp.route('/jamu/<int:id_hapus>', methods=['DELETE'])
@jwt_required()
def hapus_jamu(id_hapus):
    try:
        target = Jamu.query.get(id_hapus)
        if not target:
            return jsonify({"status": "error", "message": "Data tidak ditemukan"}), 404
        
        db.session.delete(target)
        db.session.commit()
        return jsonify({"status": "success", "message": "Jamu berhasil dihapus"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500