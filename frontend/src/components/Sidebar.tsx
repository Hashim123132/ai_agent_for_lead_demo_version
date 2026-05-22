import { Car, MessageSquare, Users, Settings, Sun, Moon } from "lucide-react";

type Props = {
  theme: "dark" | "light";
  setTheme: (theme: "dark" | "light") => void;
};

export default function Sidebar({ theme, setTheme }: Props) {
  const isDark = theme === "dark";

  return (
    <aside
      className={`w-80 border-r p-5 hidden md:flex flex-col ${
        isDark
          ? "bg-zinc-950 border-zinc-800"
          : "bg-white border-zinc-200"
      }`}
    >
      <h1 className="text-5xl font-bold leading-tight mb-10">
        Rental <br /> Agent
      </h1>

      <nav className="space-y-3">
        <div className={`flex items-center gap-3 rounded-xl px-4 py-3 ${isDark ? "bg-zinc-800" : "bg-zinc-100"}`}>
          <MessageSquare size={18} />
          <span>AI Chat</span>
        </div>

        <div className="flex items-center gap-3 text-zinc-400 px-4 py-3">
          <Car size={18} />
          <span>Rental Leads</span>
        </div>

        <div className="flex items-center gap-3 text-zinc-400 px-4 py-3">
          <Users size={18} />
          <span>Customers</span>
        </div>

        <div className="flex items-center gap-3 text-zinc-400 px-4 py-3">
          <Settings size={18} />
          <span>Settings</span>
        </div>
      </nav>

      <div className="mt-auto space-y-4">
        <div className={`flex rounded-xl p-1 ${isDark ? "bg-zinc-900" : "bg-zinc-100"}`}>
          <button
            onClick={() => setTheme("light")}
            className="flex-1 flex items-center justify-center gap-2 py-2 rounded-lg"
          >
            <Sun size={16} /> Light
          </button>

          <button
            onClick={() => setTheme("dark")}
            className={`flex-1 flex items-center justify-center gap-2 py-2 rounded-lg ${
              isDark ? "bg-zinc-800" : ""
            }`}
          >
            <Moon size={16} /> Dark
          </button>
        </div>

        <p className="text-sm text-zinc-500">Leads save to Google Sheets</p>
      </div>
    </aside>
  );
}