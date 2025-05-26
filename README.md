# 📝 PaperBridge (Self-Hosted Edition)

Turn your handwritten journal pages into beautifully structured Obsidian notes with GPT-powered transcription and automation.

## 🚀 What is PaperBridge?

PaperBridge is a streamlined system for converting physical journal entries into searchable, tagged, and Markdown-formatted notes inside your Obsidian vault.

This self-hosted version gives you complete control over the code, your data, and GPT usage.

---

## ✨ Features

* 🧠 GPT-powered OCR & note structuring
* 🗂️ Saves notes directly into your Obsidian folder
* 📎 Saves scanned attachments
* 🏷️ Auto-tags content and extracts metadata
* 🖥️ Fully self-hosted (no data leaves your control)

---

## 🛠️ Requirements

* Python 3.10+
* Flask
* OpenAI account + API key
* Apple Shortcuts (on macOS or iOS)

---

## 📦 Installation

### 1. Clone This Repository

```bash
git clone https://github.com/your-username/paperbridge.git
cd paperbridge
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set Your OpenAI API Key

Create a `.env` file or set it as an environment variable:

```bash
export OPENAI_API_KEY=your-key-here
```

### 4. Run the Server

```bash
python main.py
```

Your server will run locally at: `http://localhost:5000`

---

## 📱 Apple Shortcuts Integration

You should have gotten access to an Apple Shortcut (`PaperBridge.shortcut`) from this link: [https://edvardoarcher.gumroad.com/l/udxmmc](https://edvardoarcher.gumroad.com/l/udxmmc)

* Prompts you to select a scan (JPEG or PDF)
* Sends it to your local PaperBridge server
* Saves the returned Markdown note and the attachment into your Obsidian vault

> 💡 You’ll set your Obsidian vault path directly in the shortcut.

---

## 📁 File Output

Each scan generates:

* `Type-notes-YYYY-MM-DD.md` (formatted note with metadata, tags, and attachment link)
* A saved image or PDF file in your configured attachment folder

---

## 🙋 FAQ

**Q: Can I use this without GPT?**
A: Not currently — GPT handles the transcription and structuring.

**Q: Can I customize the prompt?**
A: Yes! Edit the `main.py` prompt block.

**Q: Will this work on Windows?**
A: The server can run on Windows, but the Apple Shortcut requires macOS/iOS.

---

## 📄 License

MIT License — you’re free to modify, remix, and reuse.

---

Made by [Edvardo Archer](https://github.com/your-username) — therapist, workflow strategist, and builder of helpful tools.
