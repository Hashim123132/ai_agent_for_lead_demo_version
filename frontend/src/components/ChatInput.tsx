import { useState } from "react";
import { Send } from "lucide-react";

type Props = {
  onSend: (text: string) => void;
};

export default function ChatInput({ onSend }: Props) {
  const [text, setText] = useState("");

  const handleSend = () => {
    if (!text.trim()) return;
    onSend(text);
    setText("");
  };

  return (
    <div className="p-6 border-t border-zinc-800">
      <div className="max-w-3xl mx-auto flex items-center gap-3 bg-zinc-900 border border-zinc-700 rounded-2xl p-3">
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          placeholder="Ask about car rental or send customer inquiry..."
          className="flex-1 bg-transparent outline-none text-white placeholder:text-zinc-500"
        />

        <button
          onClick={handleSend}
          className="bg-blue-600 hover:bg-blue-700 rounded-xl p-3"
        >
          <Send size={18} />
        </button>
      </div>
    </div>
  );
}