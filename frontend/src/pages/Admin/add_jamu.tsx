import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import NavbarAdmin from '../../components/navbar_admin';

export default function AddJamu() {
  const navigate = useNavigate();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  const handleLogout = () => {
    const konfirmasi = window.confirm("Yakin mau logout, Bang?");
    if (konfirmasi) {
      localStorage.removeItem('token_jamu');
      navigate('/4dm13n'); 
    }
  };

  return (
    <div className={`flex flex-col h-screen bg-[#FDFBF7] font-sans overflow-hidden transition-all duration-700 ease-in-out ${mounted ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
      {/* Top Navbar */}
      <NavbarAdmin onLogout={handleLogout} />
      
      <div className="flex flex-1 overflow-hidden">
        {/* Sidebar */}
        <aside className="w-56 h-full bg-[#F5F2EA] flex flex-col border-r border-[#E5DECD] shrink-0">
          <div className="flex items-center gap-3 px-5 py-6">
            <div className="w-12 h-12 rounded-full bg-black border-2 border-black flex items-center justify-center shrink-0">
              <svg className="w-7 h-7 text-white" fill="currentColor" viewBox="0 0 24 24">
                 <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
              </svg>
            </div>
            <div className="flex flex-col">
              <span className="font-bold text-[15px] text-black leading-tight">Nama user</span>
              <span className="text-[10px] text-gray-800 italic mt-0.5">Administrator</span>
            </div>
          </div>

          <div className="px-3 mt-2">
            <button 
              onClick={() => navigate('/dashboard_4dm13n')}
              className="w-full bg-[#D68227] hover:bg-[#c47522] text-black font-bold rounded-lg py-2.5 px-4 flex items-center gap-3 shadow-md transition-colors"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
              <span className="text-[15px] tracking-wide">Dashboard</span>
            </button>
          </div>

          <div className="mt-auto px-4 pb-6">
            <button 
              onClick={handleLogout}
              className="w-full bg-[#CC0000] hover:bg-[#FF0404] text-white font-bold text-[15px] rounded-lg py-2.5 px-4 flex items-center justify-center shadow-md transition-colors"
            >
              Log out
            </button>
          </div>
        </aside>

        {/* Main Content */}
        <main className="flex-1 flex flex-col h-full overflow-y-auto bg-[#FDFBF7]">
          {/* HEADER */}
          <header className="bg-[#344F51] text-white px-8 py-5 flex items-center shadow-md shrink-0 z-10">
            <div className="flex items-center gap-3">
              <svg className="w-8 h-8 text-white/90" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
              <h1 className="text-xl font-semibold tracking-wide">Add jamu</h1>
            </div>
          </header>

          {/* CONTENT FORM */}
          <div className="p-8 flex-1 flex justify-center">
            <div className={`w-full max-w-5xl bg-[#FCE6CF] rounded-xl shadow-lg p-6 flex flex-col gap-4 border border-[#F0D5BB] transition-all duration-1000 delay-100 ease-out transform ${mounted ? 'opacity-100 scale-100' : 'opacity-0 scale-95'}`}>
              
              {/* Row 1: Nama jamu */}
              <div className="flex flex-col gap-1">
                <label className="text-black font-bold text-sm font-serif">Nama jamu</label>
                <input 
                  type="text" 
                  placeholder="Nama jamu" 
                  className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:border-[#D68227] focus:ring-1 focus:ring-[#D68227]"
                />
              </div>

              {/* Row 2: Khasiat & Kandungan */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="flex flex-col gap-1">
                  <label className="text-black font-bold text-sm font-serif">Khasiat</label>
                  <textarea 
                    className="w-full h-32 rounded-md bg-[#D68227] text-white placeholder-white/70 border-none p-3 text-sm resize-none focus:outline-none focus:ring-2 focus:ring-orange-600 shadow-inner"
                  ></textarea>
                </div>
                <div className="flex flex-col gap-1">
                  <label className="text-black font-bold text-sm font-serif">Kandungan</label>
                  <textarea 
                    className="w-full h-32 rounded-md bg-[#D68227] text-white placeholder-white/70 border-none p-3 text-sm resize-none focus:outline-none focus:ring-2 focus:ring-orange-600 shadow-inner"
                  ></textarea>
                </div>
              </div>

              {/* Row 3: Aturan Minum & Efek Samping */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="flex flex-col gap-1">
                  <label className="text-black font-bold text-sm font-serif">Aturan Minum</label>
                  <textarea 
                    placeholder="ketik disini"
                    className="w-full h-16 rounded-md bg-white border border-gray-300 p-3 text-sm resize-none focus:outline-none focus:border-[#D68227] focus:ring-1 focus:ring-[#D68227]"
                  ></textarea>
                </div>
                <div className="flex flex-col gap-1">
                  <label className="text-black font-bold text-sm font-serif">Efek Samping</label>
                  <textarea 
                    placeholder="ketik disini"
                    className="w-full h-16 rounded-md bg-white border border-gray-300 p-3 text-sm resize-none focus:outline-none focus:border-[#D68227] focus:ring-1 focus:ring-[#D68227]"
                  ></textarea>
                </div>
              </div>

              {/* Row 4: Produsen & Lokasi Produksi */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="flex flex-col gap-1">
                  <label className="text-black font-bold text-sm font-serif">Produsen</label>
                  <div className="relative h-64 bg-[#D68227] rounded-md shadow-inner overflow-hidden flex flex-col">
                    <div className="flex justify-center pt-2 pb-1 text-white opacity-80">
                      <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" /></svg>
                    </div>
                    <select 
                      multiple
                      className="flex-1 w-full bg-transparent text-white border-none px-2 pb-3 text-[13px] font-medium focus:outline-none overflow-y-auto custom-scrollbar appearance-none text-center"
                    >
                      <option className="py-1">Madura Sari</option>
                      <option className="py-1">Jamu Tradisional Madura</option>
                      <option className="py-1">Jamu Assegaf</option>
                      <option className="py-1">Jamu Intan</option>
                      <option className="py-1">Sari Madu</option>
                      <option className="py-1">Firdaus Kurnia Indah</option>
                      <option className="py-1">Kampung Paseraman Kamal</option>
                      <option className="py-1">Njonja Bolan</option>
                      <option className="py-1">Jamu Pusaka Kraton Cakraningrat</option>
                      <option className="py-1">Jamu Putri Bangkalan</option>
                      <option className="py-1">Mustika Madura</option>
                      <option className="py-1">TOKO NUR</option>
                      <option className="py-1">TOKO BU EMA</option>
                      <option className="py-1">Warda</option>
                      <option className="py-1">TOKO ANGGREK</option>
                    </select>
                  </div>
                </div>

                <div className="flex flex-col gap-1">
                  <label className="text-black font-bold text-sm font-serif">Lokasi Produksi</label>
                  <div className="relative h-64 bg-[#D68227] rounded-md shadow-inner overflow-hidden flex flex-col">
                    <div className="flex justify-center pt-2 pb-1 text-white opacity-80">
                      <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" /></svg>
                    </div>
                    <select 
                      multiple
                      className="flex-1 w-full bg-transparent text-white border-none px-2 pb-3 text-[13px] font-medium focus:outline-none overflow-y-auto custom-scrollbar appearance-none text-center"
                    >
                      <option className="py-1">JL Pahlawan 21 Sampang</option>
                      <option className="py-1">BURNEH</option>
                      <option className="py-1">Klobungan Jeddih</option>
                      <option className="py-1">Jl. Ki Lemur Duwur Bangkalan</option>
                      <option className="py-1">Bancaran</option>
                      <option className="py-1">Jl.Jokotole No..20</option>
                      <option className="py-1">Jl.Jokotole No..21</option>
                      <option className="py-1">Jl.Jokotole No..22</option>
                      <option className="py-1">Jl.Jokotole No..23</option>
                      <option className="py-1">Jl. Kabupaten, Gladak Anyar Pamekasan</option>
                      <option className="py-1">Jl.Anggrek, Lingkungan Delama</option>
                    </select>
                  </div>
                </div>
              </div>

              {/* Row 5: Jenis jamu, Perizinan, Kabupaten */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="flex flex-col gap-1">
                  <label className="text-black font-bold text-sm text-center font-serif">Jenis jamu</label>
                  <div className="relative h-32 bg-[#D68227] rounded-md shadow-inner overflow-hidden flex flex-col">
                    <div className="flex justify-center pt-1.5 pb-0.5 text-white opacity-80">
                      <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" /></svg>
                    </div>
                    <select 
                      multiple
                      className="flex-1 w-full bg-transparent text-white border-none px-2 pb-2 text-[13px] font-medium focus:outline-none overflow-y-auto custom-scrollbar appearance-none text-center"
                    >
                      <option className="py-1">Pil</option>
                      <option className="py-1">Cair</option>
                      <option className="py-1">Serbuk</option>
                      <option className="py-1">Kapsul</option>
                      <option className="py-1">Selai</option>
                      <option className="py-1">Krim</option>
                    </select>
                  </div>
                </div>

                <div className="flex flex-col gap-1">
                  <label className="text-black font-bold text-sm text-center font-serif">Perizinan</label>
                  <div className="relative h-32 bg-[#D68227] rounded-md shadow-inner overflow-hidden flex flex-col">
                    <div className="flex justify-center pt-1.5 pb-0.5 text-white opacity-80">
                      <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" /></svg>
                    </div>
                    <select 
                      multiple
                      className="flex-1 w-full bg-transparent text-white border-none px-2 pb-2 text-[13px] font-medium focus:outline-none overflow-y-auto custom-scrollbar appearance-none text-center"
                    >
                      <option className="py-1">P-IRT</option>
                      <option className="py-1">BPOM</option>
                      <option className="py-1">KEMENKES</option>
                      <option className="py-1">TDI & UKOT</option>
                    </select>
                  </div>
                </div>

                <div className="flex flex-col gap-1">
                  <label className="text-black font-bold text-sm text-center font-serif">Kabupaten</label>
                  <div className="relative h-32 bg-[#D68227] rounded-md shadow-inner overflow-hidden flex flex-col">
                    <div className="flex justify-center pt-1.5 pb-0.5 text-white opacity-80">
                      <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" /></svg>
                    </div>
                    <select 
                      multiple
                      className="flex-1 w-full bg-transparent text-white border-none px-2 pb-2 text-[13px] font-medium focus:outline-none overflow-y-auto custom-scrollbar appearance-none text-center"
                    >
                      <option className="py-1">Bangkalan</option>
                      <option className="py-1">Sampang</option>
                      <option className="py-1">Pamekasan</option>
                      <option className="py-1">Sumenep</option>
                    </select>
                  </div>
                </div>
              </div>

              {/* Row 6: Upload Gambar */}
              <div className="flex flex-col gap-1 mt-2">
                <label className="text-black font-bold text-sm font-serif">Upload Gambar</label>
                <div className="bg-white rounded-md border border-gray-300 p-2 flex items-center gap-3">
                  <button className="bg-[#E5E7EB] hover:bg-gray-300 text-gray-700 text-xs font-semibold py-1.5 px-3 rounded shadow-sm border border-gray-400">
                    Upload File
                  </button>
                  <div className="bg-[#E5E7EB] text-gray-700 w-6 h-6 flex items-center justify-center font-bold rounded shadow-sm border border-gray-400 cursor-pointer hover:bg-gray-300">
                    +
                  </div>
                  <span className="text-sm text-gray-600 truncate">x images__2_-removebg-preview.png</span>
                </div>
                <p className="text-[10px] text-gray-600 italic mt-1">*Format file yang didukung: .jpg, .png, .jpeg. Ukuran maksimal 2 MB.</p>
              </div>

              {/* Row 7: Buttons */}
              <div className="flex justify-end gap-3 mt-2">
                {/* Simpan */}
                <button className="bg-[#FFD700] hover:bg-[#E6C200] text-black text-[13px] font-bold py-2 px-6 rounded flex items-center gap-2 shadow-sm hover:scale-105 transition-transform">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" />
                  </svg>
                  Simpan
                </button>

                {/* Batal */}
                <button 
                  onClick={() => navigate('/dashboard_4dm13n')}
                  className="bg-[#8B0000] hover:bg-[#660000] text-white text-[13px] font-bold py-2 px-6 rounded flex items-center gap-2 shadow-sm hover:scale-105 transition-transform"
                >
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                  Batal
                </button>
              </div>

            </div>
          </div>
        </main>
      </div>

      <style>{`
        .custom-scrollbar::-webkit-scrollbar {
          width: 8px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: rgba(255, 255, 255, 0.1); 
          border-radius: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: rgba(255, 255, 255, 0.5); 
          border-radius: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: rgba(255, 255, 255, 0.8); 
        }
        option:checked {
          background-color: rgba(255,255,255,0.2) !important;
          color: white;
        }
      `}</style>
    </div>
  );
}
