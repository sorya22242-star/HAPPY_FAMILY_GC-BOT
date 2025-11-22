from instagrapi import Client
import time
import os

cl = Client()
cl.delay_range = [1, 5]

# Session save karega taaki baar-baar password na daalna pade
if os.path.exists("session.json"):
    cl.load_settings("session.json")
else:
    cl.login("happy_family_gc_bot", "@happy.sorya.com")  # ← Yahan apna IG username & password daal
    cl.dump_settings("session.json")

# ←←← APNA GROUP THREAD ID YAHAN DAAL (sabse important)
GROUP_THREAD_ID = "17843017835746397"  # ← Ye change kar apne GC ka

print("Instagram GC Auto Welcome Bot Started...")

sent_users = set()  # Already welcomed wale

while True:
    try:
        thread = cl.direct_thread("17843017835746397")
        participants = thread.users

        for user in participants:
            if user.pk not in sent_users:
                cl.direct_send(
                    cl.direct_send(
    f"""🌸 Welcome to our HAPPY FAMILY GC 💛 @{user.username}

Ab tum hamari cute si family ka hissa ban gaye ho ✨😍

Yaha sab ek-dusre ka khayal rakhte hain, 
thoda masti, thoda pyaar.. bas family vibes only! 🥰💕

⭐ Little Rules:
1) Sweetly baat karo 🍭
2) Gaali / fight bilkul nahi 🚫
3) Spam mat karo 🙅‍♂️
4) Bas enjoy karo aur family ke sath moments banao ✨

Chalo ab apna cute sa introduction de do, 
hamari family tumhe welcome karne ke liye excited hai 😭🌻""",
    [user.pk]
                    ))
                )
                print(f"Welcomed @{user.username}")
                sent_users.add(user.pk)
                time.sleep(15)  # Ban se bachne ke liye delay

        time.sleep(20)
    except Exception as e:
        print("Error:", e)
        time.sleep(60)
