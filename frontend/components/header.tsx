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
    <header className="flex justify-between items-center px-6 py-4 bg-white shadow-md">
      <div className="flex items-center">
        <span className="text-2xl font-bold gradient-text">Aura</span>
      </div>
      <div className="flex space-x-4">
        <Button variant="outline">Feature 1</Button>
        <Button variant="outline">Feature 2</Button>
        <RainbowButton onClick={loginOnClick}>Get Started</RainbowButton>
      </div>
    </header>
  );
}
