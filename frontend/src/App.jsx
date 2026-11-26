import { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {
  Plus,
  MessageSquare,
  ShieldCheck,
  Wifi,
  Camera,
  ClipboardCheck,
  ArrowUp,
  Bot,
  User,
  Menu,
  X,
  BookOpen,
  Sparkles,
} from "lucide-react";



const suggestions = [
  {
    icon: Wifi,
    title: "Connectivity Issues",
    text: "What should I do if my internet disconnects during an exam?",
  },
  {
    icon: Camera,
    title: "Camera Problems",
    text: "My camera is not working during verification.",
  },
  {
    icon: ClipboardCheck,
    title: "Exam Status",
    text: "How can I check the status of my assessment?",
  },
  {
    icon: ShieldCheck,
    title: "Integrity Review",
    text: "What happens if my exam is flagged for review?",
  },
];

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [sidebarOpen, setSidebarOpen] = useState(true);

  const handleSend = async (text = input) => {
    const question = text.trim();
    if (!question) return;

    // Display the user's question
    setMessages((prev) => [
      ...prev,
      { role: "user", text: question },
    ]);

    setInput("");

    // Show loading message
    setMessages((prev) => [
      ...prev,
      { role: "assistant", text: "", loading: true },
    ]);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });

      if (!response.ok) {
        throw new Error("Failed to get response from server");
      }

      const data = await response.json();

      // Replace loading message with actual RAG response
      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          role: "assistant",
          text: data.answer,
          sources: data.sources,
        };

        return updated;
      });
    } catch (error) {
      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          role: "assistant",
          text: "Sorry, I couldn't connect to the ProctorIQ server. Please make sure the backend is running and try again.",
        };

        return updated;
      });
    }
  };
  const newChat = () => {
    setMessages([]);
    setInput("");
  };

  return (
    <div className="min-h-screen bg-[#0b0d12] text-white flex">

      {/* SIDEBAR */}
      {sidebarOpen && (
        <aside className="w-72 bg-[#10131a] border-r border-white/[0.06] p-5 flex flex-col shrink-0">

          {/* Logo */}
          <div className="flex items-center gap-3 mb-8">
            <div className="w-10 h-10 rounded-xl bg-blue-600 flex items-center justify-center shadow-lg shadow-blue-600/20">
              <ShieldCheck size={22} />
            </div>

            <div>
              <h1 className="font-semibold text-lg tracking-tight">ProctorIQ</h1>
              <p className="text-xs text-gray-500">Assessment Support AI</p>
            </div>

            <button
              onClick={() => setSidebarOpen(false)}
              className="ml-auto text-gray-500 hover:text-white"
            >
              <X size={18} />
            </button>
          </div>

          {/* New chat */}
          <button
            onClick={newChat}
            className="flex items-center justify-center gap-2 w-full py-3 rounded-xl bg-blue-600 hover:bg-blue-500 transition font-medium text-sm"
          >
            <Plus size={18} />
            New conversation
          </button>

          {/* History */}
          <div className="mt-9">
            <p className="text-[11px] uppercase tracking-[1.5px] text-gray-500 mb-3">
              Recent conversations
            </p>

            <div className="space-y-1">
              <button className="flex items-center gap-3 w-full text-left p-3 rounded-lg hover:bg-white/[0.04] text-sm text-gray-400">
                <MessageSquare size={16} />
                Exam submission status
              </button>

              <button className="flex items-center gap-3 w-full text-left p-3 rounded-lg hover:bg-white/[0.04] text-sm text-gray-400">
                <MessageSquare size={16} />
                Camera verification issue
              </button>

              <button className="flex items-center gap-3 w-full text-left p-3 rounded-lg hover:bg-white/[0.04] text-sm text-gray-400">
                <MessageSquare size={16} />
                Internet connection problem
              </button>
            </div>
          </div>

          {/* Bottom info */}
          <div className="mt-auto">
            <div className="p-4 rounded-xl bg-[#171c26] border border-white/[0.05]">
              <div className="flex items-center gap-2 mb-2">
                <BookOpen size={15} className="text-blue-400" />
                <span className="text-xs font-medium text-gray-300">
                  Knowledge-based AI
                </span>
              </div>

              <p className="text-[11px] text-gray-500 leading-5">
                Answers grounded in official assessment support documents.
              </p>
            </div>

            <p className="text-[11px] text-gray-600 text-center mt-4">
              ProctorIQ · AI Support Assistant
            </p>
          </div>
        </aside>
      )}

      {/* MAIN */}
      <main className="flex-1 flex flex-col min-w-0">

        {/* HEADER */}
        <header className="h-[72px] border-b border-white/[0.06] flex items-center justify-between px-6 md:px-8 shrink-0">

          <div className="flex items-center gap-3">
            {!sidebarOpen && (
              <button
                onClick={() => setSidebarOpen(true)}
                className="p-2 rounded-lg hover:bg-white/[0.05] text-gray-400"
              >
                <Menu size={19} />
              </button>
            )}

            <div>
              <h2 className="text-sm font-medium">ProctorIQ Assistant</h2>
              <p className="text-xs text-gray-500 mt-1">
                Assessment Support
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-green-500/[0.08] border border-green-500/[0.12]">
            <span className="w-1.5 h-1.5 rounded-full bg-green-400" />
            <span className="text-xs text-green-400">Online</span>
          </div>
        </header>

        {/* CHAT AREA */}
        <section className="flex-1 overflow-y-auto">

          {messages.length === 0 ? (
            /* WELCOME SCREEN */
            <div className="min-h-full flex flex-col items-center justify-center px-5 py-12">

              <div className="w-14 h-14 rounded-2xl bg-blue-500/[0.12] border border-blue-500/[0.15] flex items-center justify-center mb-6">
                <Sparkles size={25} className="text-blue-400" />
              </div>

              <h1 className="text-3xl md:text-4xl font-semibold tracking-tight text-center">
                How can I help you?
              </h1>

              <p className="text-gray-500 text-sm mt-3 text-center max-w-md leading-6">
                Get help with your assessment, technical issues, verification,
                and exam-related questions.
              </p>

              {/* Suggestions */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-10 max-w-2xl w-full">
                {suggestions.map((item, index) => {
                  const Icon = item.icon;

                  return (
                    <button
                      key={index}
                      onClick={() => handleSend(item.text)}
                      className="group text-left p-5 rounded-2xl bg-[#121620] border border-white/[0.06] hover:border-blue-500/30 hover:bg-[#171d2b] transition-all duration-200"
                    >
                      <div className="flex items-center justify-between mb-4">
                        <div className="w-9 h-9 rounded-lg bg-blue-500/[0.08] flex items-center justify-center">
                          <Icon size={17} className="text-blue-400" />
                        </div>

                        <ArrowUp
                          size={15}
                          className="text-gray-600 rotate-45 group-hover:text-blue-400 transition"
                        />
                      </div>

                      <h3 className="text-sm font-medium text-gray-200 mb-1.5">
                        {item.title}
                      </h3>

                      <p className="text-xs text-gray-500 leading-5">
                        {item.text}
                      </p>
                    </button>
                  );
                })}
              </div>

              <div className="flex items-center gap-2 mt-8 text-[11px] text-gray-600">
                <ShieldCheck size={13} />
                <span>Answers based on assessment support information</span>
              </div>
            </div>
          ) : (
            /* MESSAGE SCREEN */
            <div className="max-w-3xl mx-auto px-5 py-8 space-y-8">

              {messages.map((message, index) => (
                <div key={index} className="flex gap-4">

                  <div
                    className={`w-9 h-9 rounded-xl flex items-center justify-center shrink-0 ${message.role === "assistant"
                      ? "bg-blue-600"
                      : "bg-[#242936]"
                      }`}
                  >
                    {message.role === "assistant" ? (
                      <Bot size={18} />
                    ) : (
                      <User size={18} />
                    )}
                  </div>

                  <div className="flex-1 pt-1">
                    <p className="text-xs text-gray-500 mb-2">
                      {message.role === "assistant" ? "ProctorIQ" : "You"}
                    </p>

                    {message.loading ? (
                      <div className="flex items-center gap-2 py-2">
                        <span className="w-2 h-2 rounded-full bg-blue-400 animate-bounce"></span>
                        <span className="w-2 h-2 rounded-full bg-blue-400 animate-bounce [animation-delay:150ms]"></span>
                        <span className="w-2 h-2 rounded-full bg-blue-400 animate-bounce [animation-delay:300ms]"></span>
                        <span className="text-xs text-gray-500 ml-2">ProctorIQ is thinking...</span>
                      </div>
                    ) : (
                      <div className="text-sm text-gray-300 leading-7 markdown-content">
                        <ReactMarkdown remarkPlugins={[remarkGfm]}>
                          {message.text}
                        </ReactMarkdown>
                      </div>
                    )}

                    {/* Sources */}
                    {message.role === "assistant" && message.sources?.length > 0 && (
                      <div className="mt-5 pt-4 border-t border-white/[0.06]">
                        <div className="flex items-center gap-2 mb-3 text-xs text-gray-500">
                          <BookOpen size={14} className="text-blue-400" />
                          <span>Sources used</span>
                        </div>

                        <div className="flex flex-wrap gap-2">
                          {message.sources.map((source, sourceIndex) => (
                            <span
                              key={sourceIndex}
                              className="px-3 py-1.5 rounded-lg bg-[#171c27] border border-white/[0.06] text-xs text-gray-400"
                            >
                              {source.replaceAll("_", " ")}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>

        {/* INPUT */}
        <div className="px-5 pb-5 pt-3 shrink-0">
          <div className="max-w-3xl mx-auto">

            <div className="flex items-end gap-3 bg-[#141821] border border-white/[0.08] focus-within:border-blue-500/40 rounded-2xl p-3 transition">

              <textarea
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === "Enter" && !e.shiftKey) {
                    e.preventDefault();
                    handleSend();
                  }
                }}
                rows={1}
                placeholder="Ask anything about your assessment..."
                className="flex-1 bg-transparent outline-none resize-none text-sm px-2 py-2 placeholder:text-gray-600 max-h-32"
              />

              <button
                onClick={() => handleSend()}
                disabled={!input.trim()}
                className="w-10 h-10 rounded-xl bg-blue-600 hover:bg-blue-500 disabled:bg-gray-700 disabled:text-gray-500 transition flex items-center justify-center shrink-0"
              >
                <ArrowUp size={18} />
              </button>
            </div>

            <p className="text-center text-[10px] text-gray-600 mt-3">
              ProctorIQ may make mistakes. Always verify important information with official support.
            </p>
          </div>
        </div>

      </main>
    </div>
  );
}

export default App;