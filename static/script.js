// Lấy sẵn các node
const input   = document.getElementById("chatbot-input");
const sendBtn = document.getElementById("sent");              // giữ đúng id="sent"
const list    = document.getElementById("chatbot-messages");

let sending = false;   // chống double-click / double-enter
let composing = false; // đang gõ IME (JP/VN), tránh gửi sớm

function appendMsg(text, who = "user") {
  const div = document.createElement("div");
  div.className = "message " + who;
  div.textContent = text;
  list.appendChild(div);
  list.scrollTop = list.scrollHeight; // auto scroll xuống cuối
}

async function handleSend() {
  const message = input.value.trim();
  if (!message || sending) return;

  sending = true;
  sendBtn.disabled = true;

  // Hiển thị message của user
  appendMsg(message, "user");
  input.value = "";

  // (tuỳ chọn) hiển thị trạng thái bot đang trả lời
  const typing = document.createElement("div");
  typing.className = "message bot";
  typing.textContent = "…";
  list.appendChild(typing);
  list.scrollTop = list.scrollHeight;

  try {
    const res = await fetch("/chat-answer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });
    const data = await res.json();
    typing.remove(); // bỏ dấu "…"
    appendMsg(data.reply ?? "(Không có phản hồi)", "bot");
  } finally {
    sending = false;
    sendBtn.disabled = false;
    input.focus();
  }
}

// Click gửi
sendBtn.addEventListener("click", handleSend);

// Enter để gửi, Shift+Enter để xuống dòng (nếu input là <textarea>).
// Nếu input là <input type="text"> thì vẫn OK, chỉ Enter sẽ gửi.
input.addEventListener("keydown", (e) => {
  if (composing) return;                               // đang gõ IME
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();                                // không chèn newline
    handleSend();
  }
});

// Bắt IME composition (tránh gửi khi đang chọn chữ)
input.addEventListener("compositionstart", () => (composing = true));
input.addEventListener("compositionend",   () => (composing = false));

// Nếu input nằm trong <form>, chặn submit toàn trang
input.form?.addEventListener("submit", (e) => e.preventDefault());
