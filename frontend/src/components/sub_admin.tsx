import React from 'react';

const SubAdminNavbar: React.FC = () => {
  return (
    <nav className="w-full bg-[#D68227] flex items-center justify-between px-6 py-3 shadow-md shrink-0 z-10 relative">
      {/* Left: User Icon */}
      <div className="flex items-center cursor-pointer hover:opacity-80 transition">
        <div className="w-10 h-10 rounded-full border-[2.5px] border-black flex items-center justify-center bg-transparent">
          <svg className="w-7 h-7 text-black" fill="currentColor" viewBox="0 0 24 24">
             <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
          </svg>
        </div>
      </div>
      
      {/* Center: Title */}
      <div className="absolute left-1/2 transform -translate-x-1/2">
        <h1 className="text-white text-3xl font-serif tracking-wider">JamuKita</h1>
      </div>

      {/* Right: Spacer for balancing the flex layout */}
      <div className="w-10"></div>
    </nav>
  );
};

export default SubAdminNavbar;