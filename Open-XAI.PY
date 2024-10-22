import openai
import pyttsx3
import speech_recognition as sr

# إعداد واجهة OpenAI
openai.api_key = "YOUR_API_KEY"

# إعداد محرك النص إلى كلام
engine = pyttsx3.init()

# دالة لتحويل النص إلى كلام
def speak(text):
    engine.say(text)
    engine.runAndWait()

# دالة للاستماع إلى المستخدم وتحويل الصوت إلى نص
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("تحدث الآن...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="ar")
            return text
        except sr.UnknownValueError:
            return "لم أفهم ما قلت"
        except sr.RequestError:
            return "حدث خطأ في الاتصال بخدمة التعرف على الصوت"

# دالة للتحدث مع OpenAI GPT
def chat_with_gpt(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

# برنامج رئيسي
def main():
    print("مرحبًا! كيف يمكنني مساعدتك؟")
    speak("مرحبًا! كيف يمكنني مساعدتك؟")
    
    while True:
        # الاستماع إلى المستخدم
        user_input = listen()

        if user_input.lower() in ["خروج", "إنهاء", "إيقاف"]:
            print("إلى اللقاء!")
            speak("إلى اللقاء!")
            break
        
        # التفاعل مع GPT
        response = chat_with_gpt(user_input)
        print("الذكاء الاصطناعي: " + response)
        speak(response)

if __name__ == "__main__":
    main()
