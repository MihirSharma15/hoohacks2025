import React from "react";
import { RetroGrid } from "./magicui/retro-grid";

const Hero = () => {
  return (
    <div className="flex justify-center items-center h-screen bg-gray-100 text-center p-4">
      <div>
        <h1 className="text-9xl font-bold mb-4">
          Meet <span className="gradient-text">Aura</span>
        </h1>
        <h2 className="text-5xl font-medium mb-6">
          Your Personal Financial Voice Assistant
        </h2>
        <p className="text-2xl max-w-3xl mx-auto">
          Talk to Aura to better understand and manage your finances.
        </p>
        <p className="text-2xl max-w-3xl mx-auto">
          Designed specifically for college students, making financial literacy
          accessible through conversation.
        </p>
      </div>
      <RetroGrid />
    </div>
  );
};

export default Hero;
