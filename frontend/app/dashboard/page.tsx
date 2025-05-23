"use client";

import React, { useState, useEffect, useRef } from "react";
import { getBatchStockData } from "../api/stock";
import { Card, CardDescription, CardHeader } from "@/components/ui/card";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import DashHeader from "@/components/dashHeader";

// Account Settings Modal Component
export function AccountSettingsModal({ isOpen, onClose }) {
  const handleSubmit = (e) => {
    e.preventDefault();
    alert("This is a static page. No actual update will occur.");
  };

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="max-w-md">
        <DialogHeader>
          <DialogTitle>Account Settings</DialogTitle>
        </DialogHeader>

        <div className="space-y-6">
          <div>
            <h2 className="text-lg font-medium">Update Email</h2>
            <form onSubmit={handleSubmit} className="space-y-4 mt-2">
              <Input type="password" placeholder="Current Password" required />
              <Input type="email" placeholder="New Email" required />
              <Button type="submit" className="w-full">
                Update Email
              </Button>
            </form>
          </div>

          <div>
            <h2 className="text-lg font-medium">Update Password</h2>
            <form onSubmit={handleSubmit} className="space-y-4 mt-2">
              <Input type="password" placeholder="Current Password" required />
              <Input type="password" placeholder="New Password" required />
              <Input
                type="password"
                placeholder="Confirm New Password"
                required
              />
              <Button type="submit" className="w-full">
                Update Password
              </Button>
            </form>
          </div>
        </div>

        <DialogClose asChild>
          <Button variant="ghost" className="absolute top-4 right-4"></Button>
        </DialogClose>
      </DialogContent>
    </Dialog>
  );
}

