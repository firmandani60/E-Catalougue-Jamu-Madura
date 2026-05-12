from flask import Blueprint, jsonify, request
from models.lokasi_pemasaran_models import db, LokasiPemasaran
from flask_jwt_extended import jwt_required

lokasi_pemasaran_bp = Blueprint('lokasi_pemasaran', __name__)

# --- READ (TAMPILKAN SEMUA) ---
@lokasi_pemasaran_bp.route('/lokasi_pemasaran', methods=['GET'])
@jwt_required()
def get_lokasi_pemasaran():
    try:
        # FIX: Panggil class LokasiPemasaran (L dan P besar)
        data_lokasi = LokasiPemasaran.query.all()
        # Pakai 'item' biar nggak nabrak nama class
        hasil_json = [item.to_dict() for item in data_lokasi]

        return jsonify({
            "status": "success",
            "message": "Data lokasi pemasaran berhasil diambil",
            "data": hasil_json
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# --- INSERT (TAMBAH DATA) ---
@lokasi_pemasaran_bp.route('/lokasi_pemasaran', methods=['POST'])
@jwt_required()
def tambah_lokasi_pemasaran():
    try:
        data = request.json
        input_nama = data.get('nama_lokasi_pemasaran')

        if not input_nama:
            return jsonify({
                "status": "error", 
                "message": "Nama lokasi pemasaran tidak boleh kosong!"
            }), 400

        # FIX: Panggil class LokasiPemasaran
        lokasi_baru = LokasiPemasaran(nama_lokasi_pemasaran=input_nama)
        db.session.add(lokasi_baru)
        db.session.commit()

        return jsonify({
            "status": "success", 
            "message": "Data lokasi pemasaran berhasil ditambahkan!"
        }), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# --- UPDATE (EDIT DATA) ---
@lokasi_pemasaran_bp.route('/lokasi_pemasaran/<int:id_edit>', methods=['PUT'])
@jwt_required()
def edit_lokasi_pemasaran(id_edit):
    try:
        # FIX: Panggil class LokasiPemasaran
        target = LokasiPemasaran.query.get(id_edit)

        if not target:
            return jsonify({
                "status": "error",
                "message": "Data lokasi pemasaran tidak ditemukan"
            }), 404
        
        data = request.json
        input_nama_baru = data.get('nama_lokasi_pemasaran')

        if not input_nama_baru:
             return jsonify({
                "status": "error", 
                "message": "Nama lokasi pemasaran baru tidak boleh kosong!"
            }), 400

        target.nama_lokasi_pemasaran = input_nama_baru
        db.session.commit()

        return jsonify({
            "status": "success", 
            "message": "Data lokasi pemasaran berhasil diupdate!"
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# --- DELETE (HAPUS DATA) ---
@lokasi_pemasaran_bp.route('/lokasi_pemasaran/<int:id_hapus>', methods=['DELETE'])
@jwt_required()
def hapus_lokasi_pemasaran(id_hapus):
    try: 
        # FIX: Panggil class LokasiPemasaran
        target = LokasiPemasaran.query.get(id_hapus)

        if not target:
            return jsonify({
                "status": "error",
                "message": "Data lokasi pemasaran tidak ditemukan"
            }), 404 
        
        db.session.delete(target)
        db.session.commit()

        return jsonify({
            "status": "success", 
            "message": "Data lokasi pemasaran berhasil dihapus"
        }), 200
    except Exception as e: 
        return jsonify({"status": "error", "message": str(e)}), 500