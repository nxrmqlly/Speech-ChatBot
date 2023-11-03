import pyttsx3
import speech_recognition


def recg_speech() -> str:
    recg = speech_recognition.Recognizer()
    _res = None
    while not _res:
        try:
            with speech_recognition.Microphone() as mic:
                recg.adjust_for_ambient_noise(mic, 0.6)

                aud = recg.listen(mic)
                _res = recg.recognize_google(
                    aud, with_confidence=True, language="en-IN"
                )

        except speech_recognition.exceptions.UnknownValueError:
            recg = speech_recognition.Recognizer()
            print("❌ > Please Say that again!\n")
            continue

    return _res[0].lower()
