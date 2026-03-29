import tkinter as tk
from tkinter import scrolledtext, messagebox
import platform
import time
import random
import sys
import threading       # for non‑blocking API calls

# Windows Longhorn (Plex) reference palette — Aurora, glass sidebar, taskbar
LH = {
    "aurora_base": "#1a3f5c",
    "aurora_band1": "#1e5a72",
    "aurora_band2": "#2a4a78",
    "aurora_glow": "#3d6a8a",
    "aurora_mist": "#4a90a8",
    "sidebar": "#1b2f47",
    "sidebar_deep": "#152535",
    "sidebar_glass": "#0f2438",
    "sidebar_edge": "#4a6b8a",
    "taskbar": "#0a1628",
    "taskbar_shine": "#3d5a78",
    "taskbar_tray": "#0d1f35",
    "text_primary": "#e8f4fc",
    "text_dim": "#a8c4dc",
    "title_accent": "#5a9fd4",
}


class CatOSLonghorn:
    def __init__(self, root):
        self.root = root
        self.root.title("Cat os LONGHORN")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        self.desktop_bg = LH["aurora_base"]
        self.sidebar_bg = LH["sidebar"]
        self.taskbar_bg = LH["taskbar"]

        self.root.configure(bg=self.desktop_bg)
        self.host_os = platform.system()

        self.setup_layout()
        self.setup_sidebar()
        self.setup_desktop()
        self.setup_taskbar()

    def setup_layout(self):
        self.taskbar = tk.Frame(self.root, bg=LH["taskbar"], height=40)
        self.taskbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.taskbar.pack_propagate(False)

        shine = tk.Frame(self.taskbar, bg=LH["taskbar_shine"], height=1)
        shine.pack(side=tk.TOP, fill=tk.X)

        self.main_area = tk.Frame(self.root, bg=self.desktop_bg)
        self.main_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.sidebar = tk.Frame(self.main_area, bg=self.sidebar_bg, width=148, highlightthickness=1, highlightbackground=LH["sidebar_edge"])
        self.sidebar.pack(side=tk.RIGHT, fill=tk.Y)
        self.sidebar.pack_propagate(False)

        self.desktop = tk.Frame(self.main_area, bg=self.desktop_bg)
        self.desktop.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def _draw_longhorn_aurora(self, canvas: tk.Canvas, w: int, h: int) -> None:
        canvas.delete("aurora")
        c = LH
        canvas.create_rectangle(0, 0, w, h, fill=c["aurora_base"], outline="", tags="aurora")
        # Layered “wave” bands (Longhorn Aurora–style abstract curves)
        for i, (y0, y1, col) in enumerate(
            [
                (0, int(h * 0.35), c["aurora_band1"]),
                (int(h * 0.15), int(h * 0.55), c["aurora_band2"]),
                (int(h * 0.35), int(h * 0.85), c["aurora_glow"]),
                (int(h * 0.55), h, c["aurora_base"]),
            ]
        ):
            canvas.create_oval(-w // 3, y0 - 40, w + w // 3, y1 + 80, fill=col, outline="", stipple="gray50", tags="aurora")
        canvas.create_oval(int(w * 0.2), int(h * 0.1), int(w * 0.95), int(h * 0.55), fill=c["aurora_mist"], outline="", stipple="gray25", tags="aurora")
        canvas.create_oval(int(-w * 0.15), int(h * 0.35), int(w * 0.55), int(h * 0.95), fill=c["aurora_band2"], outline="", stipple="gray12", tags="aurora")
        canvas.lower("aurora")

    def _on_desktop_configure(self, event) -> None:
        if event.widget == self.desktop_canvas:
            self._draw_longhorn_aurora(self.desktop_canvas, event.width, event.height)

    def setup_sidebar(self):
        head = tk.Frame(self.sidebar, bg=LH["sidebar_deep"], height=36)
        head.pack(side=tk.TOP, fill=tk.X)
        head.pack_propagate(False)
        tk.Label(
            head,
            text="LONGHORN",
            bg=LH["sidebar_deep"],
            fg=LH["title_accent"],
            font=("Segoe UI", 11, "bold"),
        ).pack(pady=8)

        lbl_logo = tk.Label(
            self.sidebar,
            text="Windows Sidebar",
            bg=self.sidebar_bg,
            fg=LH["text_dim"],
            font=("Segoe UI", 8),
        )
        lbl_logo.pack(pady=(4, 2))

        self.clock_frame = tk.Frame(
            self.sidebar,
            bg=LH["sidebar_glass"],
            bd=1,
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground=LH["sidebar_edge"],
        )
        self.clock_frame.pack(padx=8, pady=8, fill=tk.X)

        self.time_lbl = tk.Label(
            self.clock_frame,
            text="",
            bg=LH["sidebar_glass"],
            fg=LH["text_primary"],
            font=("Segoe UI", 20, "bold"),
        )
        self.time_lbl.pack(pady=(10, 0))
        self.date_lbl = tk.Label(
            self.clock_frame,
            text="",
            bg=LH["sidebar_glass"],
            fg=LH["text_dim"],
            font=("Segoe UI", 8),
        )
        self.date_lbl.pack(pady=(0, 10))

        search_frame = tk.Frame(self.sidebar, bg=self.sidebar_bg)
        search_frame.pack(padx=8, pady=6, fill=tk.X)
        tk.Label(search_frame, text="Search", bg=self.sidebar_bg, fg=LH["text_dim"], font=("Segoe UI", 8)).pack(anchor="w")
        search_entry = tk.Entry(
            search_frame,
            width=15,
            bg=LH["sidebar_glass"],
            fg=LH["text_primary"],
            insertbackground=LH["text_primary"],
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground=LH["sidebar_edge"],
            font=("Segoe UI", 9),
        )
        search_entry.pack(fill=tk.X, pady=2)

        status_frame = tk.Frame(
            self.sidebar,
            bg=LH["sidebar_glass"],
            bd=0,
            highlightthickness=1,
            highlightbackground=LH["sidebar_edge"],
        )
        status_frame.pack(padx=8, pady=8, fill=tk.X)
        tk.Label(
            status_frame,
            text="CPU: 4%\nRAM: 512 MB",
            bg=LH["sidebar_glass"],
            fg=LH["text_dim"],
            font=("Segoe UI", 8),
            justify=tk.LEFT,
        ).pack(pady=10, anchor="w", padx=10)

        self.update_sidebar_clock()

    def update_sidebar_clock(self):
        current_time = time.strftime("%H:%M")
        current_date = time.strftime("%A, %b %d")
        self.time_lbl.config(text=current_time)
        self.date_lbl.config(text=current_date)
        self.root.after(1000, self.update_sidebar_clock)

    def setup_desktop(self):
        self.desktop_canvas = tk.Canvas(
            self.desktop,
            highlightthickness=0,
            borderwidth=0,
            bg=LH["aurora_base"],
        )
        self.desktop_canvas.pack(fill=tk.BOTH, expand=True)
        self.desktop_canvas.bind("<Configure>", self._on_desktop_configure)

        self.create_icon("💻\nC.A.T Terminal", 20, 20, self.open_cat_terminal)
        self.create_icon("⚙️\nReal Apps", 20, 90, self.open_real_apps)
        self.create_icon("📁\nMy System", 20, 160, self.show_system_info)

        self.create_icon("🍷\nWINE Emulator", 110, 20, lambda: self.launch_prebuilt("WINE Emulator", "Initializing x86 compatibility layer..."))
        self.create_icon("💬\nDiscord", 110, 90, lambda: self.launch_prebuilt("Discord", "Connecting to voice channels..."))
        self.create_icon("🦁\nBrave", 110, 160, lambda: self.launch_prebuilt("Brave Browser", "Blocking trackers..."))

        self.create_icon("🎧\nTeamSpeak", 200, 20, lambda: self.launch_prebuilt("TeamSpeak 3", "Connecting to server..."))
        self.create_icon("🌐\nEdge", 200, 90, lambda: self.launch_prebuilt("Microsoft Edge", "Loading Chromium engine..."))
        self.create_icon("🤖\nC.A.T Core", 200, 160, self.open_cat_core)

    def create_icon(self, text, x, y, command):
        """Longhorn desktop tiles — same graphic as before (black / blue flat)."""
        btn = tk.Button(
            self.desktop_canvas,
            text=text,
            bg="black",
            fg="blue",
            font=("Tahoma", 8),
            relief=tk.FLAT,
            command=command,
            activebackground="black",
            activeforeground="blue",
            justify=tk.CENTER,
            width=12,
            bd=0,
            cursor="hand2",
        )
        self.desktop_canvas.create_window(x, y, window=btn, anchor=tk.NW)

    def setup_taskbar(self):
        self.start_btn = tk.Button(
            self.taskbar,
            text="❖ Start",
            bg="black",
            fg="blue",
            font=("Tahoma", 11, "bold", "italic"),
            relief=tk.FLAT,
            padx=15,
            command=self.toggle_start_menu,
            activebackground="black",
            activeforeground="blue",
            cursor="hand2",
        )
        self.start_btn.pack(side=tk.LEFT, fill=tk.Y)

        self.tray = tk.Frame(self.taskbar, bg=LH["taskbar_tray"], width=88, highlightthickness=0)
        self.tray.pack(side=tk.RIGHT, fill=tk.Y)
        self.tray.pack_propagate(False)

        tray_icons = tk.Label(
            self.tray,
            text="🔊  🔋  🌐",
            bg=LH["taskbar_tray"],
            fg=LH["text_dim"],
            font=("Segoe UI Symbol", 9),
        )
        tray_icons.pack(expand=True)

    def toggle_start_menu(self):
        messagebox.showinfo("Start", "Cat os LONGHORN Start Menu triggered.\nVersion: Python 3.14 Environment.")

    def show_system_info(self):
        info = f"Cat os LONGHORN Virtual Environment\n\nHost System: {self.host_os}\nArchitecture: x86_64\nPython Core Engine Active\nTheme: Plex / Aurora"
        messagebox.showinfo("System Properties", info)

    def open_real_apps(self):
        messagebox.showinfo("Real Apps", "[C.A.T] Mapping Host File System...\n\nBridging simulated environment with real applications folder.")

    def launch_prebuilt(self, app_name, message):
        messagebox.showinfo(app_name, f"Executing {app_name}...\n\n{message}\n\n(Environment Virtualized inside Cat os LONGHORN)")

    def _longhorn_window_chrome(self, win: tk.Toplevel, title: str, body_bg: str) -> tk.Frame:
        """Plex-style title strip + client area (Longhorn window look)."""
        win.configure(bg=LH["sidebar_deep"])
        titlebar = tk.Frame(win, bg=LH["sidebar_deep"], height=32)
        titlebar.pack(side=tk.TOP, fill=tk.X)
        titlebar.pack_propagate(False)
        tk.Label(
            titlebar,
            text=title,
            bg=LH["sidebar_deep"],
            fg=LH["text_primary"],
            font=("Segoe UI", 9),
        ).pack(side=tk.LEFT, padx=10, pady=6)
        client = tk.Frame(win, bg=body_bg)
        client.pack(fill=tk.BOTH, expand=True)
        return client

    def open_cat_core(self):
        bb_win = tk.Toplevel(self.root)
        bb_win.title("C.A.T - Central Advanced Tech Core")
        bb_win.geometry("500x400")
        body_bg = "#0F172A"
        client = self._longhorn_window_chrome(bb_win, "C.A.T — Central Advanced Tech Core", body_bg)

        tk.Label(
            client,
            text="🤖 C.A.T Central Advanced Tech Core",
            bg=body_bg,
            fg=LH["title_accent"],
            font=("Segoe UI", 11, "bold"),
        ).pack(pady=10)

        input_frame = tk.Frame(client, bg=body_bg)
        input_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(input_frame, text="Task Prompt:", bg=body_bg, fg=LH["text_dim"], font=("Segoe UI", 9)).pack(side=tk.LEFT)
        prompt_entry = tk.Entry(
            input_frame,
            bg="#1E293B",
            fg="white",
            font=("Consolas", 9),
            insertbackground="white",
            width=40,
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground=LH["sidebar_edge"],
        )
        prompt_entry.insert(0, "Download invoices from email and save as CSV")
        prompt_entry.pack(side=tk.LEFT, padx=5)

        log = scrolledtext.ScrolledText(
            client,
            bg="#1E293B",
            fg="#A7F3D0",
            font=("Consolas", 9),
            height=12,
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground=LH["sidebar_edge"],
        )
        log.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        btn_frame = tk.Frame(client, bg=body_bg)
        btn_frame.pack(fill=tk.X, pady=10)

        # ---------- LM Studio integration ----------
        LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"

        def call_lm_studio(task, log_widget, error_callback):
            """Send prompt to LM Studio and stream response into log."""
            try:
                import requests
            except ImportError:
                error_callback("Requests library not installed. Install it with 'pip install requests' to use LM Studio.")
                return

            # Prepare the message for the LLM
            system_prompt = (
                "You are C.A.T (Central Advanced Tech Core), an autonomous desktop agent. "
                "Given a user task, provide a step‑by‑step plan as if you were executing it on a Windows desktop. "
                "Be concise but detailed. Use bullet points or numbered steps."
            )
            payload = {
                "model": "local-model",  # LM Studio ignores this, but required
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": task}
                ],
                "temperature": 0.7,
                "max_tokens": 500,
                "stream": False
            }
            try:
                response = requests.post(LM_STUDIO_URL, json=payload, timeout=30)
                if response.status_code == 200:
                    data = response.json()
                    answer = data["choices"][0]["message"]["content"]
                    # Display the answer in the log, line by line
                    log_widget.insert(tk.END, "[LM STUDIO] Response received:\n\n")
                    for line in answer.splitlines():
                        log_widget.insert(tk.END, line + "\n")
                    log_widget.see(tk.END)
                else:
                    error_callback(f"LM Studio error: HTTP {response.status_code}\n{response.text}")
            except requests.exceptions.ConnectionError:
                error_callback("Cannot connect to LM Studio. Make sure it's running on port 1234.")
            except Exception as e:
                error_callback(f"Unexpected error: {str(e)}")

        def run_task_with_lmstudio():
            task = prompt_entry.get()
            log.delete("1.0", tk.END)
            log.insert(tk.END, "[SYSTEM] Contacting LM Studio on localhost:1234...\n")
            log.insert(tk.END, f"[AGENT] Task: '{task}'\n\n")
            log.see(tk.END)

            def on_error(err_msg):
                log.insert(tk.END, f"\n[ERROR] {err_msg}\n")
                log.insert(tk.END, "\nFalling back to simulated sequence...\n")
                log.see(tk.END)
                run_simulated_sequence(task, log)

            # Start LM Studio call in a separate thread
            threading.Thread(target=call_lm_studio, args=(task, log, on_error), daemon=True).start()

        def run_simulated_sequence(task, log_widget):
            """Original simulated sequence (fallback)."""
            sequence = [
                "[SYSTEM] Initializing Cat os LONGHORN Docker Container...",
                f"[AGENT] Received Task: '{task}'",
                "[AGENT] Planning steps using LLM...",
                "[DESKTOP] Launching virtual Firefox browser...",
                "[ACTION] Navigating to target portal...",
                "[VISION] Analyzing DOM and visual elements...",
                "[ACTION] Simulating mouse move to (450, 320)...",
                "[ACTION] Executing left click on 'Download'...",
                "[SYSTEM] Intercepting file download to virtual filesystem...",
                "[AGENT] Parsing data into structured format...",
                "[SUCCESS] Task completed autonomously in isolated environment.",
            ]

            def insert_step(index):
                if index < len(sequence):
                    log_widget.insert(tk.END, sequence[index] + "\n")
                    log_widget.see(tk.END)
                    bb_win.after(random.randint(600, 1500), insert_step, index + 1)

            insert_step(0)

        # Buttons
        tk.Button(
            btn_frame,
            text="▶ Execute Agent (LM Studio)",
            bg="black",
            fg="blue",
            font=("Tahoma", 8, "bold"),
            activebackground="black",
            activeforeground="blue",
            relief=tk.FLAT,
            command=run_task_with_lmstudio,
        ).pack(side=tk.LEFT, padx=10)

        def view_container():
            log.insert(tk.END, "\n[DOCKER] Inspecting C.A.T Ubuntu container...\n")
            log.insert(tk.END, "[STATE] Running. RAM: 1.2GB. Virtual XFCE Desktop Active.\n")
            log.see(tk.END)

        tk.Button(
            btn_frame,
            text="🐳 View Container",
            bg="black",
            fg="blue",
            font=("Tahoma", 8, "bold"),
            activebackground="black",
            activeforeground="blue",
            relief=tk.FLAT,
            command=view_container,
        ).pack(side=tk.RIGHT, padx=10)

    def open_cat_terminal(self):
        cat_win = tk.Toplevel(self.root)
        cat_win.title("C.A.T Terminal")
        cat_win.geometry("550x350")

        top_bar_bg = LH["sidebar_deep"]
        tab_bg = "#0C0C0C"
        cat_win.configure(bg=top_bar_bg)

        title_row = tk.Frame(cat_win, bg=top_bar_bg, height=36)
        title_row.pack(side=tk.TOP, fill=tk.X)
        title_row.pack_propagate(False)
        tk.Label(
            title_row,
            text="C.A.T Terminal",
            bg=top_bar_bg,
            fg=LH["text_primary"],
            font=("Segoe UI", 9),
        ).pack(side=tk.LEFT, padx=10, pady=8)

        tab_frame = tk.Frame(cat_win, bg=top_bar_bg, height=35)
        tab_frame.pack(side=tk.TOP, fill=tk.X)
        tab_frame.pack_propagate(False)

        active_tab = tk.Frame(tab_frame, bg=tab_bg, width=160, height=28)
        active_tab.pack(side=tk.LEFT, padx=(10, 0), pady=(4, 0))
        active_tab.pack_propagate(False)

        tk.Label(active_tab, text=">_ C.A.T Subsystem", bg=tab_bg, fg=LH["text_primary"], font=("Segoe UI", 9)).pack(side=tk.LEFT, padx=10)

        btn_add = tk.Button(
            tab_frame,
            text="＋",
            bg="black",
            fg="blue",
            font=("Segoe UI", 10),
            bd=0,
            activebackground="black",
            activeforeground="blue",
            cursor="hand2",
        )
        btn_add.pack(side=tk.LEFT, padx=5, pady=(4, 0))

        txt = scrolledtext.ScrolledText(
            cat_win,
            bg=tab_bg,
            fg="#CCCCCC",
            font=("Consolas", 10),
            insertbackground="white",
            bd=0,
            highlightthickness=0,
        )
        txt.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)

        startup_seq = [
            "Windows Terminal (C.A.T Edition)",
            "Version: Windows 11 25H2 Architecture",
            "--------------------------------------------------",
            "Mounting Python ASM Virtualizer... [OK]",
            "Type 'help' for commands, or 'pr asm x86_x64' to query bits.\n> ",
        ]
        for line in startup_seq:
            txt.insert(tk.END, line + "\n")

        def handle_cmd(event):
            content = txt.get("1.0", tk.END).split("\n")
            if len(content) >= 2:
                cmd = content[-2].replace("> ", "").strip()
            else:
                cmd = ""

            txt.insert(tk.END, "\n")

            if cmd == "help":
                txt.insert(tk.END, "C.A.T Terminal Commands:\n")
                txt.insert(tk.END, " - run <os> <app> : Simulates running cross-platform apps\n")
                txt.insert(tk.END, " - pr asm x86_x64 : Queries raw ASM bits and registers\n")
                txt.insert(tk.END, " - clear          : Clears terminal\n")
            elif cmd == "clear":
                txt.delete("1.0", tk.END)
            elif cmd.startswith("run"):
                parts = cmd.split(" ")
                if len(parts) >= 3:
                    target_os = parts[1].lower()
                    app = " ".join(parts[2:])
                    txt.insert(tk.END, f"[C.A.T] Allocating hypervisor memory for {target_os.upper()}...\n", "sys")
                    txt.insert(tk.END, f"[C.A.T] Bridging native calls to execute '{app}'...\n", "sys")
                    txt.insert(tk.END, "[SUCCESS] Virtual process isolated and running in background.\n", "success")
                else:
                    txt.insert(tk.END, "Syntax: run <windows|mac|linux> <app_name>\n", "err")

            elif cmd == "pr asm x86_x64":
                self.simulate_asm_query(txt)

            elif cmd != "":
                txt.insert(tk.END, f"Unknown C.A.T directive: {cmd}\n", "err")

            txt.insert(tk.END, "> ")
            txt.see(tk.END)
            return "break"

        txt.tag_config("sys", foreground=LH["title_accent"])
        txt.tag_config("success", foreground="#10B981")
        txt.tag_config("err", foreground="#EF4444")

        txt.bind("<Return>", handle_cmd)
        txt.focus_set()

    def simulate_asm_query(self, txt_widget):
        txt_widget.insert(tk.END, "[SYSTEM] Querying x86_64 architecture bits...\n", "sys")
        txt_widget.insert(tk.END, "[SYSTEM] Accessing CPU Ring 0 (Simulated)...\n\n", "sys")

        registers = ["RAX", "RBX", "RCX", "RDX", "RSI", "RDI", "RSP", "RBP"]
        for i in range(0, len(registers), 2):
            r1, r2 = registers[i], registers[i + 1]
            val1 = f"0x{random.randint(0, 0xFFFFFFFFFFFFFFFF):016X}"
            val2 = f"0x{random.randint(0, 0xFFFFFFFFFFFFFFFF):016X}"
            txt_widget.insert(tk.END, f" {r1}: {val1}    {r2}: {val2}\n")

        txt_widget.insert(tk.END, "\n[ASM] Dumping executed machine code instruction bits:\n")
        for _ in range(3):
            bits = " ".join([f"{random.randint(0, 255):08b}" for _ in range(4)])
            txt_widget.insert(tk.END, f" > {bits}  (x86 ops translated)\n")

        txt_widget.insert(tk.END, "\n[C.A.T] ASM Query Complete. Subsystem stable.\n", "success")


