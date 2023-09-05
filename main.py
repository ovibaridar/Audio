import gtts
import playsound


text = input("Enter the data")
sound = gtts.gTTS(text, lang="bn")
sound.save("wellcome.mp3")
playsound.playsound("wellcome.mp3")
print("done")
