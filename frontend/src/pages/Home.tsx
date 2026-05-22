import { useState } from "react";
import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";

export default function Home() {
  const [theme, setTheme] = useState<"dark" | "light">("dark");

  return (
    <div
      className={
        theme === "dark"
          ? "min-h-screen w-full bg-zinc-950 text-white flex"
          : "min-h-screen w-full bg-zinc-100 text-zinc-950 flex"
      }
    >
      <Sidebar theme={theme} setTheme={setTheme} />
      <ChatWindow theme={theme} />
    </div>
  );
}