# ========== STARTUP BEEP FUNCTION (MS‑DOS style triple beep) ==========
def play_startup_beeps(window):
    """Play three beeps (beep‑beep‑beep) without blocking the GUI."""
    def beep(count):
        if count >= 3:
            return
        try:
            # Windows: use winsound.Beep (frequency 800 Hz, duration 200 ms)
            if platform.system() == "Windows":
                import winsound
                winsound.Beep(800, 200)
            else:
                # Unix/Linux/macOS: use terminal bell (print('\a'))
                sys.stdout.write('\a')
                sys.stdout.flush()
        except Exception:
            # Fallback: silent fail
            pass
        # Schedule next beep after 300 ms
        window.after(300, lambda: beep(count + 1))
    beep(0)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    boot_win = tk.Toplevel(root)
    boot_win.title("System Boot")
    boot_win.geometry("700x450")
    boot_win.configure(bg=LH["aurora_base"])
    boot_win.resizable(False, False)

    bios_text = tk.Text(
        boot_win,
        bg=LH["sidebar_deep"],
        fg=LH["text_dim"],
        font=("Consolas", 10, "bold"),
        bd=0,
        highlightthickness=0,
    )
    bios_text.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

    boot_messages = [
        "AC BIOS (C) AC CORP.",
        "Main Processor: Virtualized CPU @ 3.00GHz",
        "Memory Testing: 4194304K OK",
        "",
        "Detecting Primary Master   ... AC CORP VIRTUAL DRIVE",
        "Detecting Primary Slave    ... None",
        "Detecting Secondary Master ... CD-ROM DRIVE",
        "Detecting Secondary Slave  ... None",
        "",
        "Initializing USB Controllers... Done.",
        "Booting from Hard Disk...",
        "Loading AC OS Kernel...",
        "OK",
    ]

    def show_splash():
        bios_text.destroy()
        splash_frame = tk.Frame(boot_win, bg=LH["aurora_base"])
        splash_frame.pack(fill=tk.BOTH, expand=True)
        lbl_welcome = tk.Label(
            splash_frame,
            text="WELCOME TO AC OS",
            bg=LH["aurora_base"],
            fg=LH["text_primary"],
            font=("Segoe UI", 28, "bold"),
        )
        lbl_welcome.pack(expand=True, pady=(100, 10))
        lbl_corp = tk.Label(
            splash_frame,
            text="[C] AC CORP · Longhorn Plex",
            bg=LH["aurora_base"],
            fg=LH["text_dim"],
            font=("Segoe UI", 14),
        )
        lbl_corp.pack(expand=True, pady=(0, 100))

        boot_win.after(2500, launch_os)

    def show_msg(idx):
        if idx < len(boot_messages):
            bios_text.insert(tk.END, boot_messages[idx] + "\n")
            bios_text.see(tk.END)
            delay = random.randint(150, 400)
            boot_win.after(delay, show_msg, idx + 1)
        else:
            boot_win.after(600, show_splash)

    # Play the triple beep just before the boot messages start
    play_startup_beeps(boot_win)
    show_msg(0)

    def launch_os():
        boot_win.destroy()
        root.deiconify()
        CatOSLonghorn(root)

    root.mainloop()
