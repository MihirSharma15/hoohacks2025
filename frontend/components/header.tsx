"use client";
import { Button } from "@/components/ui/button";
import { useRouter } from "next/router";
import { RainbowButton } from "./magicui/rainbow-button";

type headerProps = {
  buttonOneOnClick?: () => void;
  buttonTwoOnClick?: () => void;
  loginOnClick?: () => void;
};

export default function Header({ loginOnClick }: headerProps) {
  return (
    <header className="fixed top-0 left-0 w-full z-50 flex justify-between items-center px-6 py-4 bg-white shadow-md">
      <div className="flex items-center">
        <span className="text-2xl font-bold gradient-text">Aura</span>
      </div>
      <div className="flex space-x-4 items-stretch">
        <Button variant="outline" className="h-full">
          Features
        </Button>
        <Button variant="outline" className="h-full">
          How It Works
        </Button>
        <RainbowButton onClick={loginOnClick} className="h-full">
          Get Started
        </RainbowButton>
      </div>
    </header>
  );
}
