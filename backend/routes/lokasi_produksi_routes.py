from flask import Blueprint, jsonify, request
from models.lokasi_produksi_models import db, LokasiProduksi
from flask_jwt_extended import jwt_required

# Nama blueprint ganti jadi lokasi_produksi_bp
lokasi_produksi_bp = Blueprint('lokasi_produksi', __name__)

# --- READ ---
@lokasi_produksi_bp.route('/lokasi_produksi', methods=['GET'])
@jwt_required()
def get_lokasi_produksi():
    try:
        # Panggil class LokasiProduksi
        data_lokasi = LokasiProduksi.query.all()
        # Variabel item tetap aman dipakai di sini
        hasil_json = [item.to_dict() for item in data_lokasi]

        return jsonify({
            "status": "success",
            "message": "Data lokasi produksi berhasil diambil",
            "data": hasil_json
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# --- INSERT ---
@lokasi_produksi_bp.route('/lokasi_produksi', methods=['POST'])
@jwt_required()
def tambah_lokasi_produksi():
    try:
        data = request.json
        input_nama = data.get('nama_lokasi_produksi')
        input_kabupaten = data.get('id_kabupaten')

        if not input_nama:
            return jsonify({"status": "error", "message": "Nama lokasi produksi kosong!"}), 400
            
        lokasi_baru = LokasiProduksi(
            nama_lokasi_produksi=input_nama,
            id_kabupaten=input_kabupaten
        )

        db.session.add(lokasi_baru)
        db.session.commit()

        return jsonify({"status": "success", "message": "Data lokasi produksi berhasil ditambahkan!"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# --- UPDATE ---
@lokasi_produksi_bp.route('/lokasi_produksi/<int:id_edit>', methods=['PUT'])
@jwt_required()
def edit_lokasi_produksi(id_edit):
    try:
        target = LokasiProduksi.query.get(id_edit)
        if not target:
            return jsonify({"status": "error", "message": "Data tidak ditemukan"}), 404
      
        data = request.json
        
        if data.get('nama_lokasi_produksi'):
            target.nama_lokasi_produksi = data.get('nama_lokasi_produksi')
        
        if data.get('id_kabupaten'):
            target.id_kabupaten = data.get('id_kabupaten')
        
        db.session.commit()

        return jsonify({"status": "success", "message": "Data lokasi produksi berhasil diperbarui!"}), 200
    except Exception as e: 
        return jsonify({"status": "error", "message": str(e)}), 500

# --- DELETE ---
@lokasi_produksi_bp.route('/lokasi_produksi/<int:id_hapus>', methods=['DELETE'])
@jwt_required()
def hapus_lokasi_produksi(id_hapus):
    try: 
        target = LokasiProduksi.query.get(id_hapus)
        if not target:
            return jsonify({"status": "error", "message": "Data tidak ditemukan"}), 404 
        
        db.session.delete(target)
        db.session.commit()

        return jsonify({"status": "success", "message": "Data lokasi produksi berhasil dihapus"}), 200
    except Exception as e: 
        return jsonify({"status": "error", "message": str(e)}), 500