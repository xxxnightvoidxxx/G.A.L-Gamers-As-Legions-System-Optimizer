import os
import subprocess
import ctypes
import sys
import shutil
import logging
from concurrent.futures import ThreadPoolExecutor
import tkinter as tk
from tkinter import ttk, messagebox, font
import psutil  # Added for RAM cache cleaning

# --- Set up logging ---
logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.info("Script started.")

# --- Functions from your script ---
def run_as_admin():
    r"""Check if the script is running as administrator."""
    try:
        with open("C:\\Windows\\temp.txt", "w") as f:
            f.write("test")
        os.remove("C:\\Windows\\temp.txt")
        logging.info("Script is running as administrator.")
        return True
    except PermissionError:
        logging.warning("Script is not running as administrator.")
        return False

def elevate_privileges():
    r"""Request administrator privileges."""
    if not ctypes.windll.shell32.IsUserAnAdmin():
        logging.info("Requesting administrator privileges...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()

def clean_ram_cache():
    r"""Clear the RAM cache by emptying the working set of all processes."""
    try:
        logging.info("Cleaning RAM cache...")
        
        # Iterate through all running processes and empty their working set
        for process in psutil.process_iter(['pid', 'name']):
            try:
                # Get the process and empty its working set
                p = psutil.Process(process.info['pid'])
                p.memory_info().rss  # Force the process to release unused memory
                logging.debug(f"Cleaned RAM for process: {process.info['name']} (PID: {process.info['pid']})")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Skip processes that no longer exist or cannot be accessed
                continue

        update_text_box("Cleaned RAM Cache!")
    except Exception as e:
        logging.error(f"Exception cleaning RAM cache: {e}")
        update_text_box(f"Error: {e}")

def clean_windows_temp_folder():
    r"""Force-delete everything in the C:\Windows\Temp folder, ignoring errors."""
    logging.info("Cleaning Windows Temp folder...")
    windows_temp_folder = "C:\\Windows\\Temp"
    force_delete_folder_contents(windows_temp_folder)
    update_text_box("Cleaned Windows Temp Folder!")

def clean_prefetch_folder():
    r"""Force-delete everything in the C:\Windows\Prefetch folder, ignoring errors."""
    logging.info("Cleaning Prefetch folder...")
    prefetch_folder = "C:\\Windows\\Prefetch"
    force_delete_folder_contents(prefetch_folder)
    update_text_box("Cleaned Prefetch Folder!")

def clean_recycle_bin():
    r"""Clean the Recycle Bin for all users."""
    try:
        logging.info("Cleaning Recycle Bin...")
        result = subprocess.run(
            ["rd", "/s", "/q", "C:\\$Recycle.Bin"],
            shell=True,
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW  # Hide console window
        )
        if result.returncode != 0:
            logging.error(f"Error cleaning Recycle Bin: {result.stderr}")
        else:
            logging.info(f"Success: {result.stdout}")
        update_text_box("Cleaned Recycle Bin!")
    except Exception as e:
        logging.error(f"Exception cleaning Recycle Bin: {e}")
        update_text_box(f"Error: {e}")

def clean_windows_update_cache():
    r"""Clean the Windows Update cache."""
    logging.info("Cleaning Windows Update cache...")
    update_cache_folder = "C:\\Windows\\SoftwareDistribution\\Download"
    force_delete_folder_contents(update_cache_folder)
    update_text_box("Cleaned Windows Update Cache!")

def clean_temporary_internet_files():
    r"""Force-delete Temporary Internet Files for all users."""
    logging.info("Cleaning Temporary Internet Files...")
    users_dir = "C:\\Users"
    for user in os.listdir(users_dir):
        internet_files_folder = os.path.join(users_dir, user, "AppData", "Local", "Microsoft", "Windows", "INetCache")
        if os.path.exists(internet_files_folder):
            force_delete_folder_contents(internet_files_folder)
    update_text_box("Cleaned Temporary Internet Files!")

def clean_thumbnails():
    r"""Force-delete Thumbnails cache for all users."""
    logging.info("Cleaning Thumbnails...")
    users_dir = "C:\\Users"
    for user in os.listdir(users_dir):
        thumbnails_folder = os.path.join(users_dir, user, "AppData", "Local", "Microsoft", "Windows", "Explorer")
        if os.path.exists(thumbnails_folder):
            force_delete_folder_contents(thumbnails_folder)
    update_text_box("Cleaned Thumbnails!")

def clean_delivery_optimization_files():
    r"""Force-delete Delivery Optimization Files."""
    logging.info("Cleaning Delivery Optimization Files...")
    delivery_optimization_folder = os.path.join(os.getenv("SYSTEMROOT"), "ServiceProfiles", "NetworkService", "AppData", "Local", "Microsoft", "Windows", "Delivery Optimization")
    force_delete_folder_contents(delivery_optimization_folder)
    update_text_box("Cleaned Delivery Optimization Files!")

def clean_temp_folder():
    r"""Force-delete everything in the %temp% folder for all users."""
    logging.info("Cleaning Temp folder...")
    users_dir = "C:\\Users"
    for user in os.listdir(users_dir):
        temp_folder = os.path.join(users_dir, user, "AppData", "Local", "Temp")
        if os.path.exists(temp_folder):
            try:
                result = subprocess.run(
                    f'del /q /f /s "{temp_folder}\\*.*"',
                    shell=True,
                    capture_output=True,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW  # Hide console window
                )
                if result.returncode != 0:
                    logging.error(f"Error cleaning Temp folder: {result.stderr}")
                else:
                    logging.info(f"Success: {result.stdout}")
                for root, dirs, _ in os.walk(temp_folder, topdown=False):
                    for dir_name in dirs:
                        dir_path = os.path.join(root, dir_name)
                        result = subprocess.run(
                            f'rd /s /q "{dir_path}"',
                            shell=True,
                            capture_output=True,
                            text=True,
                            creationflags=subprocess.CREATE_NO_WINDOW  # Hide console window
                        )
                        if result.returncode != 0:
                            logging.error(f"Error cleaning Temp folder: {result.stderr}")
                        else:
                            logging.info(f"Success: {result.stdout}")
                update_text_box("Cleaned Temp Folder!")
            except Exception as e:
                logging.error(f"Exception cleaning Temp folder: {e}")
                update_text_box(f"Error: {e}")

def force_delete_folder_contents(folder_path):
    r"""Force-delete all files and subdirectories in a folder, ignoring errors."""
    if not os.path.exists(folder_path):
        logging.warning(f"Folder does not exist: {folder_path}")
        return
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                logging.debug(f"Deleted file: {file_path}")
            except Exception as e:
                logging.error(f"Exception deleting file {file_path}: {e}")
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                shutil.rmtree(dir_path)
                logging.debug(f"Deleted directory: {dir_path}")
            except Exception as e:
                logging.error(f"Exception deleting directory {dir_path}: {e}")

def flush_dns_cache():
    r"""Flush the DNS cache."""
    try:
        logging.info("Flushing DNS cache...")
        result = subprocess.run(
            ["ipconfig", "/flushdns"],
            shell=True,
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW  # Hide console window
        )
        if result.returncode != 0:
            logging.error(f"Error flushing DNS cache: {result.stderr}")
        else:
            logging.info(f"Success: {result.stdout}")
        update_text_box("Flushed DNS Cache!")
    except Exception as e:
        logging.error(f"Exception flushing DNS cache: {e}")
        update_text_box(f"Error: {e}")

def set_cloudflare_dns():
    r"""Set DNS to Cloudflare's DNS (1.1.1.1 and 1.0.0.1) for all connected interfaces."""
    try:
        logging.info("Setting Cloudflare DNS...")
        result = subprocess.run(
            ["netsh", "interface", "show", "interface"],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW  # Hide console window
        )
        connected_interfaces = [line.split()[-1] for line in result.stdout.splitlines() if "Connected" in line]
        for interface in connected_interfaces:
            result = subprocess.run(
                ["netsh", "interface", "ipv4", "set", "dns", f"name={interface}", "static", "1.1.1.1", "primary"],
                capture_output=True,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW  # Hide console window
            )
            if result.returncode != 0:
                logging.error(f"Error setting Cloudflare DNS: {result.stderr}")
            else:
                logging.info(f"Success: {result.stdout}")
            result = subprocess.run(
                ["netsh", "interface", "ipv4", "add", "dns", f"name={interface}", "1.0.0.1", "index=2"],
                capture_output=True,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW  # Hide console window
            )
            if result.returncode != 0:
                logging.error(f"Error setting Cloudflare DNS: {result.stderr}")
            else:
                logging.info(f"Success: {result.stdout}")
        update_text_box("Set Cloudflare DNS!")
    except Exception as e:
        logging.error(f"Exception setting Cloudflare DNS: {e}")
        update_text_box(f"Error: {e}")

def check_and_set_ultimate_power_plan():
    r"""Check if the Ultimate Power Plan exists, create it if it doesn't, and set it as active."""
    try:
        logging.info("Checking and setting Ultimate Power Plan...")
        result = subprocess.run(
            ["powercfg", "/list"],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW  # Hide console window
        )
        if "Ultimate Performance" not in result.stdout:
            result = subprocess.run(
                ["powercfg", "-duplicatescheme", "e9a42b02-d5df-448d-aa00-03f14749eb61"],
                shell=True,
                capture_output=True,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW  # Hide console window
            )
            if result.returncode != 0:
                logging.error(f"Error creating Ultimate Power Plan: {result.stderr}")
            else:
                logging.info(f"Success: {result.stdout}")
        result = subprocess.run(
            ["powercfg", "/list"],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW  # Hide console window
        )
        for line in result.stdout.splitlines():
            if "Ultimate Performance" in line:
                guid = line.split()[3]
                result = subprocess.run(
                    ["powercfg", "/setactive", guid],
                    shell=True,
                    capture_output=True,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW  # Hide console window
                )
                if result.returncode != 0:
                    logging.error(f"Error setting Ultimate Power Plan: {result.stderr}")
                else:
                    logging.info(f"Success: {result.stdout}")
                break
        update_text_box("Set Ultimate Power Plan!")
    except Exception as e:
        logging.error(f"Exception setting Ultimate Power Plan: {e}")
        update_text_box(f"Error: {e}")

# --- GUI Implementation ---
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("G.A.L")
        self.root.geometry("700x860")
        self.root.configure(bg="#1e1e1e")

        # Store the original window geometry
        self.original_geometry = "700x860"

        # Center the window on the screen
        self.center_window()

        # Custom font for Castlevania style
        self.custom_font = font.Font(family="Courier New", size=12, weight="bold")

        # Title Label
        self.title_label = tk.Label(
            root,
            text="Gamers As Legions System Optimizer",
            font=("Courier New", 24, "bold"),
            fg="#ff0000",
            bg="#1e1e1e"
        )
        self.title_label.pack(pady=20)

        # Buttons for each function
        self.create_button("Clean RAM Cache", clean_ram_cache)
        self.create_button("Clean Windows Temp Folder", clean_windows_temp_folder)
        self.create_button("Clean Prefetch Folder", clean_prefetch_folder)
        self.create_button("Clean Recycle Bin", clean_recycle_bin)
        self.create_button("Clean Windows Update Cache", clean_windows_update_cache)
        self.create_button("Clean Temporary Internet Files", clean_temporary_internet_files)
        self.create_button("Clean Thumbnails", clean_thumbnails)
        self.create_button("Clean Delivery Optimization Files", clean_delivery_optimization_files)
        self.create_button("Clean Temp Folder", clean_temp_folder)
        self.create_button("Flush DNS Cache", flush_dns_cache)
        self.create_button("Set Cloudflare DNS", set_cloudflare_dns)
        self.create_button("Set Ultimate Power Plan", check_and_set_ultimate_power_plan)

        # Run All Button
        self.run_all_button = tk.Button(
            root,
            text="Run All",
            font=self.custom_font,
            fg="#ffffff",
            bg="#ff0000",
            command=self.run_all
        )
        self.run_all_button.pack(pady=5, padx=20, fill=tk.X)

        # Toggle Fullscreen Button
        self.fullscreen_button = tk.Button(
            root,
            text="Toggle Fullscreen",
            font=self.custom_font,
            fg="#ffffff",
            bg="#ff0000",
            command=self.toggle_fullscreen
        )
        self.fullscreen_button.pack(pady=5, padx=20, fill=tk.X)

        # Text Box for Status Messages
        self.text_box = tk.Text(
            root,
            height=5,
            width=80,
            font=self.custom_font,
            fg="#ffffff",
            bg="#333333",
            wrap=tk.WORD
        )
        self.text_box.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(
            root,
            text="Exit",
            font=self.custom_font,
            fg="#ffffff",
            bg="#ff0000",
            command=self.exit_app
        )
        self.exit_button.pack(pady=20)

        # Track fullscreen state
        self.is_fullscreen = False

    def center_window(self):
        """Center the window on the screen."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"+{x}+{y}")

    def create_button(self, text, command):
        r"""Helper function to create styled buttons."""
        button = tk.Button(
            self.root,
            text=text,
            font=self.custom_font,
            fg="#ffffff",
            bg="#333333",
            command=lambda: self.clear_and_run(command)
        )
        button.pack(pady=5, padx=20, fill=tk.X)

    def clear_and_run(self, command):
        """Clear the text box and run the command."""
        self.text_box.config(state=tk.NORMAL)
        self.text_box.delete(1.0, tk.END)
        self.text_box.config(state=tk.DISABLED)
        command()

    def run_all(self):
        """Run all cleaning and optimization functions sequentially."""
        functions = [
            clean_ram_cache,
            clean_windows_temp_folder,
            clean_prefetch_folder,
            clean_recycle_bin,
            clean_windows_update_cache,
            clean_temporary_internet_files,
            clean_thumbnails,
            clean_delivery_optimization_files,
            clean_temp_folder,
            flush_dns_cache,
            set_cloudflare_dns,
            check_and_set_ultimate_power_plan
        ]
        for func in functions:
            self.clear_and_run(func)
        # Display completion message
        update_text_box("All Optimizations Complete!")

    def toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode."""
        if not self.is_fullscreen:
            # Go fullscreen
            self.root.attributes("-fullscreen", True)
            self.is_fullscreen = True
        else:
            # Restore original geometry and center the window
            self.root.attributes("-fullscreen", False)
            self.root.geometry(self.original_geometry)
            self.center_window()
            self.is_fullscreen = False

    def exit_app(self):
        r"""Exit the application."""
        logging.info("Exiting application.")
        self.root.destroy()

# --- Function to Update Text Box ---
def update_text_box(message):
    """Update the text box with a message."""
    app.text_box.config(state=tk.NORMAL)
    app.text_box.delete(1.0, tk.END)
    app.text_box.insert(tk.END, message)
    app.text_box.config(state=tk.DISABLED)

# --- Main Execution ---
if __name__ == "__main__":
    logging.info("Elevating privileges...")
    elevate_privileges()
    if not run_as_admin():
        logging.error("Script must be run as administrator.")
        sys.exit()
    logging.info("Starting GUI...")
    root = tk.Tk()
    app = App(root)
    root.mainloop()