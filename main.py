from fastapi import FastAPI
import random

app = FastAPI()

# List of Roman Urdu jokes
jokes = [
    "Teacher: Tumhara naam kya hai? Student: Mera naam Batman hai. Teacher: Tumhare walid ka naam? Student: Bruce Wayne.",
    "Biwi: Suno ji, agar mujhe kuch ho gaya to aap dusri shaadi kar lenge? Shohar: Pagli, main to tumhara bhai ban ke aya tha, tumne hi shaadi kar li.",
    "Doctor: Aapko kis cheez se allergy hai? Patient: Biwi ke sawalon se. Doctor: To phir aapko dawa nahi, dua ki zaroorat hai.",
    "Pathan: Mujhe Titanic film ki ticket do. Ticket Clerk: Titanic to doob gayi hai. Pathan: Oh, mujhe pata nahi tha. Phir mujhe kisi aur ship ki ticket de do.",
    "Teacher: Agar tumhare paas 10 aam hain aur 2 gira diye to kitne aam bache? Student: Sir, 10 hi bache. Teacher: Wo kaise? Student: Giray hue aam uthakar wapas rakh lunga.",
    "Biwi: Aapko meri khoobsurti zyada pasand hai ya aqalmandi?​​Shohar: Mujhe tumhari yeh mazak karne ki aadat sabse zyada pasand hai.",
    "Pappu: Papa, aapko chand aur tarein mein kya farq lagta hai?​​Papa: Beta, chand raat ko nikalta hai aur tarein tumhare exam result dekh kar nikalte hain.",
    "​Teacher: Tumne homework kyun nahi kiya?​​Student: Sir, light nahi thi.​​Teacher: To candle jala lete.​​Student: Sir, candle se Wi-Fi nahi chalta.",
    "Pathan: Mujhe ek kilo doodh dena.​Doodhwala: Doodh to liquid hota hai, kilo mein nahi milta. Pathan: Achha, to ek kilo pani de do, doodh mein daal kar peeyunga.",
    "​Teacher: Tum class mein so rahe ho?​Student: Nahi sir, aapke lecture sunte sunte sapne dekh raha hoon.",
    "Pappu: Papa, mujhe ek bike leni hai.​Papa: Pehle apni exams mein pass ho jao, phir sochenge. Pappu: Papa, aap bhi na, choti choti baaton pe mazak karte hain."
]


@app.get("/")
def read_root():
    return {"messsage": "Welcome to Joke Generator API"}

@app.get("/jokes")
def get_joke():
    """ Returns a random joke """
    return {"Joke": random.choice(jokes)}
