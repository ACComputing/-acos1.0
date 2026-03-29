import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import platform
import time
import random

class CatOSLonghorn:
    def __init__(self, root):
        self.root = root
        self.root.title("Cat os LONGHORN")
        self.root.geometry("700x450")
        self.root.resizable(False, False)
        
        # Windows Longhorn "Plex" Theme Colors
        self.desktop_bg = "#274B72"    # Deep Slate Blue for Desktop
        self.sidebar_bg = "#193352"    # Darker Sidebar
        self.taskbar_bg = "#0D1B2A"    # Glossy dark taskbar
        self.start_btn_bg = "#386FA4"  # Start button blue
        self.text_color = "#FFFFFF"    # White text for modern look
        
        self.root.configure(bg=self.desktop_bg)
        self.host_os = platform.system()
        
        self.setup_layout()
        self.setup_sidebar()
        self.setup_desktop()
        self.setup_taskbar()

    def setup_layout(self):
        """Creates the main layout areas (Taskbar, Sidebar, Desktop)"""
        # Taskbar at the bottom
        self.taskbar = tk.Frame(self.root, bg=self.taskbar_bg, height=40)
        self.taskbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.taskbar.pack_propagate(False)
        
        # Main area above taskbar
        self.main_area = tk.Frame(self.root, bg=self.desktop_bg)
        self.main_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Sidebar on the right
        self.sidebar = tk.Frame(self.main_area, bg=self.sidebar_bg, width=140)
        self.sidebar.pack(side=tk.RIGHT, fill=tk.Y)
        self.sidebar.pack_propagate(False)
        
        # Desktop on the left
        self.desktop = tk.Frame(self.main_area, bg=self.desktop_bg)
        self.desktop.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def setup_sidebar(self):
        """Creates the iconic Windows Longhorn Sidebar."""
        # Sidebar Title / Logo
        lbl_logo = tk.Label(self.sidebar, text="LONGHORN", bg=self.sidebar_bg, fg="blue", font=("Arial", 10, "bold"))
        lbl_logo.pack(pady=(15, 5))
        
        # Analog Clock placeholder (Digital for simplicity)
        self.clock_frame = tk.Frame(self.sidebar, bg="#11243A", bd=1, relief=tk.SUNKEN)
        self.clock_frame.pack(padx=10, pady=10, fill=tk.X)
        
        self.time_lbl = tk.Label(self.clock_frame, text="", bg="#11243A", fg="blue", font=("Tahoma", 18, "bold"))
        self.time_lbl.pack(pady=(10, 0))
        self.date_lbl = tk.Label(self.clock_frame, text="", bg="#11243A", fg="blue", font=("Tahoma", 8))
        self.date_lbl.pack(pady=(0, 10))
        
        # Quick Search Box Widget
        search_frame = tk.Frame(self.sidebar, bg=self.sidebar_bg)
        search_frame.pack(padx=10, pady=10, fill=tk.X)
        tk.Label(search_frame, text="Search", bg=self.sidebar_bg, fg="blue", font=("Tahoma", 8)).pack(anchor="w")
        search_entry = tk.Entry(search_frame, width=15, bg="#2A4B72", fg="white", relief=tk.FLAT)
        search_entry.pack(fill=tk.X, pady=2)
        
        # System status widget
        status_frame = tk.Frame(self.sidebar, bg="#11243A", bd=1, relief=tk.SUNKEN)
        status_frame.pack(padx=10, pady=10, fill=tk.X)
        tk.Label(status_frame, text="CPU: 4% \nRAM: 512 MB", bg="#11243A", fg="blue", font=("Tahoma", 8), justify=tk.LEFT).pack(pady=10, anchor="w", padx=10)

        self.update_sidebar_clock()

    def update_sidebar_clock(self):
        """Updates the Longhorn sidebar clock and date."""
        current_time = time.strftime("%H:%M")
        current_date = time.strftime("%A, %b %d")
        self.time_lbl.config(text=current_time)
        self.date_lbl.config(text=current_date)
        self.root.after(1000, self.update_sidebar_clock)

    def setup_desktop(self):
        """Creates the desktop area and icons."""
        # Desktop Icons - Column 1 (System Tools)
        self.create_icon("💻\nC.A.T Terminal", 20, 20, self.open_cat_terminal)
        self.create_icon("⚙️\nReal Apps", 20, 90, self.open_real_apps)
        self.create_icon("📁\nMy System", 20, 160, self.show_system_info)

        # Desktop Icons - Column 2 (Prebuilt Apps)
        self.create_icon("🍷\nWINE Emulator", 110, 20, lambda: self.launch_prebuilt("WINE Emulator", "Initializing x86 compatibility layer..."))
        self.create_icon("💬\nDiscord", 110, 90, lambda: self.launch_prebuilt("Discord", "Connecting to voice channels..."))
        self.create_icon("🦁\nBrave", 110, 160, lambda: self.launch_prebuilt("Brave Browser", "Blocking trackers..."))

        # Desktop Icons - Column 3 (Prebuilt Apps & AI)
        self.create_icon("🎧\nTeamSpeak", 200, 20, lambda: self.launch_prebuilt("TeamSpeak 3", "Connecting to server..."))
        self.create_icon("🌐\nEdge", 200, 90, lambda: self.launch_prebuilt("Microsoft Edge", "Loading Chromium engine..."))
        self.create_icon("🤖\nC.A.T Core", 200, 160, self.open_cat_core)

    def create_icon(self, text, x, y, command):
        """Helper to create sleek, flat desktop icons blending into the background."""
        btn = tk.Button(self.desktop, text=text, bg="black", fg="blue", 
                        font=("Tahoma", 8), relief=tk.FLAT, command=command,
                        activebackground="black", activeforeground="blue",
                        justify=tk.CENTER, width=12, bd=0, cursor="hand2")
        btn.place(x=x, y=y)

    def setup_taskbar(self):
        """Creates the Longhorn style taskbar at the bottom."""
        # Start Button (Plex Style)
        self.start_btn = tk.Button(self.taskbar, text="❖ Start", bg="black", 
                                   fg="blue", font=("Tahoma", 11, "bold", "italic"), 
                                   relief=tk.FLAT, padx=15, command=self.toggle_start_menu,
                                   activebackground="black", activeforeground="blue", cursor="hand2")
        self.start_btn.pack(side=tk.LEFT, fill=tk.Y)
        
        # System Tray Area (Simplified since clock is in sidebar)
        self.tray = tk.Frame(self.taskbar, bg="#11243A", width=80)
        self.tray.pack(side=tk.RIGHT, fill=tk.Y)
        self.tray.pack_propagate(False)
        
        tray_icons = tk.Label(self.tray, text="🔊 🔋 🌐", bg="#11243A", fg="blue", font=("Segoe UI Symbol", 9))
        tray_icons.pack(expand=True)

    def toggle_start_menu(self):
        messagebox.showinfo("Start", "Cat os LONGHORN Start Menu triggered.\nVersion: Python 3.14 Environment.")

    def show_system_info(self):
        """Shows fake system info."""
        info = f"Cat os LONGHORN Virtual Environment\n\nHost System: {self.host_os}\nArchitecture: x86_64\nPython Core Engine Active\nTheme: Plex Glass"
        messagebox.showinfo("System Properties", info)

    def open_real_apps(self):
        """Simulates opening a real apps folder."""
        messagebox.showinfo("Real Apps", "[C.A.T] Mapping Host File System...\n\nBridging simulated environment with real applications folder.")
        
    def launch_prebuilt(self, app_name, message):
        """Simulates launching a prebuilt app."""
        messagebox.showinfo(app_name, f"Executing {app_name}...\n\n{message}\n\n(Environment Virtualized inside Cat os LONGHORN)")

    def open_cat_core(self):
        """Opens the C.A.T AI Desktop Agent environment."""
        bb_win = tk.Toplevel(self.root)
        bb_win.title("C.A.T - Central Advanced Tech Core")
        bb_win.geometry("500x400")
        bb_win.configure(bg="#0F172A") 
        
        tk.Label(bb_win, text="🤖 C.A.T Central Advanced Tech Core", bg="#0F172A", fg="blue", font=("Tahoma", 11, "bold")).pack(pady=10)
        
        input_frame = tk.Frame(bb_win, bg="#0F172A")
        input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(input_frame, text="Task Prompt:", bg="#0F172A", fg="blue", font=("Tahoma", 9)).pack(side=tk.LEFT)
        prompt_entry = tk.Entry(input_frame, bg="#1E293B", fg="white", font=("Consolas", 9), insertbackground="white", width=40)
        prompt_entry.insert(0, "Download invoices from email and save as CSV")
        prompt_entry.pack(side=tk.LEFT, padx=5)
        
        log = scrolledtext.ScrolledText(bb_win, bg="#1E293B", fg="#A7F3D0", font=("Consolas", 9), height=12)
        log.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        btn_frame = tk.Frame(bb_win, bg="#0F172A")
        btn_frame.pack(fill=tk.X, pady=10)
        
        def run_task():
            task = prompt_entry.get()
            log.delete("1.0", tk.END)
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
                "[SUCCESS] Task completed autonomously in isolated environment."
            ]
            
            def insert_step(index):
                if index < len(sequence):
                    log.insert(tk.END, sequence[index] + "\n")
                    log.see(tk.END)
                    bb_win.after(random.randint(600, 1500), insert_step, index + 1)

            insert_step(0)

        def view_container():
            log.insert(tk.END, "\n[DOCKER] Inspecting C.A.T Ubuntu container...\n")
            log.insert(tk.END, "[STATE] Running. RAM: 1.2GB. Virtual XFCE Desktop Active.\n")
            log.see(tk.END)

        tk.Button(btn_frame, text="▶ Execute Agent", bg="black", fg="blue", font=("Tahoma", 8, "bold"), 
                  activebackground="black", activeforeground="blue", relief=tk.FLAT, command=run_task).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="🐳 View Container", bg="black", fg="blue", font=("Tahoma", 8, "bold"), 
                  activebackground="black", activeforeground="blue", relief=tk.FLAT, command=view_container).pack(side=tk.RIGHT, padx=10)

    def open_cat_terminal(self):
        """Opens the modern C.A.T Terminal (Windows 11 25H2 Edition)."""
        cat_win = tk.Toplevel(self.root)
        cat_win.title("C.A.T Terminal")
        cat_win.geometry("550x350")
        
        # Win 11 Terminal Top Bar styling
        top_bar_bg = "#202020" # Dark gray window frame
        tab_bg = "#0C0C0C"     # Active tab background
        cat_win.configure(bg=top_bar_bg)
        
        # Faux Tab Bar Header
        tab_frame = tk.Frame(cat_win, bg=top_bar_bg, height=35)
        tab_frame.pack(side=tk.TOP, fill=tk.X)
        tab_frame.pack_propagate(False)
        
        # The Active Tab
        active_tab = tk.Frame(tab_frame, bg=tab_bg, width=160, height=30)
        active_tab.pack(side=tk.LEFT, padx=(8, 0), pady=(5, 0))
        active_tab.pack_propagate(False)
        
        tk.Label(active_tab, text=">_ C.A.T Subsystem", bg=tab_bg, fg="#FFFFFF", font=("Segoe UI", 9)).pack(side=tk.LEFT, padx=10)
        
        # "New Tab" + button
        btn_add = tk.Button(tab_frame, text="＋", bg=top_bar_bg, fg="white", font=("Segoe UI", 10), 
                            bd=0, activebackground="#333333", activeforeground="white", cursor="hand2")
        btn_add.pack(side=tk.LEFT, padx=5, pady=(5, 0))

        # Main Terminal Area
        txt = scrolledtext.ScrolledText(cat_win, bg=tab_bg, fg="#CCCCCC", font=("Consolas", 10), insertbackground="white", bd=0, highlightthickness=0)
        txt.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        startup_seq = [
            "Windows Terminal (C.A.T Edition)",
            "Version: Windows 11 25H2 Architecture",
            "--------------------------------------------------",
            "Mounting Python ASM Virtualizer... [OK]",
            "Type 'help' for commands, or 'pr asm x86_x64' to query bits.\n> "
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
                    txt.insert(tk.END, f"[SUCCESS] Virtual process isolated and running in background.\n", "success")
                else:
                    txt.insert(tk.END, "Syntax: run <windows|mac|linux> <app_name>\n", "err")
            
            elif cmd == "pr asm x86_x64":
                self.simulate_asm_query(txt)
            
            elif cmd != "":
                txt.insert(tk.END, f"Unknown C.A.T directive: {cmd}\n", "err")
            
            txt.insert(tk.END, "> ")
            txt.see(tk.END)
            return "break" 

        # Add text tags for coloring terminal outputs
        txt.tag_config("sys", foreground="#3B82F6")     # Blue
        txt.tag_config("success", foreground="#10B981") # Green
        txt.tag_config("err", foreground="#EF4444")     # Red

        txt.bind("<Return>", handle_cmd)
        txt.focus_set()

    def simulate_asm_query(self, txt_widget):
        """Simulates querying x86_64 CPU bits and memory addresses."""
        txt_widget.insert(tk.END, "[SYSTEM] Querying x86_64 architecture bits...\n", "sys")
        txt_widget.insert(tk.END, "[SYSTEM] Accessing CPU Ring 0 (Simulated)...\n\n", "sys")
        
        registers = ['RAX', 'RBX', 'RCX', 'RDX', 'RSI', 'RDI', 'RSP', 'RBP']
        for i in range(0, len(registers), 2):
            r1, r2 = registers[i], registers[i+1]
            val1 = f"0x{random.randint(0, 0xFFFFFFFFFFFFFFFF):016X}"
            val2 = f"0x{random.randint(0, 0xFFFFFFFFFFFFFFFF):016X}"
            txt_widget.insert(tk.END, f" {r1}: {val1}    {r2}: {val2}\n")
        
        txt_widget.insert(tk.END, "\n[ASM] Dumping executed machine code instruction bits:\n")
        for _ in range(3):
            bits = " ".join([f"{random.randint(0, 255):08b}" for _ in range(4)])
            txt_widget.insert(tk.END, f" > {bits}  (x86 ops translated)\n")
            
        txt_widget.insert(tk.END, "\n[C.A.T] ASM Query Complete. Subsystem stable.\n", "success")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() # Hide the main window during bootup
    
    boot_win = tk.Toplevel(root)
    boot_win.title("System Boot")
    boot_win.geometry("700x450")
    boot_win.configure(bg="black")
    boot_win.resizable(False, False)
    
    bios_text = tk.Text(boot_win, bg="black", fg="#A8A8A8", font=("Consolas", 10, "bold"), bd=0, highlightthickness=0)
    bios_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
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
        "OK"
    ]
    
    def show_splash():
        bios_text.destroy()
        splash_frame = tk.Frame(boot_win, bg="black")
        splash_frame.pack(fill=tk.BOTH, expand=True)
        
        lbl_welcome = tk.Label(splash_frame, text="WELCOME TO AC OS", bg="black", fg="blue", font=("Arial", 28, "bold"))
        lbl_welcome.pack(expand=True, pady=(100, 10))
        
        lbl_corp = tk.Label(splash_frame, text="[C] AC CORP", bg="black", fg="white", font=("Arial", 14))
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
            
    def launch_os():
        boot_win.destroy()
        root.deiconify()
        app = CatOSLonghorn(root)
        
    # Start the boot sequence
    show_msg(0)
    
    root.mainloop()