export default function Dashboard() {
  const [messages, setMessages] = useState<
    { role: string; content: string; articles: any }[]
  >([
    {
      role: "assistant",
      content: "Hello! How can I help you today?",
      articles: [],
    },
  ]);
  const [input, setInput] = useState("");
  const [isRecording, setIsRecording] = useState(false);
  const [sliderVisible, setSliderVisible] = useState(false);
  const [expandedStocks, setExpandedStocks] = useState<string[]>([]);
  const [showAccountModal, setShowAccountModal] = useState(false);
  const data = [""];

  const wsRef = useRef(null);

  const [articles, setArticles] = useState([]);

  useEffect(() => {
    wsRef.current = new WebSocket("ws://localhost:8000/ws");

    wsRef.current.onopen = () => {
      console.log("WebSocket connection established");
    };

    wsRef.current.onmessage = (event) => {
      console.log("Received data:", event.data);
      
      // First check if it's a string
      if (typeof event.data === 'string') {
        console.log(event.data)
        // Try to determine if it looks like JSON
        if (event.data.trim().startsWith('{')) {
          console.log(2)
          try {
            console.log(3)
            // Attempt to parse as JSON
            const data = JSON.parse(event.data);
            
            // If successful, process as assistant message
            if (data.summary && data.articles) {
              console.log(4)
              setMessages((prev) => [
                ...prev,
                {
                  role: "assistant",
                  content: data.summary,
                  articles: data.articles,
                },
              ]);
              setArticles(data.articles);
            } else {
              console.log(5)
              // JSON without expected structure
              setMessages((prev) => [
                ...prev,
                { role: "assistant", content: JSON.stringify(data), articles: [] },
              ]);
            }
          } catch {
            console.log(6)
            // If it looks like JSON but isn't valid, treat as user message
            setMessages((prev) => [
              ...prev,
              { role: "user", content: event.data, articles: [] },
            ]);
          }
        } else {
          console.log(7)
          // Definitely not JSON, treat as user message
          setMessages((prev) => [
            ...prev,
            { role: "user", content: event.data, articles: [] },
          ]);
        }
      } else {
        console.log(9)
        // Non-string data (unlikely in this case)
        console.log("Received non-string data");
      }
    };
    
    

    wsRef.current.onclose = () => {
      console.log("WebSocket connection closed");
    };

    return () => {
      if (wsRef.current) {
        wsRef.current.close();
      }
    };
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    // Add user message to chat
    setMessages((prev) => [
      ...prev,
      { role: "user", content: input, articles: [] },
    ]);

    // Send message via WebSocket
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(input);
    }

    setInput("");
  };

  // Handle audio recording
  const toggleRecording = async () => {
    if (isRecording) {
      setIsRecording(false);
      // Stop recording logic here
    } else {
      setIsRecording(true);
      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          audio: true,
        });
        const mediaRecorder = new MediaRecorder(stream);
        const audioChunks = [];

        mediaRecorder.ondataavailable = (event) => {
          audioChunks.push(event.data);
        };

        mediaRecorder.onstop = () => {
          const audioBlob = new Blob(audioChunks);
          if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
            wsRef.current.send(audioBlob);
          }
        };

        mediaRecorder.start();

        // Stop recording after 5 seconds for testing
        setTimeout(() => {
          mediaRecorder.stop();
          setIsRecording(false);
        }, 5000);
      } catch (err) {
        console.error("Error accessing microphone:", err);
        setIsRecording(false);
      }
    }
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

  const [stockTickers, setStockTickers] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      setSelectedFile(e.target.files[0]);
    }
    const file = e.target.files[0];

    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        const csv = event.target.result;
        const lines = csv.split("\n");
        const headers = lines[0].split(",");
        const symbolIndex = headers.indexOf("symbol");

        if (symbolIndex !== -1) {
          const tickers = new Set();
          for (let i = 1; i < lines.length; i++) {
            const values = lines[i].split(",");
            if (values[symbolIndex]) {
              tickers.add(values[symbolIndex].trim());
            }
          }
          setStockTickers(Array.from(tickers));
        }
      };
      reader.readAsText(file);
    }
  };

  const [stockData, setStockData] = useState([]);

  useEffect(() => {
    async function fetchStockData() {
      if (stockTickers.length > 0) {
        const data = await getBatchStockData(stockTickers);
        setStockData(data);
      }
    }
    fetchStockData();
  }, [stockTickers]);

  const getStockNews = (ticker: string) => {
    // This would ideally come from an API
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
      <DashHeader onClick={() => setShowAccountModal(true)} />
      {/* Profile Button */}

      {/* Main Content */}
      <div
        className={`transition-all duration-300 flex flex-col flex-1 overflow-hidden pt-16 ${
          sliderVisible ? "pr-64" : "pr-0"
        }`}
      >
        {/* Main chat area */}
        <div className="flex-1 overflow-y-auto p-4">
          <div className="max-w-3xl mx-auto">
            {messages.map((message, index) => (
              <div key={index}>
                {/* Message with gradient border */}
                <div
                  className={`mb-2 mt-2 max-w-[80%] ${
                    message.role === "user" ? "ml-auto" : "mr-auto"
                  }`}
                >
                  <div
                    className={`${
                      message.role === "assistant"
                        ? "border-3 border-transparent bg-clip-padding bg-gradient-to-r from-blue-500 to-green-500 p-[2px] mb-4"
                        : ""
                    } rounded-md`}
                  >
                    <div
                      className={`${
                        message.role === "user" ? "bg-blue-100" : "bg-white"
                      } p-4 rounded-md`}
                    >
                      <p className="text-black">{message.content}</p>
                    </div>
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  {/* Begin source cards */}
                  {message.role === "assistant" &&
                    articles &&
                    message.articles.map((article, index) => (
                      <Card
                        className="w-[350px] cursor-pointer"
                        key={index}
                        onClick={() => window.open(article.url, "_blank")}
                      >
                        <div className="p-4">
                          <CardHeader className="font-bold">
                            {article.title}
                          </CardHeader>
                        </div>
                      </Card>
                    ))}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Input area */}
        <div className="border-t border-gray-200 p-4 bg-white">
          <form
            onSubmit={handleSubmit}
            className="max-w-3xl mx-auto flex relative"
          >
            <div className="relative flex-1">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Type your message..."
                className="w-full p-3 pr-12 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
              />
              <button
                type="button"
                onClick={toggleRecording}
                className={`absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-black ${
                  isRecording ? "text-red-500" : ""
                }`}
                aria-label="Voice input"
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
                >
                  <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path>
                  <path d="M19 10v2a7 7 0 0 1-14 0v-2"></path>
                  <line x1="12" y1="19" x2="12" y2="23"></line>
                  <line x1="8" y1="23" x2="16" y2="23"></line>
                </svg>
              </button>
            </div>
            <button
              type="submit"
              className="ml-2 bg-black text-white px-4 py-2 rounded-lg"
            >
              Send
            </button>
          </form>
        </div>
      </div>

      {/* Slider Panel with Toggle Button */}
      <div className="fixed top-0 right-0 h-full">
        {/* Toggle Button - Always visible */}
        <button
          onClick={toggleSlider}
          className="absolute top-1/2 right-0 transform -translate-y-1/2 translate-x-0 w-10 h-10 flex items-center justify-center bg-gray-200 rounded-l-md shadow-md border border-gray-300 text-black z-10"
          style={{
            right: sliderVisible ? "256px" : "0px",
            transition: "right 0.3s ease",
          }}
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

        {/* Slider Panel */}
        <div
          className={`pt-20 transition-all duration-300 bg-white border-l border-gray-200 h-full overflow-hidden ${
            sliderVisible ? "w-64" : "w-0"
          }`}
        >
          {sliderVisible && (
            <div className="p-4 overflow-y-auto h-full">
              <h3 className="text-lg font-medium mb-4 text-black">
                Stock Watchlist
              </h3>

              {/* CSV Import Section */}
              {!selectedFile && (
                <div className="mb-6 p-4 border border-gray-200 rounded-lg">
                  <h4 className="text-md font-medium mb-2 text-black">
                    Import Portfolio Data
                  </h4>
                  <p className="text-sm text-black mb-3">
                    Upload a CSV file with your portfolio data
                  </p>
                  <input
                    type="file"
                    title="your text"
                    accept=".csv"
                    onChange={handleFileChange}
                    className="block w-full text-sm text-black
                        file:mr-4 file:py-2 file:px-4
                        file:rounded-full file:border-0
                        file:text-sm file:font-semibold
                        file:bg-black file:text-white
                        hover:file:bg-gray-700"
                    style={{ color: "rgba(0,0,0,0)" }}
                  />
                  <div
                    className="absolute inset-0 pointer-events-none"
                    style={{ width: "calc(100% - 110px)", marginLeft: "110px" }}
                  ></div>
                </div>
              )}

              {/* Stock List */}
              <div className="space-y-2">
                {stockData.map((stock, index) => (
                  <div
                    key={index}
                    className="border rounded-md overflow-hidden"
                  >
                    <button
                      onClick={() => toggleStockNews(stock.ticker)}
                      className="w-full p-3 bg-white flex justify-between items-center hover:bg-gray-50"
                    >
                      <span className="font-medium text-black">
                        {stock.ticker}
                      </span>
                      <span
                        className={`text-sm ${
                          stock.daily_percent_change >= 0
                            ? "text-green-600"
                            : "text-red-600"
                        } mr-2`}
                      >
                        {stock.daily_percent_change >= 0 ? "+" : ""}
                        {stock.daily_percent_change.toFixed(2)}%
                      </span>
                    </button>

                    {expandedStocks.includes(stock.ticker) && (
                      <div className="p-3 bg-gray-50 border-t text-sm">
                        {getStockNews(stock.ticker).map((news, i) => (
                          <div
                            key={i}
                            className="mb-2 pb-2 border-b border-gray-200 last:border-0 last:mb-0 last:pb-0"
                          >
                            <p className="font-medium text-black">
                              {news.title}
                            </p>
                            <p className="text-black text-xs mt-1">
                              {news.date}
                            </p>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>

              {/* Reupload Portfolio Data option - Only show if a file has been uploaded */}
              {selectedFile && (
                <div className="mt-8 p-4 border border-gray-200 rounded-lg">
                  <h4 className="text-md font-medium mb-2 text-black">
                    Reupload Portfolio Data
                  </h4>
                  <div className="relative">
                    <input
                      type="file"
                      title=" "
                      accept=".csv"
                      onChange={handleFileChange}
                      className="block w-full text-sm text-black
                        file:mr-4 file:py-2 file:px-4
                        file:rounded-full file:border-0
                        file:text-sm file:font-semibold
                        file:bg-black file:text-white
                        hover:file:bg-gray-700"
                      style={{ color: "rgba(0,0,0,0)" }}
                    />
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      </div>

      {/* Account Settings Modal */}
      <AccountSettingsModal
        isOpen={showAccountModal}
        onClose={() => setShowAccountModal(false)}
      />
    </div>
  );
}
