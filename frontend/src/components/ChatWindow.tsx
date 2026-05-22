import { useState } from "react";
import ChatInput from "./ChatInput";

type Message = {
  role: "user" | "ai";
  content: string;
};

export default function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([]);

  const sendMessage = async (text: string) => {
    const userMessage: Message = { role: "user", content: text };
    setMessages((prev) => [...prev, userMessage]);

    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        session_id: "frontend-test-session",
        message: text,
      }),
    });

    const data = await res.json();

    setMessages((prev) => [
      ...prev,
      {
        role: "ai",
        content: data.response,
      },
    ]);
  };

  return (
<main className="flex-1 flex flex-col h-screen overflow-hidden">
        <header className="h-16 border-b border-zinc-800 flex items-center px-6">
        <h2 className="font-semibold">AI Rental Inquiry Agent</h2>
      </header>

<section className="flex-1 overflow-y-auto p-6 min-h-0">
          {messages.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center text-center">
            <h1 className="text-4xl font-bold mb-3">
              Welcome to Rental Agent
            </h1>
            <p className="text-zinc-400 max-w-xl">
              Chat with customers, collect rental details, and automatically save
              qualified leads into Google Sheets.
            </p>
          </div>
        ) : (
          <div className="max-w-3xl mx-auto space-y-4">
            {messages.map((msg, index) => (
              <div
                key={index}
                className={`p-4 rounded-2xl ${
                  msg.role === "user"
                    ? "bg-blue-600 ml-auto max-w-xl"
                    : "bg-zinc-800 mr-auto max-w-xl"
                }`}
              >
                {msg.content}
              </div>
            ))}
          </div>
        )}
      </section>

      <ChatInput onSend={sendMessage} />
    </main>
  );
}