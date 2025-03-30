"use client";

import Header from "@/components/header";
import Hero from "@/components/Hero";
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();

  return (
    <div>
      <Header
        loginOnClick={() => {
          router.push("/login");
        }}
      />
      <Hero />
    </div>
  );
}
