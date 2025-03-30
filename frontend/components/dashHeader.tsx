"use client";
import { Button } from "@/components/ui/button";
import { useRouter } from "next/router";
import { RainbowButton } from "./magicui/rainbow-button";

type DHProps = { onClick: () => void };

export default function DashHeader({ onClick }: DHProps) {
  return (
    <header className="fixed top-0 left-0 w-full z-50 flex justify-between items-center px-6 py-4 bg-white shadow-md">
      <button
        onClick={onClick}
        className="w-12 h-12 bg-black rounded-full flex items-center justify-center shadow-md hover:bg-gray-800 transition-colors z-10"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="white"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
      </button>

      <div className="flex-1 flex justify-center">
        <span className="text-4xl font-bold gradient-text">Aura</span>
      </div>

      <div className="flex items-center">
        {/* You can add any account-related buttons here */}
      </div>
    </header>
  );
}
