"use client";

import React, { useState, useEffect } from "react";
import { auth } from "../../firebase";

export default function Dashboard() {
  const [messages, setMessages] = useState<{ role: string; content: string }[]>(
    [{ role: "assistant", content: "Hello! How can I help you today?" }]
  );
  const [input, setInput] = useState("");
  const [sliderVisible, setSliderVisible] = useState(false);
  const [expandedStocks, setExpandedStocks] = useState<string[]>([]);
  const [profilePhoto, setProfilePhoto] = useState<string | null>(null);

  useEffect(() => {
    const user = auth.currentUser;
    if (user) {
      setProfilePhoto(user.photoURL);
    }
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    setMessages([...messages, { role: "user", content: input }]);

    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: `This is a simulated response to: "${input}"`,
        },
      ]);
    }, 1000);

    setInput("");
  };

  const toggleSlider = () => {
    setSliderVisible(!sliderVisible);
  };

  const toggleStockNews = (ticker: string) => {
    if (expandedStocks.includes(ticker)) {
      setExpandedStocks(expandedStocks.filter((stock) => stock !== ticker));
    } else {
      setExpandedStocks([...expandedStocks, ticker]);
    }
  };

  const getStockNews = (ticker: string) => {
    const newsMap: Record<string, { title: string; date: string }[]> = {
      BSX: [
        {
          title: "Boston Scientific stock has gained 3% since Q4 earnings",
          date: "Feb 12, 2025",
        },
        {
          title:
            "BSX trading at US$95.65, overvalued by 26% compared to intrinsic value",
          date: "Jan 15, 2025",
        },
      ],
      IRBT: [
        {
          title:
            "iRobot Corporation stock surges over 5%, reaching $8.73 per share",
          date: "Jan 17, 2025",
        },
      ],
      KRG: [
        {
          title:
            "Raymond James drops price objective on Kite Realty Group Trust to $28.00",
          date: "Mar 11, 2025",
        },
        {
          title: "KeyBanc maintains Overweight rating with $31.00 price target",
          date: "Feb 19, 2025",
        },
      ],
      FOX: [
        {
          title: "Wall Street analyst downgraded Fox's stock",
          date: "Jan 21, 2025",
        },
      ],
      MAIN: [
        {
          title:
            "Main Street Capital Corporation selected in random stock pick",
          date: "Mar 26, 2025",
        },
      ],
    };

    return newsMap[ticker] || [{ title: "No recent news available", date: "" }];
  };

  return (
    <div className="flex h-screen bg-gray-100 relative">
      {/* Profile Button */}
      <button
        onClick={() => (window.location.href = "/account-settings")}
        className="fixed top-4 left-4 w-12 h-12 rounded-full flex items-center justify-center shadow-md hover:bg-gray-800 transition-colors"
        style={{
          backgroundImage: profilePhoto ? `url(${profilePhoto})` : "none",
          backgroundSize: "cover",
          backgroundPosition: "center",
          backgroundColor: profilePhoto ? "transparent" : "black",
        }}
      >
        {!profilePhoto && (
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
        )}
      </button>

      {/* Slider Toggle Button */}
      <button
        onClick={toggleSlider}
        className="fixed top-1/2 right-0 transform -translate-y-1/2 w-10 h-10 flex items-center justify-center bg-gray-200 rounded-l-md shadow-md border border-gray-300 text-black z-10"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          className={`transition-transform ${
            sliderVisible ? "rotate-180" : ""
          }`}
        >
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>

      {/* Main Content */}
      <div
        className={`transition-all duration-300 flex flex-col flex-1 overflow-hidden ${
          sliderVisible ? "pr-64" : "pr-0"
        }`}
      >
        {/* Main chat area */}
        <div className="flex-1 overflow-y-auto p-4">
          <div className="max-w-3xl mx-auto">
            {messages.map((message, index) => (
              <div
                key={index}
                className={`mb-4 p-4 rounded-lg ${
                  message.role === "user"
                    ? "bg-blue-100 ml-auto"
                    : "bg-white mr-auto"
                } max-w-[80%]`}
              >
                <p className="text-black">{message.content}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Input area */}
        <div className="border-t border-gray-200 p-4 bg-white">
          <form onSubmit={handleSubmit} className="max-w-3xl mx-auto flex">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type your message..."
              className="flex-1 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button
              type="submit"
              className="ml-2 bg-blue-600 text-white px-4 py-2 rounded-lg"
            >
              Send
            </button>
          </form>
        </div>
      </div>

      {/* Slider Panel */}
      <div
        className={`transition-all duration-300 bg-white border-l border-gray-200 fixed top-0 right-0 h-full overflow-hidden ${
          sliderVisible ? "w-64" : "w-0"
        }`}
      >
        {sliderVisible && (
          <div className="p-4 overflow-y-auto h-full">
            <h3 className="text-lg font-medium mb-4 text-black">
              Stock Watchlist
            </h3>

            {/* Random Stocks List */}
            <div className="space-y-2">
              {["BSX", "IRBT", "KRG", "FOX", "MAIN"].map((ticker, index) => (
                <div key={index} className="border rounded-md overflow-hidden">
                  <button
                    onClick={() => toggleStockNews(ticker)}
                    className="w-full p-3 bg-white flex justify-between items-center hover:bg-gray-50"
                  >
                    <span className="font-medium">{ticker}</span>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="16"
                      height="16"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      className={`transition-transform ${
                        expandedStocks.includes(ticker) ? "rotate-180" : ""
                      }`}
                    >
                      <polyline points="6 9 12 15 18 9"></polyline>
                    </svg>
                  </button>

                  {expandedStocks.includes(ticker) && (
                    <div className="p-3 bg-gray-50 border-t text-sm">
                      {getStockNews(ticker).map((news, i) => (
                        <div
                          key={i}
                          className="mb-2 pb-2 border-b border-gray-200 last:border-0 last:mb-0 last:pb-0"
                        >
                          <p className="font-medium">{news.title}</p>
                          <p className="text-gray-600 text-xs mt-1">
                            {news.date}
                          </p>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
